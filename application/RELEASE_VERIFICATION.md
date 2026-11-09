# Release verification record

Last technical verification: 2026-11-09.

## Source state

- Portfolio repository: `mehtama1234/ASDRP-Neuroscience-Portfolio`, commit
  `0dd0397` or later.
- Flagship repository: `AmishI123/neuroscience-project`, commit `1cfe112`.
- Hosted portfolio: Site version 27, deployment status `succeeded`.

## Verification command

```bash
python3 application/audit_portfolio.py
python3 application/verify_public_release.py
```

Results: `PORTFOLIO AUDIT PASSED` and `PUBLIC RELEASE VERIFICATION PASSED`.

## Key artifact hashes

| Artifact | SHA-256 |
|---|---|
| `application/ASDRP-neuroscience-portfolio-packet.pdf` | `bd5457525a488fef429a7d060a5e137ef89630b257de3c3e0f63d983d9235314` |
| `communication/video/renders/eeg-research-storyboard.mp4` | `acd1a4fada91e3ce17d6bfd5ac9611fbebcfefcff2a8befe8e8c497a77852646` |
| `communication/video/renders/portfolio-research-storyboard.mp4` | `05266ba689a482244850720e950c2b79da3276f829d927b432088109ea68a1b4` |
| `communication/video/renders/mouse-research-storyboard.mp4` | `51ae34b49c644727cc847a56b485c7f7eb02c9dea6c4eeb9de24e0081b344073` |
| `communication/projects/neuroscience-mobile/releases/neuroscience-lab-debug.apk` | `0549e522f492b8ea5c110554e780ca8027294e31a838b57921157774b8b5e3c1` |

This record verifies the technical package only. Applicant-authored essays,
voice narration, physical-device acceptance, and future population-level
uncertainty remain separately labeled in the final submission gate.

The EEG metrics now also include a 20-permutation global label-shuffle control
under `blocked_label_shuffle_control`: mean shuffled ROC AUC 0.499 for the
pointwise model and 0.501 for causal context. They also include a 90-sample
purge-gap sensitivity analysis: mean ROC AUC 0.448 pointwise and 0.443 with
causal context.
