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
random row shuffling. This is a reproduction of one continuous recording, not
evidence of generalization to new participants.
