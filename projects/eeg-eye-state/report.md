# EEG eye state: a time-aware neural-state classification study

## Abstract

We asked whether a simple model can distinguish open-eye and closed-eye states from
14-channel EEG, and whether short-term temporal context improves the prediction.
Using the UCI EEG Eye State dataset, we compared standardized pointwise EEG against
the same signal augmented with causal trailing means and standard deviations. We
used a class-balanced logistic-regression model and a chronological 70%/15%/15%
train/validation/test split. On the held-out block, pointwise EEG reached ROC AUC
**0.625** and balanced accuracy **0.557**. The first temporal-context model reached
ROC AUC **0.530** and balanced accuracy **0.485**, so this implementation did not
improve generalization. The negative result is retained: adding features is not
automatically beneficial, especially for one short continuous recording.

## Question and hypothesis

The question is whether short-term history helps decode a coarse neural state. We
expected temporal context to help because eye state changes over time, but treated
that as a testable hypothesis rather than a guaranteed result.

## Data and method

The UCI dataset contains 14,980 chronological samples from one 117-second recording,
with 14 EEG channels and a manually annotated binary eye-state label. The label is
approximately balanced in this file (44.9% closed-eye samples). We use a chronological
split to avoid leakage from neighboring time points across random folds.

The baseline uses the 14 channel values. The extended model adds a causal nine-sample
trailing mean and standard deviation for every channel. Both models standardize
features using training data inside a scikit-learn pipeline and use class-balanced
logistic regression.

## Results

| Model | Validation ROC AUC | Test ROC AUC | Test balanced accuracy | Test F1 |
|---|---:|---:|---:|---:|
| Pointwise EEG | 0.572 | **0.625** | **0.557** | **0.167** |
| EEG + causal context | **0.581** | 0.530 | 0.485 | 0.142 |

The extended model looked slightly better on validation but failed to generalize to
the final block. That divergence is exactly why the final test block was kept hidden
from model selection.

## Blocked cross-validation expansion

To test whether the final-block result depended on one arbitrary boundary, we added
five forward-chaining folds with `TimeSeriesSplit`. Each fold trains only on earlier
samples and evaluates the next contiguous block. The original 70/15/15 result above
is retained as the primary pre-specified holdout; these folds are a robustness
analysis, not a replacement for independent recordings.

| Model | Mean fold ROC AUC | SD | Range |
|---|---:|---:|---:|
| Pointwise EEG | 0.478 | 0.100 | 0.354–0.593 |
| EEG + causal context | 0.488 | 0.095 | 0.346–0.602 |

Across these non-independent time blocks, both models vary substantially and remain
near chance on average. The context model is only slightly higher on mean AUC; this
does not overturn the original final-block negative result or establish that context
helps generally.

### Temporal-window sweep

We also varied the causal window before looking at the results: 3, 9, 30, and 90
samples. The original nine-sample model remains the named primary extension; the
sweep is exploratory robustness analysis.

| Causal window | Final-block ROC AUC | Five-fold mean ROC AUC |
|---:|---:|---:|
| 3 samples | 0.599 | 0.491 |
| 9 samples | 0.530 | 0.488 |
| 30 samples | 0.599 | 0.548 |
| 90 samples | 0.556 | 0.567 |

Longer context performs better in this one recording’s blocked folds, but the fold
range remains broad and the analysis is not independent-subject validation. This
motivates testing multiple timescales on additional recordings rather than
selecting a winning window as a general rule.

### Label-shuffle negative control

As a control for the blocked evaluation, we globally permuted the eye-state
labels 20 times and reran the same five forward-chaining folds with the same
feature sets. The mean shuffled ROC AUC was **0.499** for pointwise EEG
(range 0.491–0.508) and **0.501** for causal context (range 0.491–0.512).
This is the expected near-chance control pattern. It supports treating the
observed time-series results as sensitive to the actual labels, while it does
not create evidence for generalization beyond this one recording.

### Purge-gap sensitivity

To test whether immediately adjacent training samples were influencing the
forward evaluation, we repeated the two primary blocked analyses with a
pre-specified **90-sample gap** before every test block. This gap matches the
largest window in the exploratory sweep. Mean ROC AUC was **0.448** for
pointwise EEG (range 0.288–0.572) and **0.443** for causal context (range
0.254–0.582). The gap analysis remains near or below chance and does not reverse
the negative interpretation.

### Recording-glitch sensitivity (added after the first results)

Four samples in the file are recording glitches (rows 898, 10386, 11509 and 13179):
values up to 715,897 where typical readings are about 4,000. The primary analysis did
not treat them specially, and its numbers above are unchanged. As a sensitivity check,
we limited each channel to the 0.5th–99.5th percentile of the **training rows only**
(recomputed for every fold) and refit.

| | Pointwise EEG | EEG + causal context |
|---|---:|---:|
| Final-block ROC AUC | **0.728** (was 0.625) | 0.609 (was 0.530) |
| Five-fold mean ROC AUC | 0.448 (was 0.478) | 0.476 (was 0.488) |

Handling the glitches clearly helps the final block, but the forward folds stay near
or below chance, and some folds are well below 0.5. A model that is reliably *worse*
than chance on a later block has learned a relationship that flips over time, so the
most likely explanation is drift across the 117-second recording, not only noise.
Because this check was added after seeing the results, it is reported as a
sensitivity analysis; the next study should decide glitch handling before any model
is fit.

## Limitations and next experiments

- One continuous recording cannot establish subject-level generalization.
- The label reflects eye state, not attention, alertness, or a clinical condition.
- A nine-sample window is an initial engineering choice, not a biologically optimal
  timescale.
- The next version should decide glitch handling in advance, and compare multiple
  windows and calibrated thresholds with blocked folds across additional recordings.
- Folds well below 0.5 suggest the signal drifts during the recording; a drift-aware
  model or per-block normalization is a natural next experiment.

## Reproduction

```bash
python3 src/analyze.py
```

Dataset citation: Roesler, O. (2013). *EEG Eye State*. UCI Machine Learning
Repository. DOI: [10.24432/C57G7J](https://doi.org/10.24432/C57G7J).
