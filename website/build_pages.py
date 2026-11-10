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
    <a class="brand" href="index.html"><span class="mark" aria-hidden="true">b.</span> Brain &amp; Behaviour</a>
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
          <g class="la-card" transform="translate(14 18) rotate(-2)"><rect width="196" height="104"/><rect class="la-top" width="196" height="5"/><text class="la-kick" x="14" y="26">1 · THE PUZZLE</text><text class="la-title" x="14" y="56">Does state matter?</text><text class="la-small" x="14" y="80">Same words, but they land</text><text class="la-small" x="14" y="94">one moment and not the next</text></g>
          <g class="la-card" transform="translate(234 66) rotate(2)"><rect width="192" height="104"/><text class="la-kick" x="14" y="24">2 · INSIDE A BRAIN</text><text class="la-title" x="14" y="52">Picture + behaviour</text><rect class="la-note" x="14" y="64" width="164" height="28"/><text class="la-k2" x="24" y="82">BETTER IN ALL 3 MICE</text></g>
          <g class="la-card la-ink" transform="translate(18 214) rotate(1.5)"><rect width="196" height="116"/><text class="la-kick" x="14" y="24">3 · FROM THE OUTSIDE</text><text class="la-title" x="14" y="52">Eyes closed?</text><text class="la-k2" x="14" y="74">5 BLOCKS IN TIME</text><text class="la-body" x="14" y="94">The signal drifts.</text></g>
          <g class="la-card" transform="translate(238 236) rotate(-2)"><rect width="190" height="132"/><text class="la-kick" x="14" y="24">4 · INTO DESIGN</text><circle cx="30" cy="54" r="14"/><path class="la-tick" d="M24.5 54l3.5 3.5 7-7"/><text class="la-title" x="52" y="60">One clear step</text><rect class="la-pill" x="14" y="88" width="72" height="22" rx="11"/><text class="la-pt" x="50" y="103" text-anchor="middle">Next Step</text><rect class="la-pill" x="92" y="88" width="82" height="22" rx="11"/><text class="la-pt" x="133" y="103" text-anchor="middle">Helper Jobs</text></g>
        </svg>"""

page("index.html", "Brain & Behaviour · an ASDRP neuroscience portfolio",
     "One question followed from a mouse’s visual cortex, to a person’s brain waves, to two apps: does what a brain is doing change what it takes in?", f"""    <section id="home" class="screen active landing" aria-labelledby="home-title">
      <div class="landing-hero">
        <div class="landing-hero-text">
          <p class="landing-kicker">A neuroscience portfolio in five chapters</p>
          <h1 id="home-title">Does what a brain is doing change what it takes in?</h1>
          <p class="landing-lede">The same instruction can land one moment and be lost the next. We wanted to know how much of that is the brain itself. So we asked two public brain recordings, tested every answer on data the model had never seen, tried hard to break it, and then built tools around what held up.</p>
          <div class="landing-actions">
            <a class="button primary" href="#story">Read the story <span aria-hidden="true">→</span></a>
            <a class="button secondary" href="mouse.html">Start with the mouse study</a>
          </div>
          <p class="landing-try-note">Public data only. A prediction is not a cause. Plans are marked as plans.</p>
          <ul class="landing-parts" aria-label="What makes it work">
            <li><a href="mouse.html"><span data-icon="eye"></span><b>Mouse visual cortex</b><small>State changes what it does</small></a></li>
            <li><a href="eeg.html"><span data-icon="activity"></span><b>EEG eye state</b><small>Readable once, then it drifts</small></a></li>
            <li><a href="#checks"><span data-icon="arrows-shuffle"></span><b>Every result checked</b><small>Each one tested to break it</small></a></li>
            <li><a href="tools.html"><span data-icon="heart-handshake"></span><b>Tools for people</b><small>One clear step, in any state</small></a></li>
          </ul>
          <p class="landing-voice"><a href="next.html"><span data-icon="flask"></span>Chapter 5: five experiments, one for each link in the story.</a></p>
        </div>
        {LANDING_ART}
      </div>

      <section class="landing-problems" id="story" aria-labelledby="landing-problems-title">
        <h2 class="landing-subhead" id="landing-problems-title">The story, one chapter at a time</h2>
        <p class="lp-lead">Each chapter answers the question the last one raised.</p>
        <ol aria-label="Five chapters" tabindex="0">
          <li><p class="lp-k">1 · The puzzle</p><h3>Same words, different moment.</h3><p class="lp-pain">A step that is easy when someone is calm can be lost when they are tired, rushed or overloaded. Is that the brain itself changing what it takes in?</p><p class="lp-fix"><b>To find out:</b> look inside a brain while its state changes.</p></li>
          <li><p class="lp-k">2 · Inside a brain</p><h3>A mouse’s state shapes what its visual cortex does.</h3><p class="lp-pain">Thousands of neurons, recorded while mice watched pictures. We predicted each neuron from the picture alone, then from the picture plus pupil size and running.</p><p class="lp-fix"><b>Found:</b> knowing the mouse’s state made prediction 25–34% better, in all three mice. <a href="mouse.html">Read chapter 2 →</a></p></li>
          <li><p class="lp-k">3 · From the outside</p><h3>Can a sensor read state in a person?</h3><p class="lp-pain">Eyes closed is one of the clearest changes in brain waves. One person, 14 scalp sensors, 117 seconds, and the model is always tested on what comes later.</p><p class="lp-fix"><b>Found:</b> on one stretch, yes (0.625, or 0.728 with four glitches limited). Across the recording it drifted to 0.478, about a coin flip. <a href="eeg.html">Read chapter 3 →</a></p></li>
          <li><p class="lp-k">4 · Into design</p><h3>Don’t guess someone’s state. Design for it.</h3><p class="lp-pain">A sensor that is right one minute and wrong the next is not something to build on. It is better to make every step work in any state.</p><p class="lp-fix"><b>Built:</b> Next Step, by Amishi Mehta, and Helper Jobs, a family project for Pragnya. Both give one clear step at a time and an easy way back in. <a href="tools.html">Read chapter 4 →</a></p></li>
          <li><p class="lp-k">5 · What comes next</p><h3>Five experiments, one for each link.</h3><p class="lp-pain">More of the mouse data, brain-wave bands, drift over time, and whether the apps really help the people they are for.</p><p class="lp-fix"><b>The rule:</b> a plan stays a plan until it has code, results and its limits written down. <a href="next.html">Read chapter 5 →</a></p></li>
        </ol>
        <p class="lp-energy"><b>The thread:</b> a brain’s state changes what it takes in; reading that state from outside is unreliable; so a good tool makes every step clear, whatever state someone is in. <span>Three mice and one person are a start, not a rule for everyone.</span></p>
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
page("mouse.html", "Mouse visual cortex · Brain & Behaviour",
     "Chapter 2: knowing a mouse’s pupil size and running speed made its visual cortex 25–34% easier to predict, in all three mice.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'All chapters'), 'Chapter 2 · Inside a brain · Mouse study', '<span id="page-title">Does a mouse’s state change what its visual cortex does?</span>', 'We predicted thousands of neurons from the picture a mouse saw, then again with its pupil size and running speed added. If state did not matter, the extra information would add nothing.', 'mouseHero')}
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
page("eeg.html", "EEG eye state · Brain & Behaviour",
     "Chapter 3: a simple model reads eye state from one person’s EEG on one stretch of time, but not reliably across the recording, because the signal drifts.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'All chapters'), 'Chapter 3 · From the outside · EEG study', '<span id="page-title">Can a sensor on the head tell when someone’s eyes are closed?</span>', 'Eyes closed is one of the clearest changes in brain waves. If a simple model cannot read it reliably over two minutes, quieter states like tiredness will be harder still.', 'eegHero')}
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
      {bridge('What chapter 3 tells us:', 'a sensor that is right on one stretch and wrong on the next is not something to build a tool on. So the tools do not try to guess.', 'tools.html', 'Chapter 4')}
      {nav(('mouse.html', 'Chapter 2 · Mouse'), ('tools.html', 'Chapter 4 · Tools'))}
    </section>""")

# ---------------- tools ----------------
page("tools.html", "Tools for people · Brain & Behaviour",
     "Chapter 4: rather than guess someone’s state, Next Step and Helper Jobs make every step work in any state.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'All chapters'), 'Chapter 4 · Into design · Tools', '<span id="page-title">Don’t guess someone’s state. Make every step work in any state.</span>', 'Chapter 2 showed that state changes what gets through. Chapter 3 showed that reading it from outside is unreliable. So these apps keep each step small, say it aloud, and make it easy to stop and come back. Nothing happens until the person taps.', 'tablets')}
      <section class="landing-problems two" aria-labelledby="apps-title">
        <h2 class="landing-subhead" id="apps-title">Two working apps</h2>
        <p class="lp-lead">Both follow the same rules: one step on the screen, big type, a picture, read aloud, and only made-up people in the examples.</p>
        <ol aria-label="Two apps" tabindex="0">
          <li><p class="lp-k">By Amishi Mehta</p><h3>Next Step</h3><p class="lp-pain">For anyone who finds long instructions, interruptions or explaining their needs hard. Made with neurodivergent young people in mind.</p><p class="lp-fix"><b>What it does:</b> turns a long brief into one next step, practises words for asking for help, and keeps a note of where to restart. <a href="{NEXT_STEP}">Open Next Step →</a></p></li>
          <li><p class="lp-k">Family project for Pragnya</p><h3>Helper Jobs</h3><p class="lp-pain">Gives neurodivergent adults a real job at kids’ Sunday outings, with a volunteer always close by.</p><p class="lp-fix"><b>What it does:</b> picture steps read aloud in English, Hindi or Spanish, and Help that reaches the lead’s phone in about a second. <a href="{HELPER_JOBS}">Open Helper Jobs →</a></p></li>
        </ol>
      </section>
      <h2 class="landing-subhead">The apps</h2><p class="landing-demo-note">Real screens from both apps.</p>
      <ol class="landing-demo" aria-label="App screens" tabindex="0">
        <li><img src="img/next-step-wide.jpg" alt="Next Step home page: plan your work, say what you need, and connect safely." loading="lazy" style="width:100%;border:1px solid var(--line);border-radius:var(--radius-card)"><strong>Next Step</strong><span>Plan your work, say what you need, and connect safely.</span></li>
        <li><img src="img/helper-jobs-wide.jpg" alt="Helper Jobs home page: a real job at Sunday outings." loading="lazy" style="width:100%;border:1px solid var(--line);border-radius:var(--radius-card)"><strong>Helper Jobs</strong><span>Pick your picture, pick a job, one step at a time.</span></li>
        <li><img src="img/helper-jobs-phone.jpg" alt="A Helper Jobs step with a real photo of the place." loading="lazy" style="width:62%;border:1px solid var(--line);border-radius:var(--radius-card)"><strong>One picture step</strong><span>A few words, a picture of the real place, and Read aloud.</span></li>
      </ol>
      <div class="landing-facts">
        <div class="landing-fact"><h2>The story on a phone</h2><p>The <a href="neuroscience-mobile/">phone tour</a> tells the same five chapters, one screen at a time, in the same design as the apps.</p></div>
        <div class="landing-fact landing-fact-not"><h2>Careful claims</h2><p>These are early test versions with made-up people in every example. They have not been tested in a formal study, and they do not diagnose or treat anything. A usability study is planned as experiment 5.</p></div>
      </div>
      {bridge('What we still don’t know:', 'whether these designs actually help the people they are for. That is the last of the five experiments.', 'next.html', 'Chapter 5')}
      {nav(('eeg.html', 'Chapter 3 · EEG'), ('next.html', 'Chapter 5 · Next'))}
    </section>""")

# ---------------- next ----------------
EXPS = [
    ("flask", "1 · Planned · tests chapter 2", "Does the timing matter?", "Does behaviour from the same moment predict better than behaviour from a moment nearby? Needs the raw Sensorium recordings, which are not in this repository."),
    ("activity", "2 · Ready to run · tests chapter 3", "Brain-wave bands", "Alpha waves rise when eyes close. Do bands like alpha hold up over time better than raw signals? Uses the EEG file already here."),
    ("brain", "3 · Planned · tests chapter 2", "Which neurons care?", "Is the gain spread across all neurons, or held by groups chosen in advance by depth and position? Needs raw responses and neuron positions."),
    ("timeline", "4 · Started · tests chapter 3", "Why does it drift?", "How fast does the link between signal and eye state change, and does adjusting for drift help? Block-by-block scores and the glitch check are done."),
    ("users", "5 · Planned · tests chapter 4", "Do the apps help?", "Do one-step-at-a-time designs make tasks easier to finish? Needs consent, a task list written in advance and no personal data beyond what the test needs."),
]
page("next.html", "Next experiments · Brain & Behaviour",
     "Chapter 5: five experiments, each testing one link in the story, with the same steps as the two studies.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'All chapters'), 'Chapter 5 · What comes next', '<span id="page-title">Five experiments, one for each link in the story.</span>', 'Each one gets its analysis written down before it runs, a test on data kept aside, a check that could break it, and an honest write-up, just like chapters 2 and 3.', 'plan')}
      <section class="landing-more" aria-labelledby="exp-title">
        <h2 class="landing-subhead" id="exp-title">The five experiments</h2>
        {grid(EXPS)}
      </section>
      <p class="lp-energy"><b>The rule we keep:</b> a plan stays labelled as a plan until it has code, saved results, a rerun record, its limits written down and a page like the two studies.</p>
      {nav(('tools.html', 'Chapter 4 · Tools'), ('index.html', 'Back to the start'))}
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
