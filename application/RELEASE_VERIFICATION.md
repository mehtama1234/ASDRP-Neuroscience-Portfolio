# Release verification record

Last technical verification: 2026-11-09.

## Source state

- Portfolio repository: `mehtama1234/ASDRP-Neuroscience-Portfolio`, commit
  `9799067` or later.
- Flagship repository: `AmishI123/neuroscience-project`, commit `5256a1b`.
- Hosted portfolio: Site version 24, deployment status `succeeded`.

## Verification command

```bash
python3 application/audit_portfolio.py
```

Result: `PORTFOLIO AUDIT PASSED`.

## Key artifact hashes

| Artifact | SHA-256 |
|---|---|
| `application/ASDRP-neuroscience-portfolio-packet.pdf` | `f7e38972aa30694af094177401785e1798d7bd0398bb6286d573a055665d61a1` |
| `communication/video/renders/eeg-research-storyboard.mp4` | `acd1a4fada91e3ce17d6bfd5ac9611fbebcfefcff2a8befe8e8c497a77852646` |
| `communication/video/renders/portfolio-research-storyboard.mp4` | `05266ba689a482244850720e950c2b79da3276f829d927b432088109ea68a1b4` |
| `communication/video/renders/mouse-research-storyboard.mp4` | `51ae34b49c644727cc847a56b485c7f7eb02c9dea6c4eeb9de24e0081b344073` |
| `communication/projects/neuroscience-mobile/releases/neuroscience-lab-debug.apk` | `0549e522f492b8ea5c110554e780ca8027294e31a838b57921157774b8b5e3c1` |

This record verifies the technical package only. Applicant-authored essays,
voice narration, physical-device acceptance, and future population-level
uncertainty remain separately labeled in the final submission gate.
