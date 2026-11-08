# Mouse visual cortex and behavioral state

## Question

Does knowing what a mouse is doing—especially its arousal and locomotion—help us
predict activity in visual cortex beyond the visual stimulus alone?

## Current result

Using Sensorium 2022 recordings and a transparent ridge-regression encoding model,
the original mouse rises from **0.126** for a stimulus-only model to **0.158** when
behavior is added; a second mouse rises from **0.154** to **0.203** under the same
pipeline. Pupil improves both animals, while the running contribution varies by
animal. These are predictive results, not causal evidence.

## Next experiments

- Repeat the analysis across additional mice beyond the two already evaluated.
- Compare animals with different amounts of running behavior.
- Add confidence intervals and statistical tests.
- Separate exploratory analysis from confirmatory evaluation.
- Document preprocessing and possible leakage risks.
- Compare pixel, PCA, and CNN feature representations.

The flagship repository now includes a pinned core dependency manifest and a formal
[replication protocol](https://github.com/AmishI123/neuroscience-project/blob/main/docs/REPLICATION_PLAN.md).

## Displayable artifacts

- Neuron explorer
- Stimulus-only versus behavior-enhanced model dashboard
- Cortical spatial map
- Research report
- Five-minute presentation and short video

Implementation: [AmishI123/neuroscience-project](https://github.com/AmishI123/neuroscience-project)
