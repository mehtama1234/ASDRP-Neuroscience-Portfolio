# Contribution ledger

This ledger makes authorship and contribution boundaries visible to a reviewer.

| Artifact | Applicant contribution to claim | Collaborator/support contribution | Evidence |
|---|---|---|---|
| Mouse project question | Helped define the comparison between stimulus-only and behavior-augmented prediction; applicant should describe the exact discussion in their own words. | Parent/collaborator helped scope the question. | `neuroscience-project/docs/PROJECT_PLAN.md` |
| Mouse data exploration | Learned Python, loaded the Sensorium data, inspected neural and behavior variables, and performed exploratory analysis. | Technical setup and debugging support. | `neuroscience-project/notebooks/01`–`02` |
| Mouse encoding models | Built and compared ridge-regression baselines and held-out evaluation. | Code review and modeling guidance. | `neuroscience-project/notebooks/03`–`05` |
| Mouse interpretation | Investigated pupil versus running ablations and arousal-sensitive neurons. | Review of analysis choices and writing feedback. | `neuroscience-project/docs/REPORT.md` |
| EEG project | Implemented the analysis script, chronological split, metrics, report, and explainer in this portfolio repository. | Portfolio architecture and review support. | `projects/eeg-eye-state/` |
| EEG robustness extensions | The repository now contains five-fold blocked evaluation, 20 label permutations, and a 90-sample purge-gap sensitivity analysis; the applicant should confirm which portions they personally ran, interpreted, or presented. | Technical review and reproducibility support. | `projects/eeg-eye-state/src/analyze.py`, `results/metrics.json` |
| Mouse replication robustness | The repository now contains a three-animal summary, behavior-shuffle controls, and leave-one-animal-out stability analysis; the applicant should confirm their exact role in running and interpreting each extension. | Technical review, debugging, and release integration. | `neuroscience-project/src/summarize_replication.py`, `results/per_mouse_replication_summary.json` |
| Reviewer-facing portfolio | The applicant should identify which demos, slides, PDFs, and video scripts they designed, edited, tested, or presented; the repository proves the artifacts exist but not personal ownership of every edit. | Implementation, packaging, and deployment support. | `website/`, `communication/`, public Site |
| Applied neurotechnology | Participated in the design and documentation of communication/accessibility concepts; exact personal contribution should be specified by the applicant. | Existing `neuro-divergent` and `neurocomms` repositories contain the implementation history. | Linked project repositories |

## Before submission

- Replace “helped” with precise first-person actions where accurate.
- Identify which code was written by the applicant versus adapted or reviewed.
- Keep the parent/collaborator relationship explicit.
- Do not claim independent authorship for work that was collaborative.
