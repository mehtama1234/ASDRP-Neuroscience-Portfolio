"""Builds the slide deck for From neurons to next steps from the same words, charts and drawings as the
website. Each slide is a 1200x675 page in the website's own styles, shown at 1.6x (1920x1080).

Run: python3 website/presentation/build_deck.py
Writes presentation/src/*.html, slides/*.jpg, slides.html, present.html, presenter.html and the PDF."""
import html, json, sys
from pathlib import Path

P = Path(__file__).resolve().parent
W = P.parent
sys.path.insert(0, str(W)); sys.path.insert(0, str(P))
import build_pages as B  # noqa: E402  (rebuilding the pages first keeps the deck and site in step)
import viewers  # noqa: E402

PDF = "from-neurons-to-next-steps-slides.pdf"
SLIDES = []


def slide(key, alt, body, notes, cls=""):
    SLIDES.append({"key": key, "alt": alt, "body": body, "notes": notes, "cls": cls})


def head(eyebrow, title, sub="", art=""):
    a = f'<div class="hj-art" data-art="{art}"></div>' if art else ""
    s = f'<p class="hj-sub">{sub}</p>' if sub else ""
    return f'<div class="lm-head"><div class="hj-heading"><p class="eyebrow">{eyebrow}</p><h1>{title}</h1>{s}</div>{a}</div>'


def answer(text):
    return f'<section class="landing-problems answer"><p class="lp-energy">{text}</p></section>'


def cards(items, cls=""):
    return f'<section class="landing-problems {cls}"><ol>' + "".join(f'<li><p class="lp-k">{k}</p><h3>{h}</h3><p class="lp-pain">{a}</p>{f"<p class=lp-fix>{b}</p>" if b else ""}</li>' for k, h, a, b in items) + '</ol></section>'


# 1 -------------------------------------------------------------------------------------------
slide("cover", "From neurons to next steps: an ASDRP neuroscience portfolio by Amishi Mehta, with the four-card collage.", f"""
<div class="landing-hero"><div class="landing-hero-text">
<p class="landing-kicker">An ASDRP neuroscience portfolio · Amishi Mehta</p>
<h1>From neurons to next steps</h1>
<p class="landing-lede">The same instruction can land one moment and be lost the next. <b>Does what a brain is doing change what it takes in?</b> And if it does, how should we design for it?</p>
<p class="landing-try-note">Public data only. A prediction is not a cause. Plans are marked as plans.</p>
</div>{B.LANDING_ART}</div>""",
      "This is one question, followed from real life into the lab and back out again. I’ll show two studies with public brain recordings, then the two apps their findings shaped, and where the work goes next.")
# 2
slide("loop", "The loop: real life, understand, measure, design, test, and back to real life.", f"""
{head('The whole story on one page', 'One loop, five chapters.', 'It starts in real life and ends back there. Each chapter answers the question the last one raised.')}
<div class="loop-figure"><div class="loop-wide" data-art="loop"></div></div>""",
      "Here is the whole talk. Real life raised a question. A mouse study helps us understand it. An EEG study asks whether we can measure it in a person. The answers shape the design of two apps. And the last step tests the apps back in real life.")
# 3
slide("ch1", "Chapter 1, real life: same words, different moment.", f"""
{head('Chapter 1 · Real life', 'Same words, different moment.', 'At Pragnya’s outings for neurodivergent kids and adults, and in everyday schoolwork, a step that is easy when someone is calm can be lost when they are tired, rushed or overloaded.', 'note')}
{answer('<b>The question:</b> is that the brain itself changing what it takes in? <span>To find out, look inside a brain while its state changes.</span>')}""",
      "This is where it started. The same instruction works one moment and is lost the next. That made us ask whether the brain’s state itself changes what gets in.")
