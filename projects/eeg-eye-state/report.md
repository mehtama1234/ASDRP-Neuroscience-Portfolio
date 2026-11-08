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

## Limitations and next experiments

- One continuous recording cannot establish subject-level generalization.
- The label reflects eye state, not attention, alertness, or a clinical condition.
- A nine-sample window is an initial engineering choice, not a biologically optimal
  timescale.
- The next version should compare multiple windows, calibrated thresholds, and a
  blocked cross-validation protocol across additional recordings.

## Reproduction

```bash
python3 src/analyze.py
```

Dataset citation: Roesler, O. (2013). *EEG Eye State*. UCI Machine Learning
Repository. DOI: [10.24432/C57G7J](https://doi.org/10.24432/C57G7J).
