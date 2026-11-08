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
