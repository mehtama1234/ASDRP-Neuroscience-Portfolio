# Recording script: the video in Amishi’s own voice

Record each slide as its own file, in a quiet room, on a phone or laptop. Read it the way you would say it to a friend; change any word that doesn’t sound like you, as long as it stays true. Save each one as `website/video/voice/NN.wav` (or `.m4a`), for example `01.wav` for slide 1, and run:

```
python3 website/presentation/build_video.py <folder with the Kokoro voice files>
```

Any slide with a recording uses your voice; any slide without one keeps the computer voice, so you can do it in parts. The captions are rebuilt from the text below, so if you change the words, change them here too (in `website/presentation/build_video.py` or the slide notes).

## 01 · From neurons to next steps

From neurons to next steps. This is one question, followed from real life into the lab and back out again: two studies with public brain recordings, the two apps their findings shaped, and where the work goes next.

## 02 · The loop

Here is the whole story. Real life raised a question. A mouse study helps us understand it. An EEG study asks whether we can measure it in a person. The answers shape the design of two apps. And the last step tests the apps back in real life.

## 03 · Chapter 1, real life

This is where it started. The same instruction works one moment and is lost the next. That made us ask whether the brain’s state itself changes what gets in.

## 04 · Chapter 2

Scientists shared recordings of thousands of brain cells from mice watching pictures. We built two simple guessers. Guesser A only knows the picture. Guesser B also knows how wide the pupils were and how fast the mouse was running. Both are tested on pictures they have never seen.

## 05 · Chapter 2 result

In every mouse, guesser B wins. The scores look small because single brain cells are noisy, so the thing to look at is the jump from A to B: a quarter to a third better. That is a link, not proof of cause.

## 06 · Inside the first mouse

Looking inside the first mouse, from Amishi’s own analysis. Adding running barely changed anything; pupil size, a sign of how alert the mouse is, gave almost the whole gain. Nine in ten brain cells were guessed better, and the cells that follow alertness gained about five times as much as the rest.

## 07 · Chapter 2 checks

We tried to break it. When we gave guesser B the wrong moments’ state, the gain disappeared. Leaving out any one mouse kept the gain. So state really matters inside the brain. Next question: can we read it from outside, in a person?

## 08 · Chapter 3

Now a person. EEG is a cap of sensors on the head. Closing your eyes is one of the easiest changes for it to see. If a simple model cannot read even that reliably, quieter states like tiredness will be harder. We always learn from earlier and test on later.

## 09 · Chapter 3 result

On one stretch it worked reasonably well. But when we tested it on five stretches across the recording, it averaged a coin flip.

## 10 · Chapter 3

Each dot is one stretch. They land on both sides of a coin flip, and some are worse than guessing. Within two minutes, the signal drifted.

## 11 · Experiment 2

So we asked a follow-up and wrote the plan down before running it: would the strength of brain-wave bands, like alpha, hold steady where raw readings did not? They helped on average, but two of five stretches still fell below a coin flip. By the rule we set beforehand, it did not hold up. So a tool should not try to guess someone’s state from a sensor.

## 12 · Chapter 4

This is where the science turns into design. Each finding gives a rule, and each rule is a real feature in the apps.

## 13 · Chapter 4

Here they are. Next Step asks about energy and shrinks the plan. Save and pause and I’m stuck make it easy to stop and come back. Helper Jobs gives one picture step at a time, read aloud, with a Help button that reaches a volunteer.

## 14 · Chapter 5

Next, with an ASDRP mentor, we run four more data experiments and write the first paper, on why the EEG drifts. Then design studies with the people the apps are for. Longer term, the joined-up question: does designing for state help people learn?

## 15 · The loop, who did what, and where to see everything.

So, the loop. Real life raised the question. The mouse showed that a brain’s state changes what it takes in. The EEG showed that state is hard to read from outside. So the apps ask how someone is doing, and keep each step small. Everything in this video is on the website, with the phone tour, the slides and both apps linked from it.