# 4
slide("ch2-how", "Chapter 2: how the mouse study works, in four steps.", f"""
{head('Chapter 2 · Understand · Mouse study', 'Does a mouse’s state change how its brain sees?', 'Mice watched pictures while thousands of brain cells were recorded in the part of the brain that handles seeing.', 'mouseStudy')}
{B.grid([
    ('photo', 'Step 1', 'What the mouse saw', 'Each picture shrunk to a short summary of its light and dark patterns.'),
    ('eye', 'Step 2', 'What state it was in', 'Pupil size (wider usually means more alert) and running speed.'),
    ('chart-dots', 'Step 3', 'Two simple guessers', 'A sees only the picture. B sees the picture plus pupil and running.'),
])}""",
      "Scientists shared recordings of thousands of brain cells from mice watching pictures. We built two simple guessers. Guesser A only knows the picture. Guesser B also knows how wide the pupils were and how fast the mouse was running. Both are tested on pictures they have never seen.")
# 5
slide("ch2-result", "Chapter 2 result: guesser B beats guesser A in all three mice.", f"""
{head('Chapter 2 · The result', 'Every mouse is easier to predict once we know its state.')}
{answer('<b>A quarter to a third better (25–34%), in all three mice,</b> on pictures the model had never seen. <span>This shows state and seeing are linked. It does not yet show which causes which.</span>')}
{B.chart('mouse-scores', 'Score on unseen pictures', 'Guesser A against guesser B.', '0 means no match, 1 would be perfect. Brain cells are noisy, so scores are low. What matters is the jump from A to B.', 'Average over every recorded brain cell.')}""",
      "In every mouse, guesser B wins. The scores look small because single brain cells are noisy, so the thing to look at is the jump from A to B: a quarter to a third better. That is a link, not proof of cause.")
# 6
slide("ch2-checks", "Chapter 2 checks: mix up the state, leave one mouse out, pupil or running.", f"""
{head('Chapter 2 · Trying to break it', 'Three checks that could have made the gain disappear.', 'It survived all three.', 'controls')}
{B.grid([
    ('arrows-shuffle', 'Mix up the state', 'The gain almost vanishes', 'Pupil and running from the wrong moments barely help. It needs the state at that moment.'),
    ('users', 'Leave one mouse out', 'Still there', 'Take any one mouse away and the other two still show the gain.'),
    ('eye', 'Pupil or running?', 'Pupil helps every mouse', 'Running helps some mice more than others.'),
])}
{B.bridge('What chapter 2 tells us:', 'the same picture lands differently depending on the mouse’s state. Can that state be read from outside the head, in a person?', '#', 'Chapter 3')}""",
      "We tried to break it. When we gave guesser B the wrong moments’ state, the gain almost vanished. Leaving out any one mouse kept the gain. So state really matters inside the brain. Next question: can we read it from outside, in a person?")
# 7
slide("ch3-how", "Chapter 3: how the EEG study works.", f"""
{head('Chapter 3 · Measure · EEG study', 'Can sensors on the head tell when someone’s eyes are closed?', 'EEG is a cap of small sensors that pick up the brain’s electrical activity through the scalp. Closing your eyes is one of the clearest changes it can see.', 'eegHero')}
{B.grid([
    ('activity', 'The recording', 'One person, two minutes', '14 sensors, about 128 readings a second, each moment marked open or closed.'),
    ('timeline', 'Learn, then test', 'Earlier, then later', 'Learn from the first part, test on what comes after, like a real app would.'),
    ('target', 'The score', '0.5 is a coin flip', '1.0 is always right. Below 0.5 is worse than guessing.'),
])}""",
      "Now a person. EEG is a cap of sensors on the head. Closing your eyes is one of the easiest changes for it to see. If a simple model cannot read even that reliably, quieter states like tiredness will be harder. We always learn from earlier and test on later.")
