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
SITE = "https://mehtama1234.github.io/ASDRP-Neuroscience-Portfolio/"


def ic(name):
    return f'<span class="lm-icon" data-icon="{name}"></span>'


def page(name, title, description, body, base="", extra_js="", manifest=""):
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#F3ECE1" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  {manifest}<link rel="icon" href="{base}assets/icon.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="{base}assets/base.css" />
  <link rel="stylesheet" href="{base}assets/experience.css" />
  <link rel="stylesheet" href="{base}assets/theme-atlas.css" />
  <link rel="stylesheet" href="{base}assets/styles.css" />
  <link rel="stylesheet" href="{base}assets/charts.css" />
</head>
<body>
  <aside class="public-demo-banner" aria-label="About this portfolio">ASDRP application portfolio · Public data only · Every number comes from committed results</aside>
  <a class="skip-link" href="#app">Skip to the page</a>
  <header>
    <a class="brand" href="{base}index.html"><span class="mark" aria-hidden="true">n.</span> From neurons to next steps</a>
    <span class="header-status"><span class="badge">Public data only</span><span class="badge">Plans marked as plans</span></span>
    <a class="header-link" href="{REPO}">Source code</a>
  </header>
  <main id="app" tabindex="-1">
{body}
    <nav class="landing-note family-links" aria-label="Everything in this portfolio"><b>Everything in this portfolio:</b><a href="{SITE}">The website</a><a href="{SITE}neuroscience-mobile/">Phone tour</a><a href="{SITE}presentation/">Slides</a><a href="{SITE}video/">Video</a><a href="{NEXT_STEP}">Next Step app</a><a href="{HELPER_JOBS}">Helper Jobs app</a><a href="{REPO}">Source code</a></nav>
  </main>
  <script src="{base}assets/icons.js"></script><script src="{base}assets/icons-extra.js"></script><script src="{base}assets/art.js"></script><script src="{base}assets/science-art.js"></script>
  <script src="{base}assets/results.js"></script><script src="{base}assets/charts.js"></script><script src="{base}assets/site.js"></script>{extra_js}
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
     "From neurons to next steps: a question from real life, tested in a mouse’s brain and a person’s brain waves, then turned into two apps that help.", f"""    <section id="home" class="screen active landing" aria-labelledby="home-title">
      <div class="landing-hero">
        <div class="landing-hero-text">
          <p class="landing-kicker">An ASDRP neuroscience portfolio · Amishi Mehta</p>
          <h1 id="home-title">From neurons to next steps</h1>
          <p class="landing-lede">At Pragnya’s outings for neurodivergent kids and adults, and in everyday schoolwork, the same instruction can land one moment and be lost the next. That raised a question: <b>does what a brain is doing change what it takes in?</b> We tested it in two public brain recordings, tried hard to break each answer, and turned what held up into the design of two apps.</p>
          <div class="landing-actions">
            <a class="button primary" href="#story">Read the story <span aria-hidden="true">→</span></a>
            <a class="button secondary" href="mouse.html">Start with the mouse study</a>
          </div>
          <p class="landing-try-note">The same story as <a href="presentation/">slides</a>, a <a href="video/">narrated video</a> and a <a href="neuroscience-mobile/">phone tour</a>. Public data only. A prediction is not a cause.</p>
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
        <div class="loop-figure"><div class="loop-wide" data-art="loop"></div><div class="loop-tall" data-art="loopTall"></div></div>
        <ol aria-label="Five chapters" tabindex="0">
          <li><p class="lp-k">1 · Real life</p><h3>Same words, different moment.</h3><p class="lp-pain">At Pragnya’s outings and in schoolwork, a step that is easy when someone is calm can be lost when they are tired, rushed or overloaded. Is that the brain itself?</p><p class="lp-fix"><b>To find out:</b> look inside a brain while its state changes.</p></li>
          <li><p class="lp-k">2 · Understand</p><h3>A mouse’s state changes how its brain sees.</h3><p class="lp-pain">Mice watched pictures while thousands of brain cells were recorded. We guessed what each cell would do from the picture alone, then from the picture plus how alert and active the mouse was.</p><p class="lp-fix"><b>Found:</b> knowing the mouse’s state made our guesses 25–33% better, in all three mice. <a href="mouse.html">Read chapter 2 →</a></p></li>
          <li><p class="lp-k">3 · Measure</p><h3>Can sensors read state in a person?</h3><p class="lp-pain">A cap of 14 sensors on one person’s head for two minutes (EEG). Closing your eyes is one of the clearest changes it picks up. Can a simple model tell when?</p><p class="lp-fix"><b>Found:</b> on one stretch, often (0.625, where 0.5 is a coin flip). Across the whole recording it drifted to 0.478, no better than guessing. <a href="eeg.html">Read chapter 3 →</a></p></li>
          <li><p class="lp-k">4 · Design</p><h3>From findings to features.</h3><p class="lp-pain">If state matters but cannot be read from outside, an app should ask, not guess. It should show less on a low-energy day, and make pausing and coming back easy.</p><p class="lp-fix"><b>Built into:</b> Next Step, by Amishi Mehta, for schoolwork, and Helper Jobs, a family project, for real jobs at Pragnya outings. <a href="tools.html">Read chapter 4 →</a></p></li>
          <li><p class="lp-k">5 · Test, then go further</p><h3>Where this goes next.</h3><p class="lp-pain">Four more data experiments, design studies with Pragnya volunteers and families, and papers others can check.</p><p class="lp-fix"><b>The aim:</b> one research direction, where neuroscience and design meet. <a href="next.html">Read chapter 5 →</a></p></li>
        </ol>
        <p class="lp-energy"><b>The loop:</b> real life raised the question; the mouse showed that state changes what a brain takes in; the EEG showed that state is hard to read from outside; so the apps ask how someone is doing and keep each step small. The last experiment takes the apps back to real life to see if they help. <span>Three mice and one person are a start, not a rule for everyone.</span></p>
        <div class="lp-how"><p class="lp-how-short"><b>What this does not show yet:</b> whether the pattern holds in more animals and more people, what causes it, or whether the apps help. Each of those is an experiment in chapter 5.</p></div>
      </section>

      <section class="landing-more" id="checks" aria-labelledby="landing-more-title">
        <div class="lm-head"><div><h2 class="landing-subhead" id="landing-more-title">How we tried to break each result</h2><p class="lp-lead">Nothing in the story counts until it has survived a check that could have made it disappear.</p></div><div class="hj-art" data-art="controls"></div></div>
        {grid([
            ('arrows-shuffle', 'Mix up the answers', 'It should fail, and it does', 'If we scramble which moments were eyes-closed, the model drops to a coin flip. If we scramble the mouse’s behaviour, the gain disappears. So the results come from real signal.'),
            ('timeline', 'Never peek at the future', 'Learn from earlier, test on later', 'The model only ever learns from the past and is tested on what comes after, the way a real app would have to work.'),
            ('route-2', 'Leave a gap', 'No help from next-door moments', 'Moments right next to each other look alike. We leave a gap between what the model learns from and what it is tested on.'),
            ('users', 'Leave one mouse out', 'No single mouse carries it', 'Take any one mouse away and the other two still show the gain.'),
            ('filter', 'Look for broken readings', 'Four found and capped', 'Four readings were hundreds of times too big. Capping them helps one test, but does not fix the drift.'),
            ('code', 'Every number traced', 'Rebuilt from saved results', 'Every chart is drawn from the saved results files, and the EEG study reruns with one command.'),
        ])}
      </section>

      <h2 class="landing-subhead">The story in three numbers</h2><p class="landing-demo-note">One from inside a brain, two from outside. Each chapter has the charts and the checks.</p>
      <ol class="landing-demo" aria-label="Three results" tabindex="0">
        {phone('Mouse study', 'THREE MICE', 'State helps', '<div class="ph-paused"><b>25–33% better</b><em>in every mouse</em></div><p class="ph-small">Once we know if the mouse is alert and running.</p>', 'State matters inside', 'Knowing the mouse’s state made its brain a quarter to a third easier to predict.')}
        {phone('EEG study', 'LAST STRETCH', '0.625 → 0.728', '<p class="ph-note">With 4 broken readings capped</p><p class="ph-small">0.5 is a coin flip. 1.0 is always right.</p>', 'Readable once…', 'On the last stretch, a simple model could often tell eyes open from closed.')}
        {phone('EEG study', 'FIVE STRETCHES', 'About a coin flip', '<div class="ph-paused ph-red"><b>Average 0.478</b><em>some stretches worse than guessing</em></div><p class="ph-small">So the apps ask instead of guess.</p>', '…but not over time', 'Within two minutes, the brain-wave pattern for eyes closed changed.')}
      </ol>

      <div class="landing-facts">
        <div class="landing-fact"><h2>Who did what</h2><p>The studies were done by the applicant with a parent collaborator, who helped scope questions, review code and debug. Software tools, including AI assistants, helped build this website and the apps. The <a href="{REPO}/blob/main/application/contribution-ledger.md">contribution ledger</a> lists each part.</p></div>
        <div class="landing-fact landing-fact-not"><h2>What it is not</h2><p>It is not a medical study and it does not diagnose anyone. Three mice and one person cannot speak for everyone, and being able to predict something is not the same as knowing what causes it.</p></div>
      </div>
      <p class="landing-note">Data: Sensorium 2022 (Willeke et al., 2022) and UCI EEG Eye State (Roesler, 2013). <a href="mouse.html">Mouse study</a><a href="eeg.html">EEG study</a><a href="tools.html">Tools</a><a href="next.html">Next experiments</a></p>
    </section>""")

