"""Builds the portfolio pages with the exact Helper Jobs / Next Step stylesheets, icons, illustrations and
markup (website/assets/base.css, experience.css, theme-atlas.css, styles.css, icons.js, art.js are copied
unchanged from neurocomms/helper-jobs). Only the charts are new (charts.css, charts.js).
Old page names redirect to the new ones. Run: python3 website/build_pages.py"""
from pathlib import Path

W = Path(__file__).resolve().parent
REPO = "https://github.com/mehtama1234/ASDRP-Neuroscience-Portfolio"
FLAGSHIP = "https://github.com/AmishI123/neuroscience-project"
NEXT_STEP = "https://mehtama1234.github.io/neuro-divergent/"
HELPER_JOBS = "https://helper-jobs.onrender.com"


def ic(name):
    return f'<span class="lm-icon" data-icon="{name}"></span>'


def page(name, title, description, body):
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#F3ECE1" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <link rel="icon" href="assets/icon.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="assets/base.css" />
  <link rel="stylesheet" href="assets/experience.css" />
  <link rel="stylesheet" href="assets/theme-atlas.css" />
  <link rel="stylesheet" href="assets/styles.css" />
  <link rel="stylesheet" href="assets/charts.css" />
</head>
<body>
  <aside class="public-demo-banner" aria-label="About this portfolio">ASDRP application portfolio · Public data only · Every number comes from committed results</aside>
  <a class="skip-link" href="#app">Skip to the page</a>
  <header>
    <a class="brand" href="index.html"><span class="mark" aria-hidden="true">n.</span> From neurons to next steps</a>
    <span class="header-status"><span class="badge">Public data only</span><span class="badge">Plans marked as plans</span></span>
    <a class="header-link" href="{REPO}">Source code</a>
  </header>
  <main id="app" tabindex="-1">
{body}
  </main>
  <script src="assets/icons.js"></script><script src="assets/icons-extra.js"></script><script src="assets/art.js"></script><script src="assets/science-art.js"></script>
  <script src="assets/results.js"></script><script src="assets/charts.js"></script><script src="assets/site.js"></script>