# 8
slide("ch3-result", "Chapter 3 result: good on one stretch, a coin flip over time.", f"""
{head('Chapter 3 · The result', 'On one stretch, yes. Over time, no.')}
{answer('On the last part of the recording the model scored <b>0.625</b> (0.728 once four broken readings were capped). Across five stretches it averaged <b>0.478: about a coin flip.</b>')}
{B.chart('eeg-scale', 'How to read the score', 'Where the results sit between guessing and always right.', 'Near 0.5 is no better than flipping a coin. Below 0.5 means the pattern it learned has flipped.', 'The score is called AUC.')}""",
      "On one stretch it worked reasonably well. But when we tested it on five stretches across the recording, it averaged a coin flip.")
# 9
slide("ch3-drift", "Chapter 3: scores on five stretches scatter around a coin flip.", f"""
{head('Chapter 3 · Over time', 'Within two minutes, the signal drifts.')}
{B.chart('eeg-folds', 'Five stretches in time', 'Across the recording, it drifts to a coin flip.', 'Some stretches fall well below 0.5: the pattern learned earlier had flipped by later on. Capping broken readings and leaving a gap do not fix it.', 'Mixing up the answers gives 0.499, so the method itself does not invent a pattern.')}
{B.bridge('What chapter 3 tells us:', 'a sensor that is right on one stretch and wrong on the next is not something to build a tool on. So the apps ask the person instead.', '#', 'Chapter 4')}""",
      "Each dot is one stretch. They land on both sides of a coin flip, and some are worse than guessing. Within two minutes, the signal drifted. So a tool should not try to guess someone’s state from a sensor.")
# 10
slide("ch4-rules", "Chapter 4: four findings become four design rules.", f"""
{head('Chapter 4 · Design · Human–computer interaction', 'From findings to features.')}
{cards([
    ('From chapter 2', 'Show less when energy is low.', '<b>Found:</b> the same picture lands differently depending on state.', '<b>In the apps:</b> “How much energy do you have today?” On “A little”, just the next step.'),
    ('From chapter 3', 'Ask, don’t guess.', '<b>Found:</b> a sensor read state once, then drifted.', '<b>In the apps:</b> the person says how they are. Nothing happens until they tap.'),
    ('From chapter 3', 'Expect change halfway.', '<b>Found:</b> within two minutes the pattern shifted.', '<b>In the apps:</b> Save &amp; pause, a note of where you stopped, break reminders.'),
    ('From real life', 'When stuck, make it smaller.', '<b>Seen:</b> a task too big all at once is where people stop.', '<b>In the apps:</b> “I’m stuck” makes the step smaller and keeps your place.'),
], 'rules')}""",
      "This is where the science turns into design. Each finding gives a rule, and each rule is a real feature in the apps.", "dense")
# 11
slide("ch4-screens", "Chapter 4: the rules on real screens in Next Step and Helper Jobs.", f"""
{head('Chapter 4 · On real screens', 'Two apps, real-world help.', 'Next Step, by Amishi Mehta, for schoolwork. Helper Jobs, a family project, for real jobs at Pragnya outings.')}
<ol class="landing-demo deck-shots">
{B.shot('../img/next-step-energy.jpg', 'Next Step energy check.', 'Show less when energy is low', 'The plan shrinks to one step.')}
{B.shot('../img/next-step-stuck.jpg', 'Next Step pause and I’m stuck.', 'Pause, and make it smaller', 'Your place is kept.')}
{B.shot('../img/helper-jobs-phone.jpg', 'Helper Jobs picture step.', 'One picture step, read aloud', 'With a Help button.')}
</ol>""",
      "Here they are. Next Step asks about energy and shrinks the plan. Save and pause and I’m stuck make it easy to stop and come back. Helper Jobs gives one picture step at a time, read aloud, with a Help button that reaches a volunteer.")
# 12
slide("ch5", "Chapter 5: the road ahead in four steps.", f"""
{head('Chapter 5 · Test, then go further', 'Where this goes next.', 'Everything here is a plan, and labelled that way.')}
{cards([(k, h, a, b) for k, h, a, b in B.ROADMAP])}""",
      "Next, with an ASDRP mentor, we run four more data experiments and write the first paper, on why the EEG drifts. Then design studies with the people the apps are for. Longer term, the joined-up question: does designing for state help people learn?", "dense")
