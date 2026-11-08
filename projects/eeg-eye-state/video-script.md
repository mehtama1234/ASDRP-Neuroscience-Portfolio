# Three-minute project video script

## 0:00–0:30 — The question

“The mouse project asks whether behavior improves neural prediction. This second
project asks a related but different question: can a short EEG recording reveal a
coarse brain state, and does recent history help?”

## 0:30–1:10 — The data

Show the 14-channel UCI recording and explain that eye state is a label, not a
diagnosis. Emphasize that the data are chronological and come from one recording.

## 1:10–2:00 — The experiment

Compare the pointwise logistic-regression baseline with the causal temporal-context
model. Show the chronological train, validation, and test blocks.

## 2:00–2:35 — The result

Show the test ROC AUC values: 0.625 for pointwise EEG and 0.530 for the context
extension. Explain that validation favored the extension slightly, but the final
held-out block did not.

## 2:35–3:00 — The lesson

“The result is not that temporal context never helps. It is that this first feature
design did not generalize on this recording. A transparent negative result tells us
exactly what the next experiment must test: more recordings and multiple timescales.
Our five forward-chaining folds also vary widely and average near chance, so the
small context advantage there is not a population claim.”
