# Reproducibility checklist

## Mouse visual-cortex study

- [x] Public repository with six notebooks
- [x] Dataset source documented in the report
- [x] Training-only preprocessing described
- [x] Baseline and behavior-augmented models defined
- [x] Held-out evaluation reported
- [x] Replication across one additional mouse
- [x] Core dependency manifest added (`neuroscience-project/requirements.txt`)
- [ ] Automated clean-environment run from that manifest
- [ ] Statistical uncertainty and confidence intervals

## EEG eye-state study

- [x] Public UCI dataset downloaded and provenance documented
- [x] Raw ARFF file retained in `data/raw/`
- [x] Chronological split specified in code and report
- [x] Baseline and extension implemented
- [x] Held-out metrics saved in `results/metrics.json`
- [x] Negative result documented rather than discarded
- [ ] Additional recordings or blocked cross-validation
- [ ] Pinned dependency file

## Communication artifacts

- [x] Interactive HTML explainers
- [x] Mobile interaction specifications
- [x] Presentation outlines
- [x] Video scripts
- [x] Scope and limitations notes
- [ ] Recorded final videos
- [x] Final exported ASDRP PDF packet
