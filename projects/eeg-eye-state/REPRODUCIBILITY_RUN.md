# EEG reproducibility run

On 2026-11-08, a fresh virtual environment was created and installed from
`requirements.txt`. The resolved core versions were NumPy 2.5.4, SciPy 1.18.1,
and scikit-learn 1.9.1.

Running `python src/analyze.py` reproduced the committed metrics:

| Model | Test ROC AUC |
|---|---:|
| Pointwise EEG | 0.6252065 |
| EEG + causal temporal context | 0.5296496 |

The run uses the retained ARFF file, the chronological 70/15/15 split, and no
random row shuffling. It also writes five forward-chaining blocked-fold results
under `blocked_cross_validation` in `results/metrics.json`; mean ROC AUC is 0.478
for pointwise EEG and 0.488 for causal context. This is still one continuous
recording, not evidence of generalization to new participants. The same file also
contains the exploratory 3/9/30/90-sample temporal-window sweep.

The same run now adds a pre-specified label-shuffle negative control: 20 global
permutations of the eye-state labels, evaluated with the same five forward-
chaining folds. The mean shuffled ROC AUC is 0.499 (pointwise) and 0.501
(causal context), with ranges 0.491–0.508 and 0.491–0.512. These values are
consistent with chance and are a control result, not evidence of independent-
participant generalization.

Finally, a 90-sample purge gap was inserted before every forward test block, equal
to the largest exploratory context window. Mean ROC AUC was 0.448 for pointwise
EEG (range 0.288–0.572) and 0.443 for causal context (range 0.254–0.582). The
gap sensitivity remains near or below chance and does not reverse the study's
negative interpretation; it is still one continuous recording.