</body>
</html>
"""
    (W / name).write_text(html)


def heading(back, eyebrow, title, sub, art):
    return f"""    <div class="lm-head"><div class="hj-heading"><a class="back-button" href="{back[0]}">← <span>{back[1]}</span></a><p class="eyebrow">{eyebrow}</p><h1>{title}</h1><p class="hj-sub">{sub}</p></div><div class="hj-art" data-art="{art}"></div></div>"""


def chart(cid, kicker, title, text, note):
    return f'<div class="chart-card"><div data-chart="{cid}"></div><div><p class="lm-k">{kicker}</p><h3>{title}</h3><p>{text}</p><p class="chart-note">{note}</p></div></div>'


def grid(items):
    return '<ul class="lm-grid">' + "".join(f'<li><div class="lm-top">{ic(i)}<p class="lm-k">{k}</p></div><h3>{h}</h3><p>{p}</p></li>' for i, k, h, p in items) + "</ul>"


def phone(app, kicker, title, middle, cap, sub):
    return f'<li><div class="phone" aria-hidden="true"><div class="ph-bar"><span>{app}</span><em class="ph-picture-tag">Result</em></div><div class="ph-body"><p class="ph-k">{kicker}</p><p class="ph-title">{title}</p>{middle}</div></div><strong>{cap}</strong><span>{sub}</span></li>'


def bridge(label, text, href, link):
    return f'<section class="landing-problems answer bridge"><p class="lp-energy"><b>{label}</b> {text} <a href="{href}">{link} →</a></p></section>'


def nav(prev, nxt):
    home = '' if 'index.html' in (prev[0], nxt[0]) else '<a href="index.html">All chapters</a>'
    return f'<p class="landing-note"><a href="{prev[0]}">← {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} →</a>{home}</p>'


# ---------------- landing ----------------
LANDING_ART = """<svg class="landing-art" viewBox="0 0 440 400" aria-hidden="true" focusable="false">
          <path class="la-line" d="M210 96 C 228 100, 222 120, 236 122"/><path class="la-line" d="M318 170 C 300 214, 250 204, 214 232"/><path class="la-line" d="M216 304 C 226 304, 228 302, 238 302"/>
          <g class="la-card" transform="translate(14 18) rotate(-2)"><rect width="196" height="104"/><rect class="la-top" width="196" height="5"/><text class="la-kick" x="14" y="26">1 · REAL LIFE</text><text class="la-title" x="14" y="56">Same words?</text><text class="la-small" x="14" y="80">They land one moment and</text><text class="la-small" x="14" y="94">are lost the next. Why?</text></g>
          <g class="la-card" transform="translate(234 66) rotate(2)"><rect width="192" height="104"/><text class="la-kick" x="14" y="24">2 · UNDERSTAND</text><text class="la-title" x="14" y="52">Picture + behaviour</text><rect class="la-note" x="14" y="64" width="164" height="28"/><text class="la-k2" x="24" y="82">BETTER IN ALL 3 MICE</text></g>
          <g class="la-card la-ink" transform="translate(18 214) rotate(1.5)"><rect width="196" height="116"/><text class="la-kick" x="14" y="24">3 · MEASURE</text><text class="la-title" x="14" y="52">Eyes closed?</text><text class="la-k2" x="14" y="74">5 BLOCKS IN TIME</text><text class="la-body" x="14" y="94">The signal drifts.</text></g>
          <g class="la-card" transform="translate(238 236) rotate(-2)"><rect width="190" height="132"/><text class="la-kick" x="14" y="24">4 · DESIGN, THEN TEST</text><circle cx="30" cy="54" r="14"/><path class="la-tick" d="M24.5 54l3.5 3.5 7-7"/><text class="la-title" x="52" y="60">Ask, don’t guess</text><rect class="la-pill" x="14" y="88" width="72" height="22" rx="11"/><text class="la-pt" x="50" y="103" text-anchor="middle">Next Step</text><rect class="la-pill" x="92" y="88" width="82" height="22" rx="11"/><text class="la-pt" x="133" y="103" text-anchor="middle">Helper Jobs</text></g>
        </svg>"""

page("index.html", "From neurons to next steps · an ASDRP neuroscience portfolio",
     "From neurons to next steps: a question from real life, tested in a mouse’s visual cortex and a person’s brain waves, then turned into two apps that help.", f"""    <section id="home" class="screen active landing" aria-labelledby="home-title">
      <div class="landing-hero">
        <div class="landing-hero-text">
          <p class="landing-kicker">An ASDRP neuroscience portfolio · Amishi Mehta</p>
          <h1 id="home-title">From neurons to next steps</h1>
          <p class="landing-lede">At Pragnya’s outings for neurodivergent kids and adults, and in everyday schoolwork, the same instruction can land one moment and be lost the next. That raised a question: <b>does what a brain is doing change what it takes in?</b> We tested it in two public brain recordings, tried hard to break each answer, and turned what held up into the design of two apps.</p>
          <div class="landing-actions">
            <a class="button primary" href="#story">Read the story <span aria-hidden="true">→</span></a>
            <a class="button secondary" href="mouse.html">Start with the mouse study</a>
          </div>
          <p class="landing-try-note">Public data only. A prediction is not a cause. Plans are marked as plans.</p>
          <ul class="landing-parts" aria-label="What makes it work">
            <li><a href="mouse.html"><span data-icon="eye"></span><b>Understand</b><small>Mouse: state changes the cortex</small></a></li>
            <li><a href="eeg.html"><span data-icon="activity"></span><b>Measure</b><small>EEG: readable once, then it drifts</small></a></li>
            <li><a href="#checks"><span data-icon="arrows-shuffle"></span><b>Checked</b><small>Every result tested to break it</small></a></li>
            <li><a href="tools.html"><span data-icon="heart-handshake"></span><b>Design</b><small>Findings become app features</small></a></li>
          </ul>
          <p class="landing-voice"><a href="next.html"><span data-icon="flask"></span>Chapter 5: where this goes next, with more studies, design research and papers.</a></p>
        </div>
        {LANDING_ART}
      </div>

      <section class="landing-problems" id="story" aria-labelledby="landing-problems-title">
        <h2 class="landing-subhead" id="landing-problems-title">One loop, five chapters</h2>
        <p class="lp-lead">It starts in real life and ends back there. Each chapter answers the question the last one raised.</p>
        <ol aria-label="Five chapters" tabindex="0">
          <li><p class="lp-k">1 · Real life</p><h3>Same words, different moment.</h3><p class="lp-pain">At Pragnya’s outings and in schoolwork, a step that is easy when someone is calm can be lost when they are tired, rushed or overloaded. Is that the brain itself?</p><p class="lp-fix"><b>To find out:</b> look inside a brain while its state changes.</p></li>
          <li><p class="lp-k">2 · Understand</p><h3>A mouse’s state shapes what its visual cortex does.</h3><p class="lp-pain">Thousands of neurons, recorded while mice watched pictures. We predicted each neuron from the picture alone, then from the picture plus pupil size and running.</p><p class="lp-fix"><b>Found:</b> knowing the mouse’s state made prediction 25–34% better, in all three mice. <a href="mouse.html">Read chapter 2 →</a></p></li>
          <li><p class="lp-k">3 · Measure</p><h3>Can a sensor read state in a person?</h3><p class="lp-pain">Eyes closed is one of the clearest changes in brain waves. One person, 14 scalp sensors, 117 seconds, and the model is always tested on what comes later.</p><p class="lp-fix"><b>Found:</b> on one stretch, yes (0.625, or 0.728 with four glitches limited). Across the recording it drifted to 0.478, about a coin flip. <a href="eeg.html">Read chapter 3 →</a></p></li>
          <li><p class="lp-k">4 · Design</p><h3>From findings to features.</h3><p class="lp-pain">If state matters but cannot be read from outside, an app should ask, not guess. It should show less on a low-energy day, and make pausing and coming back easy.</p><p class="lp-fix"><b>Built into:</b> Next Step, by Amishi Mehta, for schoolwork, and Helper Jobs, a family project, for real jobs at Pragnya outings. <a href="tools.html">Read chapter 4 →</a></p></li>
          <li><p class="lp-k">5 · Test, then go further</p><h3>Where this goes next.</h3><p class="lp-pain">Four more data experiments, design studies with Pragnya volunteers and families, and papers others can check.</p><p class="lp-fix"><b>The aim:</b> one research direction, where neuroscience and design meet. <a href="next.html">Read chapter 5 →</a></p></li>
        </ol>
        <p class="lp-energy"><b>The loop:</b> real life raised the question; the mouse showed that state changes what a brain takes in; the EEG showed that state is hard to read from outside; so the apps ask how someone is doing and keep each step small. The last experiment takes the apps back to real life to see if they help. <span>Three mice and one person are a start, not a rule for everyone.</span></p>
        <div class="lp-how"><p class="lp-how-short"><b>What this does not show yet:</b> whether the pattern holds in more animals and more people, what causes it, or whether the apps help. Each of those is an experiment in chapter 5.</p></div>
      </section>

      <section class="landing-more" id="checks" aria-labelledby="landing-more-title">
        <div class="lm-head"><div><h2 class="landing-subhead" id="landing-more-title">How we tried to break each result</h2><p class="lp-lead">Nothing in the story counts until it has survived a check that could have made it disappear.</p></div><div class="hj-art" data-art="controls"></div></div>
        {grid([
            ('arrows-shuffle', 'Shuffle the answers', 'A coin flip, as it should be', 'With the EEG labels scrambled 20 times, the score falls to 0.499. Mouse behaviour shuffled 20 times adds almost nothing.'),
            ('timeline', 'Split by time', 'Train on the past, test the future', 'No random mixing of neighbouring moments, which makes EEG results look far better than they are.'),
            ('route-2', 'Leave a gap', '90 samples between train and test', 'Removing the moments right next to each test block keeps the EEG result near chance: it is not leakage.'),
            ('users', 'Leave one out', 'No single mouse carries it', 'The average gain stays positive (+0.040 to +0.048) whichever mouse is left out.'),
            ('filter', 'Glitch check', 'Four broken samples found', 'Values up to 715,897 where normal is about 4,000. Limiting them helps the last block, not the drift.'),
            ('code', 'Every number traced', 'Rebuilt from saved results', 'The charts are generated from the committed results files, and the EEG study reruns with one command.'),
        ])}
      </section>

      <h2 class="landing-subhead">The story in three numbers</h2><p class="landing-demo-note">One from inside a brain, two from outside. Each chapter has the charts and the checks.</p>
      <ol class="landing-demo" aria-label="Three results" tabindex="0">
        {phone('Mouse study', 'THREE MICE', 'Behaviour helps', '<div class="ph-paused"><b>+0.032 to +0.049</b><em>held-out correlation</em></div><p class="ph-small">Pupil helps all three mice.</p>', 'State matters inside', 'Adding pupil and running made prediction a quarter to a third better.')}
        {phone('EEG study', 'FINAL TEST BLOCK', '0.625 → 0.728', '<p class="ph-note">After limiting 4 glitches</p><p class="ph-small">0.5 is a coin flip, 1.0 is perfect.</p>', 'Readable once…', 'A simple model read eye state well on the last part of the recording.')}
        {phone('EEG study', 'FIVE BLOCKS IN TIME', 'Near a coin flip', '<div class="ph-paused ph-red"><b>Average 0.478</b><em>some blocks well below 0.5</em></div><p class="ph-small">So the tools don’t try to guess.</p>', '…but not over time', 'Within two minutes the link between signal and eye state shifted.')}
      </ol>

      <div class="landing-facts">
        <div class="landing-fact"><h2>Who did what</h2><p>The studies were done by the applicant with a parent collaborator, who helped scope questions, review code and debug. Software tools, including AI assistants, helped build this website. The <a href="{REPO}/blob/main/application/contribution-ledger.md">contribution ledger</a> lists each part.</p></div>
        <div class="landing-fact landing-fact-not"><h2>What it is not</h2><p>It is not a clinical or diagnostic study. Three mice and one EEG recording cannot speak for all animals or people, and a model that predicts something does not show what causes it.</p></div>
      </div>
      <p class="landing-note">Data: Sensorium 2022 (Willeke et al., 2022) and UCI EEG Eye State (Roesler, 2013). <a href="mouse.html">Mouse study</a><a href="eeg.html">EEG study</a><a href="tools.html">Tools</a><a href="next.html">Next experiments</a></p>
    </section>""")

# ---------------- mouse ----------------
page("mouse.html", "Mouse visual cortex · From neurons to next steps",
     "Chapter 2: knowing a mouse’s pupil size and running speed made its visual cortex 25–34% easier to predict, in all three mice.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'All chapters'), 'Chapter 2 · Understand · Mouse study', '<span id="page-title">Does a mouse’s state change what its visual cortex does?</span>', 'We predicted thousands of neurons from the picture a mouse saw, then again with its pupil size and running speed added. If state did not matter, the extra information would add nothing.', 'mouseHero')}
      <section class="landing-problems answer"><p class="lp-energy"><b>It mattered, in all three mice.</b> With pupil and running added, prediction on unseen pictures rose by +0.032 to +0.049, a quarter to a third better than the picture alone. <span>A better prediction shows a link, not a cause.</span></p></section>

      <section class="landing-more" aria-labelledby="how-title">
        <div class="lm-head"><div><h2 class="landing-subhead" id="how-title">How we tested it</h2><p class="lp-lead">The same steps for every mouse, scored on images the model never saw.</p></div><div class="hj-art" data-art="mouseStudy"></div></div>
        {grid([
            ('photo', 'The picture', 'Shrunk and summarised', 'Each image is shrunk 4×4 and summarised with 150 principal components.'),
            ('eye', 'The behaviour', 'Pupil and running', 'Pupil size and running speed recorded at the same moment as the brain activity.'),
            ('chart-dots', 'The model', 'Ridge regression', 'One simple model per neuron, standardised on training data only.'),
            ('target', 'The test', 'Official held-out images', 'Scored by the correlation between predicted and real activity, averaged over neurons.'),
            ('books', 'The data', 'Sensorium 2022', 'Public recordings from mouse primary visual cortex, thousands of neurons per mouse.'),
            ('users', 'The unit', 'Each mouse counts once', 'Neurons are not treated as separate animals.'),
        ])}
      </section>

      <h2 class="landing-subhead">The results</h2>
      {chart('mouse-scores', 'Result', 'Every mouse is easier to predict once we know its state.', 'The picture explains part of what visual cortex does. Whether the mouse is alert and moving explains more, in every animal.', 'Mean held-out Pearson correlation across neurons, Sensorium 2022 official test images.')}
      {chart('mouse-gain', 'Gain', 'The size of the gain differs by mouse.', 'Pupil size helps all three animals. How much running adds changes from mouse to mouse, so each animal is reported on its own.', 'Gain = score with behaviour minus score with the picture only.')}

      <section class="landing-more" aria-labelledby="checks-title" id="checks">
        <div class="lm-head"><div><h2 class="landing-subhead" id="checks-title">Trying to break the result</h2><p class="lp-lead">Three checks that could have made the gain disappear.</p></div><div class="hj-art" data-art="controls"></div></div>
        {grid([
            ('arrows-shuffle', 'Shuffle the behaviour', 'Almost no gain', 'Behaviour scrambled across trials, 20 times per mouse, adds almost nothing. The gain needs behaviour from the same moment.'),
            ('users', 'Leave one mouse out', 'Still positive', 'The average gain stays positive whichever mouse is removed, so no single recording carries the result.'),
            ('eye', 'Pupil or running?', 'Pupil helps every mouse', 'Taking each signal away in turn: pupil improves all three mice; running varies by animal.'),
        ])}
      </section>
      {chart('mouse-loo', 'Leave one mouse out', 'Positive without any one animal.', 'This makes the three-mouse pattern less dependent on one recording. It is a check, not an estimate for all mice.', 'Average gain over the two remaining mice.')}

      <div class="landing-facts" style="margin-top:28px">
        <div class="landing-fact"><h2>Code and data</h2><p>The analysis is in <a href="{FLAGSHIP}">AmishI123/neuroscience-project</a> (notebooks 01–05 and <code>src/summarize_replication.py</code>). The numbers here are copied from its committed summary into <code>website/build_results.py</code>. Data: Willeke et al. (2022), <i>The Sensorium competition on predicting large-scale mouse primary visual cortex activity</i>, arXiv:2206.08666.</p></div>
        <div class="landing-fact landing-fact-not"><h2>What it does not show</h2><p>Three mice cannot speak for all mice. A better prediction does not show that arousal or running cause the change. The report’s intervals are within each animal, not for the whole population.</p></div>
      </div>
      {bridge('What chapter 2 tells us:', 'the same picture lands differently depending on the state the mouse is in. So the next question is whether that state can be read from outside the head, in a person.', 'eeg.html', 'Chapter 3')}
      {nav(('index.html', 'All chapters'), ('eeg.html', 'Chapter 3 · EEG'))}
    </section>""")