# 13
slide("close", "The loop, who did what, and where to see everything.", f"""
{head('Thank you', 'From neurons to next steps.')}
{answer('<b>The loop:</b> real life raised the question; the mouse showed that state changes what a brain takes in; the EEG showed that state is hard to read from outside; so the apps ask how someone is doing and keep each step small. <span>Three mice and one person are a start, not a rule for everyone.</span>')}
<div class="landing-facts"><div class="landing-fact"><h2>See it all</h2><p>Website: mehtama1234.github.io/ASDRP-Neuroscience-Portfolio<br>Phone tour, slides, Next Step and Helper Jobs are all linked from there.</p></div><div class="landing-fact"><h2>Who did what</h2><p>The studies were done by the applicant with a parent collaborator. Software tools, including AI assistants, helped build the site and the apps. Every number comes from saved results.</p></div></div>""",
      "To sum up the loop. Everything I showed is on the website, with the phone tour, these slides and both apps linked from it. Thank you.")

DECK_CSS = """html,body{margin:0;width:1000px;height:563px;overflow:hidden;background:var(--bg,#F3ECE1)}main#app{margin:0!important;padding:0!important;max-width:none!important;width:1000px}
.deck-slide{width:1000px;height:563px;max-width:none!important;margin:0!important;border:0!important;box-sizing:border-box;padding:30px 44px 38px;display:flex;flex-direction:column;justify-content:center;gap:4px;position:relative;overflow:hidden}
.deck-slide .landing-hero{gap:30px}.deck-slide h1{font-size:44px;line-height:1.08;margin:0 0 10px}.deck-slide .landing-hero h1{font-size:60px}
.deck-slide .hj-sub{font-size:17px;max-width:640px}.deck-slide .lm-head{margin-bottom:12px;align-items:center}.deck-slide .hj-art{max-width:250px}
.deck-slide .landing-problems{margin:6px 0}.deck-slide .lm-grid{margin-top:8px}.deck-slide .lm-grid li{padding:14px 16px}.deck-slide .lm-grid p{font-size:14px}
.deck-slide .chart-card{margin:8px 0 0}.deck-slide .landing-problems.answer.bridge{margin-top:14px}
.deck-slide .loop-figure{margin-top:10px}.deck-slide .landing-problems li{padding:14px 16px}.deck-slide .landing-problems .lp-pain,.deck-slide .landing-problems .lp-fix{font-size:14px}
.deck-shots{grid-template-columns:repeat(3,1fr)!important}.deck-shots img{max-height:330px;width:auto!important;max-width:100%;object-fit:contain}
.deck-foot{position:absolute;left:44px;right:44px;bottom:12px;display:flex;justify-content:space-between;font:600 11px/1 system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.deck-slide .family-links{display:none}
.deck-slide h1{font-size:34px!important}.deck-slide .landing-hero h1{font-size:54px!important}.deck-slide .hj-sub{font-size:15px}
.deck-slide .chart-card{grid-template-columns:1.3fr 1fr;padding:12px 16px;gap:18px;align-items:center}.deck-slide .chart-card svg.chart{max-height:215px;width:100%}.deck-slide .chart-card h3{font-size:19px}.deck-slide .chart-card p{font-size:13px}
.deck-slide .lp-energy{font-size:14px;padding:12px 16px}.deck-slide .deck-shots img{max-height:225px}.deck-slide .deck-shots strong{font-size:15px}.deck-slide .deck-shots span{font-size:12px}
.deck-slide.dense .landing-problems .lp-pain,.deck-slide.dense .landing-problems .lp-fix{font-size:12.5px;line-height:1.4}.deck-slide.dense .landing-problems h3{font-size:16px}
.deck-slide .lm-grid h3{font-size:17px}"""