# ---------------- mouse ----------------
page("mouse.html", "Understand · mouse study · From neurons to next steps",
     "Chapter 2: knowing how alert and active a mouse was made its brain’s response to pictures 25–33% easier to predict, in all three mice.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'All chapters'), 'Chapter 2 · Understand · Mouse study', '<span id="page-title">Does a mouse’s state change how its brain responds to what it sees?</span>', 'Mice watched pictures while scientists recorded thousands of brain cells in the part of the brain that handles seeing. We tried to guess what each cell would do, first from the picture alone, then from the picture plus two signs of the mouse’s state: how wide its pupils were and how fast it was running. If state did not matter, the extra signs would not help.', 'mouseHero')}
      <section class="landing-problems answer"><p class="lp-energy"><b>It mattered, in all three mice.</b> Knowing the mouse’s state made our guesses a quarter to a third better (25–33%), on pictures the model had never seen. <span>This shows state and seeing are linked. It does not yet show which causes which.</span></p></section>

      <section class="landing-more" aria-labelledby="how-title">
        <div class="lm-head"><div><h2 class="landing-subhead" id="how-title">How we tested it</h2><p class="lp-lead">Two guessers, the same pictures, and a fair test on pictures neither had seen.</p></div><div class="hj-art" data-art="mouseStudy"></div></div>
        {grid([
            ('photo', 'Step 1', 'What the mouse saw', 'Each picture is shrunk to a short summary of its light and dark patterns, so a simple model can use it.'),
            ('eye', 'Step 2', 'What state it was in', 'Pupil size (wider usually means more alert) and running speed, recorded at the same moment as the brain cells.'),
            ('chart-dots', 'Step 3', 'Two simple guessers', 'Guesser A sees only the picture. Guesser B sees the picture plus pupil and running. Both are the simplest kind of model: a weighted sum.'),
            ('target', 'Step 4', 'A fair test', 'Both guess how each brain cell responds to pictures they have never seen. We score how closely each guess follows the real cell.'),
            ('books', 'The data', 'A public dataset', 'Sensorium 2022: recordings of thousands of brain cells from mice watching pictures, shared by scientists for anyone to study.'),
            ('users', 'Being fair', 'Each mouse counts once', 'The many brain cells in one mouse are not counted as many mice.'),
        ])}
      </section>

      <h2 class="landing-subhead">The results</h2>
      {chart('mouse-scale', 'How to read the score', 'How closely the guess follows the real brain cell.', '0 means the guess and the cell have nothing in common; 1 would be a perfect match. Brain cells are noisy, so even good guesses score low. What matters is the jump from A to B.', 'The score is a correlation, averaged over every recorded brain cell.')}
      {chart('mouse-scores', 'Result', 'Every mouse is easier to predict once we know its state.', 'The picture explains part of what the seeing part of the brain does. Whether the mouse is alert and moving explains more, in every animal.', 'Tested on pictures the guessers never saw.')}
      {chart('mouse-gain', 'How much state adds', 'Every mouse gains, by different amounts.', 'Pupil size helps all three mice. How much running adds changes from mouse to mouse, so each mouse is shown on its own.', 'Gain = guesser B’s score minus guesser A’s score.')}

      <section class="landing-more" aria-labelledby="checks-title" id="checks">
        <div class="lm-head"><div><h2 class="landing-subhead" id="checks-title">Trying to break the result</h2><p class="lp-lead">Three checks that could have made the gain disappear. It survived all three.</p></div><div class="hj-art" data-art="controls"></div></div>
        {grid([
            ('arrows-shuffle', 'Mix up the state', 'The gain disappears', 'We gave guesser B the pupil and running from the wrong moments, 20 times per mouse. It added nothing. The gain needs the mouse’s state at that moment.'),
            ('users', 'Leave one mouse out', 'Still there', 'Take any one mouse away and the other two still show the gain, so no single mouse carries the result.'),
            ('eye', 'Pupil or running?', 'Pupil helps every mouse', 'Taking each sign away in turn: pupil helps all three mice; running helps some more than others.'),
        ])}
      </section>
      {chart('mouse-loo', 'Leave one mouse out', 'The gain stays without any one mouse.', 'So the pattern does not hang on one recording. It is a check, not a promise about all mice.', 'Average gain over the two mice that are left.')}

      <div class="landing-facts" style="margin-top:28px">
        <div class="landing-fact"><h2>Code and data</h2><p>The analysis is in <a href="{FLAGSHIP}">AmishI123/neuroscience-project</a> (notebooks 01–05 and <code>src/summarize_replication.py</code>). The numbers here are copied from its committed summary into <code>website/build_results.py</code>. Data: Willeke et al. (2022), <i>The Sensorium competition on predicting large-scale mouse primary visual cortex activity</i>, arXiv:2206.08666.</p></div>
        <div class="landing-fact landing-fact-not"><h2>What it does not show</h2><p>Three mice cannot speak for all mice. A better guess does not show that being alert or running causes the brain to change. Other things that happen at the same time could explain it.</p></div>
      </div>
      {bridge('What chapter 2 tells us:', 'the same picture lands differently depending on the state the mouse is in. So the next question is whether that state can be read from outside the head, in a person.', 'eeg.html', 'Chapter 3')}
      {nav(('index.html', 'All chapters'), ('eeg.html', 'Chapter 3 · EEG'))}
    </section>""")

# ---------------- EEG ----------------
page("eeg.html", "Measure · EEG study · From neurons to next steps",
     "Chapter 3: a simple model reads eye state from one person’s EEG on one stretch of time, but not reliably across the recording, because the signal drifts.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'All chapters'), 'Chapter 3 · Measure · EEG study', '<span id="page-title">Can sensors on the head tell when someone’s eyes are closed?</span>', 'EEG is a cap of small sensors that pick up the brain’s electrical activity through the scalp. Closing your eyes is one of the clearest changes it can see. If a simple model cannot read even that reliably for two minutes, quieter states like tiredness will be harder still.', 'eegHero')}
      <section class="landing-problems answer"><p class="lp-energy"><b>On one stretch, yes. Over time, no.</b> On the last part of the recording the model scored 0.625, and 0.728 once four broken readings were capped. But tested on five stretches across the recording, it averaged 0.478: about a coin flip. <span>Letting it see the last few moments as well did not help.</span></p></section>

      <section class="landing-more" aria-labelledby="how-title">
        <div class="lm-head"><div><h2 class="landing-subhead" id="how-title">How we tested it</h2><p class="lp-lead">Learn from earlier in the recording, then test on what comes later, like a real app would have to.</p></div><div class="hj-art" data-art="eegStudy"></div></div>
        {grid([
            ('activity', 'The recording', 'One person, two minutes', '14 sensors, about 128 readings a second. Each moment is marked eyes open or eyes closed (closed about 45% of the time).'),
            ('timeline', 'Learn, then test', 'Earlier, then later', 'The model learns from the first 70% of the recording, is tuned on the next 15%, and is tested once on the last 15%.'),
            ('chart-dots', 'Two models', 'Now, or now plus a moment ago', 'One sees a single moment. The other also sees the last 9 readings, about a fourteenth of a second.'),
            ('target', 'The score', '0.5 is a coin flip', 'How often the model ranks an eyes-closed moment above an eyes-open one. 0.5 is guessing, 1.0 is always right.'),
            ('route-2', 'Five stretches', 'Moving forward in time', 'Learn from everything before a stretch, test on that stretch, and repeat five times across the recording.'),
            ('books', 'The data', 'A public recording', 'UCI EEG Eye State (Roesler, 2013), shared for anyone to study.'),
        ])}
      </section>

      <h2 class="landing-subhead">The results</h2>
      {chart('eeg-scale', 'How to read the score', 'Where the results sit between guessing and always right.', 'Anything near 0.5 is no better than flipping a coin. Below 0.5 means the model is wrong more often than right, so the pattern it learned has flipped.', 'The score is called AUC.')}
      {chart('eeg-holdout', 'The last stretch', 'Good on one stretch, better once broken readings are capped.', 'Four readings were broken: up to 715,897 when normal is about 4,000. Capping each sensor at the range seen while learning lifts the score from 0.625 to 0.728.', 'We added this check after the first results, so the new numbers sit next to the old ones, not in place of them.')}
      {chart('eeg-folds', 'Five stretches in time', 'Across the recording, it drifts to a coin flip.', 'Scores land on both sides of 0.5, and some fall well below it. Being worse than guessing means the pattern the model learned earlier had flipped by later on.', 'So the signal drifts within two minutes. Capping broken readings and leaving a gap do not fix it.')}

      <section class="landing-more" aria-labelledby="checks-title" id="checks">
        <div class="lm-head"><div><h2 class="landing-subhead" id="checks-title">Making sure it is not our mistake</h2><p class="lp-lead">Three checks that the result comes from the recording, not from how we handled it.</p></div><div class="hj-art" data-art="controls"></div></div>
        {grid([
            ('arrows-shuffle', 'Mix up the answers', 'Scores 0.499, a coin flip', 'With eyes open and closed scrambled 20 times, the model scores a coin flip, as it should. Our method does not invent a pattern.'),
            ('route-2', 'Leave a gap', 'Scores 0.448, still near guessing', 'We left out the moments just before each test stretch, so the model could not lean on near-copies. The result stays near a coin flip.'),
            ('filter', 'Cap broken readings', 'Four readings, capped fairly', 'The caps come only from the part the model learns from, so the test part never shapes them.'),
        ])}
      </section>
      {chart('eeg-windows', 'How far back to look', 'Looking further back seems to help, but we did not pick a winner.', 'We chose to try 3, 9, 30 and 90 readings back before seeing any results. Ninety does best on average, but picking it now would mean tuning to this one recording.', 'Next: compare these on new recordings before choosing.')}

      <div class="landing-facts" style="margin-top:28px">
        <div class="landing-fact"><h2>Rerun it</h2><p><code>python3 projects/eeg-eye-state/src/analyze.py</code> writes <code>results/metrics.json</code>, and <code>python3 website/build_results.py</code> turns it into these charts. See the <a href="{REPO}/blob/main/projects/eeg-eye-state/report.md">full report</a>. Data: Roesler, O. (2013). <i>EEG Eye State</i>. UCI Machine Learning Repository, doi:10.24432/C57G7J.</p></div>
        <div class="landing-fact landing-fact-not"><h2>What it does not show</h2><p>One person and one short recording cannot show how this works for other people. The only thing measured is eyes open or closed, not attention, tiredness or any condition.</p></div>
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
    ("flask", "1 · Planned · tests chapter 2", "Does the timing matter?", "Does the mouse’s state at that exact moment help more than its state a little earlier or later? Needs the full mouse recordings."),
    ("activity", "2 · Ready to run · tests chapter 3", "Brain-wave bands", "One kind of brain wave, called alpha, grows when eyes close. Does tracking it hold up over time better than the raw readings? Uses the recording we already have."),
    ("brain", "3 · Planned · tests chapter 2", "Which brain cells change?", "Does state change every brain cell a little, or a few groups a lot? Groups are chosen before looking. Needs the full mouse recordings."),
    ("timeline", "4 · Started · tests chapter 3", "Why does it drift?", "How quickly does the eyes-closed pattern change, and can the model keep up if it keeps learning? The stretch-by-stretch scores and the broken-reading check are done."),
    ("users", "5 · Planned · closes the loop", "Do the apps help?", "Back to real life: do the four design rules make tasks easier to finish, for the people the apps are for? Needs consent, a task list written in advance and no personal data beyond what the test needs."),
]
ROADMAP = [
    ("Now · done", "Two studies, two apps.", "The mouse and EEG studies, every result checked and rerunnable. Next Step and Helper Jobs working, with the four design rules built in.", "<b>Shown:</b> on this site, in the slides and in the phone tour."),
    ("Next · with an ASDRP mentor", "Run the four data experiments.", "Brain-wave bands and drift in the EEG, using the data already here. Then timing and groups of brain cells in the full mouse recordings.", "<b>Aim:</b> a first paper, on why the EEG drifts, for a student research journal such as the <i>Journal of Emerging Investigators</i>, plus a poster."),
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

# ---------------- the phone tour: the same five chapters, one screen at a time ----------------
TOUR = [
    ("home", "Start", "home", "The loop", "From neurons to next steps", "At Pragnya’s outings and in schoolwork, the same instruction can land one moment and be lost the next. Does what a brain is doing change what it takes in? Five short screens follow that question from real life, into the lab, and back out again.",
     '<div class="loop-figure"><div data-art="loopTall"></div></div>', "", "index.html"),
    ("ch1", "Real life", "users", "Chapter 1 of 5 · Real life", "Same words, different moment.", "A step that is easy when someone is calm can be lost when they are tired, rushed or overloaded. Is that the brain itself? To find out, look inside a brain while its state changes.",
     '<div class="hj-art" data-art="note"></div>', "", "index.html#story"),
    ("ch2", "Understand", "eye", "Chapter 2 of 5 · Understand", "A mouse’s state changes how its brain sees.", "Mice watched pictures while thousands of brain cells were recorded. Guesser A saw only the picture. Guesser B also knew how alert and active the mouse was.",
     '<div class="hj-art" data-art="mouseStudy"></div>', '<b>Found:</b> knowing the mouse’s state made guesses 25–33% better, in all three mice.<div class="tour-nums"><p><b>25–33%</b><span>better guesses once state is known</span></p><p><b>3 of 3</b><span>mice show the gain</span></p></div>', "mouse.html"),
    ("ch3", "Measure", "activity", "Chapter 3 of 5 · Measure", "Can sensors read state in a person?", "A cap of 14 sensors on one person’s head for two minutes (EEG). Can a simple model tell when their eyes are closed?",
     '<div class="hj-art" data-art="eegStudy"></div>', '<b>Found:</b> on one stretch, often. Across the recording it drifted to no better than guessing.<div class="tour-nums"><p><b>0.625</b><span>on one stretch (0.5 is a coin flip)</span></p><p><b>0.478</b><span>across the recording: guessing</span></p></div>', "eeg.html"),
    ("ch4", "Design", "heart-handshake", "Chapter 4 of 5 · Design", "From findings to features.", "State matters, but it cannot be read from outside. So the apps ask, not guess. They show less on a low-energy day, and make pausing and coming back easy.",
     '<img src="{img}next-step-energy.jpg" alt="Next Step asks how much energy you have today: a little, some or plenty." style="width:100%;border:1px solid var(--line);border-radius:var(--radius-card)">', '<b>Built into:</b> Next Step, by Amishi Mehta, for schoolwork, and Helper Jobs, a family project, for real jobs at Pragnya outings.', "tools.html"),
    ("ch5", "Future", "flask", "Chapter 5 of 5 · Test, then go further", "Where this goes next.", "Four more data experiments, design studies with Pragnya volunteers and families, and papers others can check. Everything here is a plan, and labelled that way.",
     '<div class="hj-art" data-art="plan"></div>', '<b>The aim:</b> one research direction, where neuroscience and design meet.', "next.html"),
]
TOUR_JS = """<script>
(function(){
  var ids = %s, screens = document.querySelectorAll('[data-screen]'), tabs = document.querySelectorAll('[data-go]');
  function show(id){ if (ids.indexOf(id) < 0) id = 'home';
    screens.forEach(function(s){ s.hidden = s.dataset.screen !== id; });
    document.querySelectorAll('.experience-nav [data-go]').forEach(function(b){ if (b.dataset.go === id) b.setAttribute('aria-current', 'page'); else b.removeAttribute('aria-current'); });
    if (location.hash.slice(1) !== id) history.replaceState(null, '', '#' + id); window.scrollTo(0, 0); }
  tabs.forEach(function(b){ b.addEventListener('click', function(){ show(b.dataset.go); }); });
  window.addEventListener('hashchange', function(){ show(location.hash.slice(1)); });
  show(location.hash.slice(1));
})();
</script>""" % str([t[0] for t in TOUR]).replace("'", '"')


def tour(out, base, img):
    screens = []
    for i, (sid, tab, icon, eyebrow, title, sub, art, found, full) in enumerate(TOUR):
        nxt = TOUR[i + 1] if i + 1 < len(TOUR) else TOUR[0]
        go = f'<button class="button primary" type="button" data-go="{nxt[0]}">{"Start" if sid == "home" else ("Back to the start" if nxt[0] == "home" else "Next: " + nxt[1])} <span aria-hidden="true">→</span></button>'
        screens.append(f"""    <section class="screen active landing tour" data-screen="{sid}" aria-labelledby="t-{sid}"{' hidden' if i else ''}>
      <div class="hj-heading"><p class="eyebrow">{eyebrow}</p><h1 id="t-{sid}">{title}</h1><p class="hj-sub">{sub}</p></div>
      {art.replace('{img}', img)}
      {f'<section class="landing-problems answer"><p class="lp-energy">{found}</p></section>' if found and 'tour-nums' not in found else ''}
      {f'<section class="landing-problems answer"><p class="lp-energy">{found.split("<div")[0]}</p></section><div' + found.split("<div", 1)[1] if 'tour-nums' in found else ''}
      <div class="landing-actions">{go}<a class="button secondary" href="{SITE}{full}">{"Open the full site" if sid == "home" else "Read the full chapter"}</a></div>{'<p class="landing-try-note"><a href="download.html">Get it as an Android app</a> · or add this page to your home screen</p>' if sid == "home" else ''}
    </section>""")
    nav = '<nav class="experience-nav tour-nav" aria-label="Chapters">' + ''.join(f'<button type="button" data-go="{t[0]}"><span data-icon="{t[2]}" aria-hidden="true"></span>{t[1]}</button>' for t in TOUR if t[0] != 'ch1') + '</nav>'
    page(out, "Phone tour · From neurons to next steps", "The five chapters of From neurons to next steps, one phone screen at a time.",
         "\n".join(screens) + "\n    " + nav, base=base, extra_js=TOUR_JS,
         manifest='<link rel="manifest" href="manifest.webmanifest" />\n  ')


tour("neuroscience-mobile/index.html", "../", "../img/")


def download(out, base, apk):
    page(out, "Android app · From neurons to next steps", "The phone tour as an Android app, built from the same pages as the website.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'Back to the phone tour'), 'The phone tour · Android', '<span id="page-title">The same five chapters, as an Android app.</span>', 'The app is built straight from the phone tour on this website, so the words, numbers and pictures are the same. It is a test build for reviewers, not a store release.', 'loopTall')}
      <div class="landing-actions"><a class="button primary" href="{apk}" download>Download the Android app <span aria-hidden="true">→</span></a><a class="button secondary" href="index.html">Use it in the browser instead</a></div>
      <section class="landing-more" aria-labelledby="dl-title">
        <h2 class="landing-subhead" id="dl-title">Before you install</h2>
        {grid([
            ('route-2', 'Step 1', 'Download the file', 'Tap the button above on an Android phone. The file ends in .apk.'),
            ('shield-check', 'Step 2', 'Allow this one install', 'Android asks before installing apps from outside the store. Say yes for this file only.'),
            ('code', 'Check it', 'Same file as the code', 'Every new tour is built by GitHub from the repository. Its fingerprint (SHA-256) is in <a href="{REPO}/blob/main/communication/projects/neuroscience-mobile/releases/SHA256.txt">SHA256.txt</a>.'),
        ])}
      </section>
      <div class="landing-facts"><div class="landing-fact landing-fact-not"><h2>What it is not</h2><p>It does not collect anything, does not need an account and does not diagnose anyone. It explains the research, one screen at a time.</p></div><div class="landing-fact"><h2>iPhone and iPad</h2><p>Open the <a href="index.html">phone tour</a> in Safari and choose Share, then Add to Home Screen. It works the same way.</p></div></div>
    </section>""", base=base)