# ---------------- EEG ----------------
page("eeg.html", "EEG eye state · From neurons to next steps",
     "Chapter 3: a simple model reads eye state from one person’s EEG on one stretch of time, but not reliably across the recording, because the signal drifts.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'All chapters'), 'Chapter 3 · Measure · EEG study', '<span id="page-title">Can a sensor on the head tell when someone’s eyes are closed?</span>', 'Eyes closed is one of the clearest changes in brain waves. If a simple model cannot read it reliably over two minutes, quieter states like tiredness will be harder still.', 'eegHero')}
      <section class="landing-problems answer"><p class="lp-energy"><b>On one stretch, yes. Over time, no.</b> The model scored 0.625 on the last part of the recording, and 0.728 once four glitch samples were limited. Tested block by block across the recording, it averaged 0.478, about a coin flip. <span>Giving it the last few moments of signal did not help.</span></p></section>

      <section class="landing-more" aria-labelledby="how-title">
        <div class="lm-head"><div><h2 class="landing-subhead" id="how-title">How we tested it</h2><p class="lp-lead">Always train on the past, and test on the future.</p></div><div class="hj-art" data-art="eegStudy"></div></div>
        {grid([
            ('activity', 'The recording', 'One person, 117 seconds', '14 channels and 14,980 samples, about 45% with eyes closed.'),
            ('timeline', 'Split by time', '70 · 15 · 15', 'Learn on the first 70%, choose on the next 15%, test once on the last 15%. No random mixing.'),
            ('chart-dots', 'Two models', 'A moment, or a moment plus history', 'One sees a single moment; the other also sees the average and spread of the last 9 samples.'),
            ('target', 'The score', 'ROC AUC', '0.5 is a coin flip and 1.0 is perfect.'),
            ('route-2', 'Five blocks', 'Forward in time', 'Train on everything before a block, test on the block, five times.'),
            ('books', 'The data', 'UCI EEG Eye State', 'Roesler (2013), a public recording with each moment marked eyes open or closed.'),
        ])}
      </section>

      <h2 class="landing-subhead">The results</h2>
      {chart('eeg-holdout', 'Final test block', 'Good on one block, better without glitches.', 'Four samples are recording glitches, with values up to 715,897 where normal readings are about 4,000. Limiting each channel to the range seen in training lifts the simple model from 0.625 to 0.728.', 'The glitch check was added after the first results, so it is shown next to the original numbers, not instead of them.')}
      {chart('eeg-folds', 'Five blocks in time', 'Over time, it drifts to a coin flip.', 'Scores scatter around 0.5, and several blocks fall well below it. A model that is reliably worse than chance has learned a pattern that flips later in the recording.', 'That points to drift across the 117 seconds, not only noise. Limiting glitches and leaving a time gap do not change it.')}

      <section class="landing-more" aria-labelledby="checks-title" id="checks">
        <div class="lm-head"><div><h2 class="landing-subhead" id="checks-title">Making sure it is not the pipeline</h2><p class="lp-lead">Three checks on how the result was produced.</p></div><div class="hj-art" data-art="controls"></div></div>
        {grid([
            ('arrows-shuffle', 'Shuffle the answers', '0.499 average', 'Eye-state labels scrambled 20 times give a coin flip, as they should. The pipeline does not invent signal.'),
            ('route-2', 'Leave a gap', '0.448 average', 'Removing the 90 samples before each test block keeps the result near chance, so it is not leakage from neighbours.'),
            ('filter', 'Limit the glitches', 'Rows 898, 10386, 11509, 13179', 'Limits are learned from training rows only, separately for each block, so the test never shapes them.'),
        ])}
      </section>
      {chart('eeg-windows', 'How much history', 'Longer history looks better, but we did not pick a winner.', 'The 3, 9, 30 and 90-sample windows were set before looking. Ninety does best on average, but choosing it now would be fitting this one recording.', 'Next: test window lengths on new recordings before choosing.')}

      <div class="landing-facts" style="margin-top:28px">
        <div class="landing-fact"><h2>Rerun it</h2><p><code>python3 projects/eeg-eye-state/src/analyze.py</code> writes <code>results/metrics.json</code>, and <code>python3 website/build_results.py</code> turns it into these charts. See the <a href="{REPO}/blob/main/projects/eeg-eye-state/report.md">full report</a>. Data: Roesler, O. (2013). <i>EEG Eye State</i>. UCI Machine Learning Repository, doi:10.24432/C57G7J.</p></div>
        <div class="landing-fact landing-fact-not"><h2>What it does not show</h2><p>One person and one short recording cannot show how this works for other people. The label is eyes open or closed, not attention, alertness or any condition.</p></div>
      </div>
      {bridge('What chapter 3 tells us:', 'a sensor that is right on one stretch and wrong on the next is not something to build a tool on. So the apps ask the person instead of guessing.', 'tools.html', 'Chapter 4')}
      {nav(('mouse.html', 'Chapter 2 · Mouse'), ('tools.html', 'Chapter 4 · Design'))}
    </section>""")

# ---------------- tools ----------------
def shot(src, alt, cap, sub, width='100%'):
    return f'<li><img src="{src}" alt="{alt}" loading="lazy" style="width:{width};border:1px solid var(--line);border-radius:var(--radius-card)"><strong>{cap}</strong><span>{sub}</span></li>'


page("tools.html", "Design · From neurons to next steps",
     "Chapter 4: what the two studies found, the design rule each finding gives, and where that rule lives in Next Step and Helper Jobs.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'All chapters'), 'Chapter 4 · Design · Human–computer interaction', '<span id="page-title">From findings to features.</span>', 'Chapter 2 showed that a brain’s state changes what gets through. Chapter 3 showed that state is hard to read from outside. Each finding became a design rule, and each rule is a real feature in two apps people use.', 'tablets')}
      <section class="landing-problems" id="rules" aria-labelledby="rules-title">
        <h2 class="landing-subhead" id="rules-title">Four findings, four design rules</h2>
        <p class="lp-lead">Read each card top to bottom: what we found, the rule it gives, and where the rule lives.</p>
        <ol aria-label="Findings, rules and features" tabindex="0">
          <li><p class="lp-k">From chapter 2</p><h3>Show less when energy is low.</h3><p class="lp-pain"><b>Found:</b> the same picture lands differently depending on the brain’s state.</p><p class="lp-fix"><b>In the apps:</b> Next Step asks “How much energy do you have today?” On “A little”, it shows just the next step. Helper Jobs shows one picture step at a time, read aloud.</p></li>
          <li><p class="lp-k">From chapter 3</p><h3>Ask, don’t guess.</h3><p class="lp-pain"><b>Found:</b> a sensor read eye state on one stretch, then drifted to a coin flip.</p><p class="lp-fix"><b>In the apps:</b> the person tells the app how they are doing. The energy check is optional, Help is a button they press, and nothing happens until they tap.</p></li>
          <li><p class="lp-k">From chapter 3</p><h3>Expect change halfway through.</h3><p class="lp-pain"><b>Found:</b> within two minutes, the link between signal and state shifted.</p><p class="lp-fix"><b>In the apps:</b> Next Step has Save &amp; pause, a note of where you stopped, and “Pick up where you left off”. Helper Jobs reminds helpers to take breaks.</p></li>
          <li><p class="lp-k">From real life</p><h3>When stuck, make it smaller.</h3><p class="lp-pain"><b>Seen:</b> a task that is too big all at once is where people stop.</p><p class="lp-fix"><b>In the apps:</b> Next Step’s “I’m stuck” offers to make the step smaller, ask a question or take a break. Nothing is sent, and your place is kept.</p></li>
        </ol>
      </section>
      <h2 class="landing-subhead">The rules, on real screens</h2><p class="landing-demo-note">Screens from the working apps, with made-up examples.</p>
      <ol class="landing-demo" aria-label="App screens" tabindex="0">
        {shot('img/next-step-energy.jpg', 'Next Step asks how much energy you have today: a little, some or plenty. A little shows just the next step.', 'Show less when energy is low', 'The person picks their energy; the plan shrinks to one step.', '78%')}
        {shot('img/next-step-stuck.jpg', 'Next Step step screen with Save and pause, a note for where I paused, and I’m stuck options: make it smaller, ask a question, see how others began, take a break.', 'Pause, and make it smaller', 'Save &amp; pause keeps your place; “I’m stuck” shrinks the step.', '78%')}
        {shot('img/helper-jobs-phone.jpg', 'A Helper Jobs step with a real photo of the place, a few words and Read aloud.', 'One picture step, read aloud', 'A few words, a photo of the real place, and a Help button.', '62%')}
      </ol>
      <section class="landing-problems two" aria-labelledby="apps-title">
        <h2 class="landing-subhead" id="apps-title">Two apps, real-world help</h2>
        <p class="lp-lead">Both follow the same rules: one step on the screen, big type, a picture, read aloud, and only made-up people in the examples.</p>
        <ol aria-label="Two apps" tabindex="0">
          <li><p class="lp-k">By Amishi Mehta · for schoolwork</p><h3>Next Step</h3><p class="lp-pain">For young people who find long instructions, interruptions or explaining their needs hard. Made with neurodivergent students in mind.</p><p class="lp-fix"><b>What it does:</b> turns a long assignment into one next step, practises words for asking for help, and keeps a note of where to restart. <a href="{NEXT_STEP}">Open Next Step →</a></p></li>
          <li><p class="lp-k">Family project · for Pragnya outings</p><h3>Helper Jobs</h3><p class="lp-pain">Gives neurodivergent adults a real job at kids’ Sunday outings, with a volunteer always close by.</p><p class="lp-fix"><b>What it does:</b> picture steps read aloud in English, Hindi or Spanish, break reminders, and Help that reaches the lead’s phone in about a second. <a href="{HELPER_JOBS}">Open Helper Jobs →</a></p></li>
        </ol>
      </section>
      <div class="landing-facts">
        <div class="landing-fact"><h2>The loop on a phone</h2><p>The <a href="neuroscience-mobile/">phone tour</a> tells the same five chapters, one screen at a time, in the same design as the apps.</p></div>
        <div class="landing-fact landing-fact-not"><h2>Careful claims</h2><p>The studies suggest these rules; they do not prove the apps work. These are early test versions with made-up people in every example, not tested in a formal study, and they do not diagnose or treat anything.</p></div>
      </div>
      {bridge('Closing the loop:', 'do these designs actually help the people they are for? That is where the research goes next.', 'next.html', 'Chapter 5')}
      {nav(('eeg.html', 'Chapter 3 · EEG'), ('next.html', 'Chapter 5 · What’s next'))}
    </section>""")