def slide_html(i, s):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Slide {i}</title>
<link rel="stylesheet" href="../../assets/base.css"><link rel="stylesheet" href="../../assets/experience.css"><link rel="stylesheet" href="../../assets/theme-atlas.css"><link rel="stylesheet" href="../../assets/styles.css"><link rel="stylesheet" href="../../assets/charts.css">
<style>{DECK_CSS}</style></head><body><main id="app"><section class="screen active landing deck-slide {s['cls']}">{s['body'].replace('src="../img/', 'src="../../img/')}
<p class="deck-foot"><span>From neurons to next steps</span><span>{i} / {len(SLIDES)}</span></p></section></main>
<script src="../../assets/icons.js"></script><script src="../../assets/icons-extra.js"></script><script src="../../assets/art.js"></script><script src="../../assets/science-art.js"></script>
<script src="../../assets/results.js"></script><script src="../../assets/charts.js"></script><script src="../../assets/site.js"></script></body></html>"""


def main():
    from playwright.sync_api import sync_playwright
    from PIL import Image
    src = P / "src"; out = P / "slides"; src.mkdir(exist_ok=True); out.mkdir(exist_ok=True)
    for old in out.glob("*.jpg"): old.unlink()
    files = []
    for i, s in enumerate(SLIDES, 1):
        name = f"{i:02d}-{s['key']}"
        (src / f"{name}.html").write_text(slide_html(i, s)); files.append(name)
    with sync_playwright() as pw:
        b = pw.chromium.launch(args=["--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": 1000, "height": 563}, device_scale_factor=1.92)
        for name in files:
            pg.goto((src / f"{name}.html").as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(200)
            over = pg.evaluate("""() => { const s = document.querySelector('.deck-slide'); return s.scrollHeight > s.clientHeight + 1 || s.scrollWidth > s.clientWidth + 1 }""")
            if over: print("OVERFLOW", name)
            pg.screenshot(path=str(out / f"{name}.png"))
            Image.open(out / f"{name}.png").convert("RGB").save(out / f"{name}.jpg", quality=88, optimize=True); (out / f"{name}.png").unlink()
        b.close()
    imgs = [Image.open(out / f"{n}.jpg").convert("RGB") for n in files]
    imgs[0].save(P / PDF, save_all=True, append_images=imgs[1:], resolution=144)
    items = [{"src": f"slides/{n}.jpg", "alt": s["alt"], "notes": s["notes"]} for n, s in zip(files, SLIDES)]
    (P / "present.html").write_text(viewers.page("Slides · From neurons to next steps", "Slide", items, "./", "All slides", True, PDF))
    (P / "presenter.html").write_text(viewers.presenter(items))
    figs = "".join(f'<li><a href="present.html#{i}"><img src="slides/{n}.jpg" alt="Slide {i}: {html.escape(s["alt"])}" loading="{"eager" if i < 3 else "lazy"}" width="1920" height="1080" style="width:100%;height:auto;border:1px solid var(--line);border-radius:var(--radius-card)"></a><strong>{i} · {html.escape(s["alt"].split(":")[0])}</strong><span>{html.escape(s["notes"][:140])}{"…" if len(s["notes"]) > 140 else ""}</span></li>' for i, (n, s) in enumerate(zip(files, SLIDES), 1))
    B.page("presentation/index.html", "Slides · From neurons to next steps", f"The {len(SLIDES)} slides for From neurons to next steps, with speaker notes.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{B.heading(('../index.html', 'All chapters'), 'The slides', '<span id="page-title">The same story, in {len(SLIDES)} slides.</span>', 'Built from the same words, charts and drawings as the website. Present full screen, open the presenter view with speaker notes, or download the PDF.', 'loop')}
      <div class="landing-actions"><a class="button primary" href="present.html">Present <span aria-hidden="true">→</span></a><a class="button secondary" href="presenter.html">Presenter view with notes</a><a class="button secondary" href="{PDF}" download>Download PDF</a></div>
      <ol class="landing-demo deck-list" aria-label="All slides" tabindex="0">{figs}</ol>
    </section>""", base="../")
    print("deck:", len(SLIDES), "slides")


if __name__ == "__main__":
    main()
