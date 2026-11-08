# Rendered research videos

The storyboard renderer creates silent, captioned MP4 review artifacts from the
verified project facts. They are useful for checking pacing and visual hierarchy.

They are not being presented as final narrated videos. Before application use, add
the applicant’s own narration, captions/transcript, collaboration credit, and a
spoken limitations section as specified in `application/video-production-plan.md`.

Render locally:

```bash
python3 communication/video/build_storyboard.py mouse
python3 communication/video/build_storyboard.py eeg
```
