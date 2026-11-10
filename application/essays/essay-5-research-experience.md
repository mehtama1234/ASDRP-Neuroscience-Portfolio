# Essay 5: Hands-on research experience (limit 375 words, up to 3 examples)

> **Draft for Amishi to make her own.** Same story as the website. Every sentence must be something you
> did and can explain. Where a step was done with your father or with AI tools, say so; the
> contribution ledger (`application/contribution-ledger.md`) lists each part. About 320 words.

---

**1. Does a mouse’s state change how its brain sees? (independent project, with my father)**
I learned Python and the basic science libraries, then loaded public Sensorium 2022 recordings:
thousands of brain cells in the part of the mouse brain that handles seeing, with pupil size and
running speed. I built two models of each cell’s response, one from the picture alone and one from
the picture plus the mouse’s state, and tested both on pictures they had never seen. State made the
guesses 25 to 33 percent better in all three mice. In the first mouse almost all of the gain came
from the pupil, not the running, and the cells that follow alertness gained about five times as much
as the rest. I tried to break the result: state taken from the wrong moments added nothing, and
leaving out any one mouse kept the gain. What I learned: a result needs a test that could make it fail.

**2. Can state be read from outside the head? (EEG study, in my portfolio)**
Using a public two-minute EEG recording, I tested whether a simple model could tell when a person’s
eyes were closed, always learning from earlier and testing on later, like a real app would. It worked
on one stretch and drifted to a coin flip over time. [Only if you ran or reran it yourself:] A
follow-up with brain-wave bands, planned before running, helped on average but still dipped below
a coin flip. I reported it as “did not hold up”, because that is what the rule I set said.

**3. From findings to features (Next Step and Helper Jobs)**
[In your words: what you designed, built or tested in Next Step, and your part in Helper Jobs for
Pragnya’s outings.] Because the EEG showed state is hard to read from outside, Next Step asks people
how much energy they have instead of guessing, and shows less on a low day.
