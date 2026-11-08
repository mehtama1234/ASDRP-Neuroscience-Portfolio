# Release verification record

Last technical verification: 2026-11-08.

## Source state

- Portfolio repository: `mehtama1234/ASDRP-Neuroscience-Portfolio`, commit
  `a92d0e8` or later.
- Flagship repository: `AmishI123/neuroscience-project`, commit `2f7ab92`.
- Hosted portfolio: Site version 17, deployment status `succeeded`.

## Verification command

```bash
python3 application/audit_portfolio.py
```

Result: `PORTFOLIO AUDIT PASSED`.

## Key artifact hashes

| Artifact | SHA-256 |
|---|---|
| `application/ASDRP-neuroscience-portfolio-packet.pdf` | `f7e38972aa30694af094177401785e1798d7bd0398bb6286d573a055665d61a1` |
| `communication/video/renders/eeg-research-storyboard.mp4` | `b80f0e2468843ae8a7ebe453aa3dc87faca182fe4f8fdd956832960e666b39a0` |
| `communication/video/renders/mouse-research-storyboard.mp4` | `51ae34b49c644727cc847a56b485c7f7eb02c9dea6c4eeb9de24e0081b344073` |
| `communication/projects/neuroscience-mobile/releases/neuroscience-lab-debug.apk` | `0549e522f492b8ea5c110554e780ca8027294e31a838b57921157774b8b5e3c1` |

This record verifies the technical package only. Applicant-authored essays,
voice narration, physical-device acceptance, and future population-level
uncertainty remain separately labeled in the final submission gate.
