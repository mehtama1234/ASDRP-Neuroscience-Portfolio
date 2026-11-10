// Fills in icons, illustrations and charts on every portfolio page.
(function () {
  const R = window.PortfolioResults, C = window.PortfolioCharts;
  document.querySelectorAll('[data-icon]').forEach(el => { el.innerHTML = window.HelperJobsIcons.icon(el.dataset.icon); });
  document.querySelectorAll('[data-art]').forEach(el => { el.innerHTML = window.HelperJobsArt.draw(el.dataset.art); });
  const pct = v => `+${(v * 100).toFixed(1)}`;
  const charts = {
    'mouse-scores': () => C.groupedBars({
      caption: 'Held-out prediction for three mice: the picture alone compared with the picture plus pupil and running.',
      series: ['Picture only', 'Picture + pupil and running'], max: 0.25, ticks: 5,
      groups: R.mouse.mice.map(m => ({ label: m.id, values: [m.stimulus, m.behavior] }))
    }),
    'mouse-gain': () => C.rowBars({
      caption: 'How much behaviour adds for each mouse (gain in held-out correlation).', max: 0.06, height: 220,
      items: R.mouse.mice.map(m => ({ label: m.id, value: +(m.behavior - m.stimulus).toFixed(3) })),
      format: v => (v === 0 ? '0' : `+${v.toFixed(3).replace(/^0/, '')}`)
    }),
    'mouse-loo': () => C.rowBars({
      caption: 'Average gain from behaviour after leaving each mouse out in turn.', max: 0.06, height: 220, tone: 's0',
      items: R.mouse.leave_one_out_mean_gain.map(m => ({ label: `Without ${m.omit.toLowerCase()}`, value: m.gain })),
      format: v => `+${v.toFixed(3).replace(/^0/, '')}`
    }),
    'eeg-holdout': () => C.groupedBars({
      caption: 'Final held-out block: score for each model as first run and with the four glitch samples limited.',
      series: ['As first run', 'Glitches limited'], max: 0.8, min: 0, ticks: 4,
      groups: [{ label: 'Single moment', values: [R.eeg.holdout[0].auc, R.eeg.glitches.holdout[0]] }, { label: 'With last 9 samples', values: [R.eeg.holdout[1].auc, R.eeg.glitches.holdout[1]] }]
    }),
    'eeg-folds': () => C.foldDots({
      caption: 'Score on each of five later blocks of the recording; the dashed line is a coin flip.',
      rows: [
        { label: 'Single moment', values: R.eeg.folds.pointwise, mean: R.eeg.fold_means['pointwise EEG'] },
        { label: 'Last 9 samples too', values: R.eeg.folds.context, mean: R.eeg.fold_means['EEG + causal temporal context'], tone: 'ink' },
        { label: 'Glitches limited', values: R.eeg.glitches.folds.pointwise, mean: R.eeg.glitches.means[0], tone: 'soft' },
        { label: 'Gap of 90 samples', values: R.eeg.gap_folds.pointwise, mean: R.eeg.gap_means['pointwise EEG'], tone: 'soft' }
      ]
    }),
    'eeg-windows': () => C.groupedBars({
      caption: 'How much of the past the model sees: final block and average of five blocks.',
      series: ['Final block', 'Average of 5 blocks'], max: 0.8, ticks: 4,
      groups: R.eeg.windows.map(w => ({ label: `${w.window} samples`, values: [w.holdout, w.blocked] }))
    })
  };
  document.querySelectorAll('[data-chart]').forEach(el => { if (charts[el.dataset.chart]) el.innerHTML = charts[el.dataset.chart](); });
  document.querySelectorAll('[data-num]').forEach(el => {
    const path = el.dataset.num.split('.'); let v = R; for (const p of path) v = v == null ? v : v[p];
    if (typeof v === 'number') el.textContent = el.dataset.fmt === 'gain' ? pct(v) : C.fmt(v);
  });
})();