download("neuroscience-mobile/download.html", "../", "../neuroscience-lab-debug.apk")
download("../communication/projects/neuroscience-mobile/download.html", "../../../website/", "releases/neuroscience-lab-debug.apk")
tour("../communication/projects/neuroscience-mobile/index.html", "../../../website/", "../../../website/img/")

# ---------------- the video ----------------
page("video/index.html", "Video · From neurons to next steps", "The five chapters of From neurons to next steps as a short narrated video, with captions.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('../index.html', 'All chapters'), 'The video', '<span id="page-title">The same story, in a few minutes.</span>', 'The slides with their speaker notes read aloud, and captions you can turn on. The words, numbers and drawings are the same as on the website.', 'loop')}
      <video controls preload="metadata" playsinline poster="../presentation/slides/01-cover.jpg" style="width:100%;height:auto;border:1px solid var(--line);border-radius:var(--radius-card);background:#000">
        <source src="from-neurons-to-next-steps.mp4" type="video/mp4">
        <track kind="captions" src="from-neurons-to-next-steps.vtt" srclang="en" label="English" default>
      </video>
      <div class="landing-actions" style="margin-top:18px"><a class="button secondary" href="from-neurons-to-next-steps.mp4" download>Download the video</a><a class="button secondary" href="from-neurons-to-next-steps.vtt" download>Download the captions</a><a class="button secondary" href="../presentation/">See the slides</a></div>
      <div class="landing-facts"><div class="landing-fact landing-fact-not"><h2>About the voice</h2><p>The narration is a computer voice reading the speaker notes, so anyone can rebuild the video from the repository.</p></div></div>
    </section>""", base="../")

# ---------------- old addresses keep working ----------------
REDIRECTS = {
    "mouse-visual-cortex.html": "mouse.html", "mouse-leave-one-out.html": "mouse.html#checks",
    "eeg-eye-state.html": "eeg.html", "eeg-label-shuffle-control.html": "eeg.html#checks", "eeg-purge-gap.html": "eeg.html#checks",
    "reviewer-dashboard.html": "index.html", "reviewer-packet.html": "index.html",
    "mouse-visual-cortex-slides.html": "presentation/", "eeg-eye-state-slides.html": "presentation/",
}
for old, new in REDIRECTS.items():
    (W / old).write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Moved</title><meta http-equiv="refresh" content="0; url={new}"><link rel="canonical" href="{new}"></head><body><p>This page moved: <a href="{new}">{new}</a>.</p></body></html>\n')
print("built index, mouse, eeg, tools, next ·", len(REDIRECTS), "redirects")
