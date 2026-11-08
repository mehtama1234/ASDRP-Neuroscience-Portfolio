# Mouse visual cortex and behavioral state

## Question

Does knowing what a mouse is doing—especially its arousal and locomotion—help us
predict activity in visual cortex beyond the visual stimulus alone?

## Current result

Using Sensorium 2022 recordings and a transparent ridge-regression encoding model,
the project reports an increase in mean held-out correlation from **0.126** for a
stimulus-only model to **0.158** when behavior is added. The reported gain is driven
primarily by pupil-linked arousal in the analyzed mouse.

## Next experiments

- Repeat the analysis across additional mice.
- Compare animals with different amounts of running behavior.
- Add confidence intervals and statistical tests.
- Separate exploratory analysis from confirmatory evaluation.
- Document preprocessing and possible leakage risks.
- Compare pixel, PCA, and CNN feature representations.

## Displayable artifacts

- Neuron explorer
- Stimulus-only versus behavior-enhanced model dashboard
- Cortical spatial map
- Research report
- Five-minute presentation and short video

Implementation: [AmishI123/neuroscience-project](https://github.com/AmishI123/neuroscience-project)