# ---------------- next ----------------
EXPS = [
    ("flask", "1 · Planned · tests chapter 2", "Does the timing matter?", "Does behaviour from the same moment predict better than behaviour from a moment nearby? Needs the raw Sensorium recordings, which are not in this repository."),
    ("activity", "2 · Ready to run · tests chapter 3", "Brain-wave bands", "Alpha waves rise when eyes close. Do bands like alpha hold up over time better than raw signals? Uses the EEG file already here."),
    ("brain", "3 · Planned · tests chapter 2", "Which neurons care?", "Is the gain spread across all neurons, or held by groups chosen in advance by depth and position? Needs raw responses and neuron positions."),
    ("timeline", "4 · Started · tests chapter 3", "Why does it drift?", "How fast does the link between signal and eye state change, and does adjusting for drift help? Block-by-block scores and the glitch check are done."),
    ("users", "5 · Planned · closes the loop", "Do the apps help?", "Back to real life: do the four design rules make tasks easier to finish, for the people the apps are for? Needs consent, a task list written in advance and no personal data beyond what the test needs."),
]
ROADMAP = [
    ("Now · done", "Two studies, two apps.", "The mouse and EEG studies, every result checked and rerunnable. Next Step and Helper Jobs working, with the four design rules built in.", "<b>Shown:</b> on this site, in the slides and in the phone tour."),
    ("Next · with an ASDRP mentor", "Run the four data experiments.", "Brain-wave bands and drift in the EEG, using the data already here. Then timing and neuron groups in the full mouse recordings.", "<b>Aim:</b> a first paper, on why the EEG drifts, for a student research journal such as the <i>Journal of Emerging Investigators</i>, plus a poster."),
    ("Then · with people", "Study the design with the people it is for.", "Co-design sessions with Pragnya volunteers and families, then a usability test of the four design rules. Consent first, and tasks written down before anyone takes part.", "<b>Aim:</b> a second paper, on the design rules, and better apps."),
    ("Longer term · the joined-up question", "Does designing for state help people learn?", "Compare the energy-aware design with a fixed one, for the same person over several weeks. Then ask whether the brain findings predict who it helps most.", "<b>Aim:</b> one research direction, where neuroscience and human–computer interaction meet."),
]
OUTPUTS = [
    ("books", "Papers", "Write-ups others can check", "Every study ends in a paper with its code, data links and limits, aimed at student journals and science fairs."),
    ("presentation", "Posters and talks", "Said out loud", "The same slides and charts as this site, for symposiums and science fairs."),
    ("code", "Open tools", "Anyone can rerun it", "Every analysis reruns with one command, and the apps stay open source."),
    ("heart-handshake", "Better apps", "Back to real life", "Each design study changes the apps, and each change is tested again."),
    ("route-2", "A design guide", "Rules others can use", "A short, plain guide to designing for brain state, built only from findings that held up."),
    ("users", "Community", "Built with people, not for them", "Pragnya volunteers and families help decide what gets built and what gets tested."),
]
page("next.html", "Where this goes next · From neurons to next steps",
     "Chapter 5: the research plan. Four more data experiments, design studies with the people the apps are for, and papers others can check.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'All chapters'), 'Chapter 5 · Test, then go further', '<span id="page-title">Where this goes next.</span>', 'The loop does not stop at two studies and two apps. Each turn adds a study, a better design and a write-up others can check. Everything on this page is a plan, and it is labelled that way.', 'plan')}
      <section class="landing-problems" id="roadmap" aria-labelledby="road-title">
        <h2 class="landing-subhead" id="road-title">The road ahead</h2>
        <p class="lp-lead">Each step builds on the last: data first, then people, then the two together.</p>
        <ol aria-label="Research plan" tabindex="0">
          {''.join(f'<li><p class="lp-k">{k}</p><h3>{h}</h3><p class="lp-pain">{pn}</p><p class="lp-fix">{fx}</p></li>' for k, h, pn, fx in ROADMAP)}
        </ol>
      </section>
      <section class="landing-more" aria-labelledby="exp-title">
        <div class="lm-head"><div><h2 class="landing-subhead" id="exp-title">The next five experiments</h2><p class="lp-lead">One for each link in the loop, with the same steps as chapters 2 and 3.</p></div></div>
        {grid(EXPS)}
      </section>
      <section class="landing-more" aria-labelledby="out-title">
        <div class="lm-head"><div><h2 class="landing-subhead" id="out-title">What each turn of the loop produces</h2><p class="lp-lead">Not just results: things other people can read, check and use.</p></div></div>
        {grid(OUTPUTS)}
      </section>
      <p class="lp-energy"><b>The rule we keep:</b> a plan stays labelled as a plan until it has code, saved results, a rerun record, its limits written down and a page like the two studies. <span>No paper, poster or result is listed as done before it is.</span></p>
      {nav(('tools.html', 'Chapter 4 · Design'), ('index.html', 'Back to the start'))}
    </section>""")

# ---------------- old addresses keep working ----------------
REDIRECTS = {
    "mouse-visual-cortex.html": "mouse.html", "mouse-leave-one-out.html": "mouse.html#checks",
    "eeg-eye-state.html": "eeg.html", "eeg-label-shuffle-control.html": "eeg.html#checks", "eeg-purge-gap.html": "eeg.html#checks",
    "reviewer-dashboard.html": "index.html", "reviewer-packet.html": "index.html",
}
for old, new in REDIRECTS.items():
    (W / old).write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Moved</title><meta http-equiv="refresh" content="0; url={new}"><link rel="canonical" href="{new}"></head><body><p>This page moved: <a href="{new}">{new}</a>.</p></body></html>\n')
print("built index, mouse, eeg, tools, next ·", len(REDIRECTS), "redirects")
