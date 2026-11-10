// Fills in icons, illustrations and charts on every portfolio page.
(function () {
  const R = window.PortfolioResults, C = window.PortfolioCharts;
  document.querySelectorAll('[data-icon]').forEach(el => { el.innerHTML = window.HelperJobsIcons.icon(el.dataset.icon); });
  document.querySelectorAll('[data-art]').forEach(el => { el.innerHTML = window.HelperJobsArt.draw(el.dataset.art); });
  const pct = v => `+${(v * 100).toFixed(1)}`;
  const charts = {
    'mouse-scores': () => C.groupedBars({
      caption: 'Score for three mice on unseen pictures: guesser A (picture only) and guesser B (picture plus pupil and running).',
      series: ['A · picture only', 'B · picture + state'], max: 0.25, ticks: 5,
      groups: R.mouse.mice.map(m => ({ label: m.id, values: [m.stimulus, m.behavior] }))
    }),
    'mouse-scale': () => {
      const m = R.mouse.mice, avg = k => m.reduce((a, b) => a + b[k], 0) / m.length;
      return C.scale({ caption: 'Score scale from 0 (nothing in common) to 1 (perfect match), with the average score of guesser A and guesser B.', band: [avg('stimulus'), avg('behavior')],
        ticks: [{ v: 0, label: '0 · nothing in common' }, { v: 0.5, label: '0.5' }, { v: 1, label: '1 · perfect match' }],
        marks: [{ v: avg('stimulus'), label: `A · picture only ${C.fmt(+avg('stimulus').toFixed(3))}`, tone: 'soft', below: true }, { v: avg('behavior'), label: `B · plus state ${C.fmt(+avg('behavior').toFixed(3))}` }] });
    },
    'eeg-scale': () => C.scale({ caption: 'Score scale from 0 to 1 where 0.5 is a coin flip, with the EEG results marked.', band: [0.45, 0.55],
      ticks: [{ v: 0, label: '0 · always wrong' }, { v: 0.5, label: '0.5 · coin flip' }, { v: 1, label: '1 · always right' }],
      marks: [{ v: R.eeg.fold_means['pointwise EEG'], label: `Over time ${C.fmt(R.eeg.fold_means['pointwise EEG'])}`, tone: 'soft', below: true }, { v: R.eeg.holdout[0].auc, label: `Last stretch ${C.fmt(R.eeg.holdout[0].auc)}`, tone: 'soft' }, { v: R.eeg.glitches.holdout[0], label: `Capped ${C.fmt(R.eeg.glitches.holdout[0])}`, below: true }] }),
    'mouse-gain': () => C.rowBars({
      caption: 'How much knowing the mouse’s state adds, for each mouse.', max: 0.06, height: 220,
      items: R.mouse.mice.map(m => ({ label: m.id, value: +(m.behavior - m.stimulus).toFixed(3) })),
      format: v => (v === 0 ? '0' : `+${v.toFixed(3).replace(/^0/, '')}`)
    }),
    'mouse-loo': () => C.rowBars({
      caption: 'Average gain from behaviour after leaving each mouse out in turn.', max: 0.06, height: 220, tone: 's0',
      items: R.mouse.leave_one_out_mean_gain.map(m => ({ label: `Without ${m.omit.toLowerCase()}`, value: m.gain })),
      format: v => `+${v.toFixed(3).replace(/^0/, '')}`
    }),
    'eeg-holdout': () => C.groupedBars({
      caption: 'Score on the last stretch of the recording for each model, as first run and with four broken readings capped.',
      series: ['As first run', 'Broken readings capped'], max: 0.8, min: 0, ticks: 4,
      groups: [{ label: 'Now only', values: [R.eeg.holdout[0].auc, R.eeg.glitches.holdout[0]] }, { label: 'Now + a moment ago', values: [R.eeg.holdout[1].auc, R.eeg.glitches.holdout[1]] }]
    }),
    'eeg-folds': () => C.foldDots({
      caption: 'Score on each of five later blocks of the recording; the dashed line is a coin flip.',
      rows: [
        { label: 'Now only', values: R.eeg.folds.pointwise, mean: R.eeg.fold_means['pointwise EEG'] },
        { label: 'Now + a moment ago', values: R.eeg.folds.context, mean: R.eeg.fold_means['EEG + causal temporal context'], tone: 'ink' },
        { label: 'Readings capped', values: R.eeg.glitches.folds.pointwise, mean: R.eeg.glitches.means[0], tone: 'soft' },
        { label: 'With a gap', values: R.eeg.gap_folds.pointwise, mean: R.eeg.gap_means['pointwise EEG'], tone: 'soft' }
      ]
    }),
    'eeg-windows': () => C.groupedBars({
      caption: 'How many readings back the model looks: score on the last stretch and average of five stretches.',
      series: ['Last stretch', 'Average of 5 stretches'], max: 0.8, ticks: 4,
      groups: R.eeg.windows.map(w => ({ label: `${w.window} back`, values: [w.holdout, w.blocked] }))
    })
  };
  document.querySelectorAll('[data-chart]').forEach(el => { if (charts[el.dataset.chart]) el.innerHTML = charts[el.dataset.chart](); });
  document.querySelectorAll('[data-num]').forEach(el => {
    const path = el.dataset.num.split('.'); let v = R; for (const p of path) v = v == null ? v : v[p];
    if (typeof v === 'number') el.textContent = el.dataset.fmt === 'gain' ? pct(v) : C.fmt(v);
  });
})();
