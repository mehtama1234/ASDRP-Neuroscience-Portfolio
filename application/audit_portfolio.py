"""Small, dependency-free handoff audit for the ASDRP portfolio."""

from pathlib import Path
import hashlib
import json
import re


ROOT = Path(__file__).resolve().parents[1]


def require(path: str) -> None:
    target = ROOT / path
    if not target.is_file() or target.stat().st_size == 0:
        raise SystemExit(f"MISSING: {path}")
    print(f"OK file {path}")


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def contains(path: str, pattern: str) -> None:
    if not re.search(pattern, text(path), re.IGNORECASE):
        raise SystemExit(f"MISSING text /{pattern}/ in {path}")
    print(f"OK text {path}: /{pattern}/")


def main() -> None:
    required = [
        "application/ASDRP-neuroscience-portfolio-packet.pdf",
        "application/contribution-ledger.md",
        "application/reproducibility-checklist.md",
        "communication/projects/mouse-visual-cortex/index.html",
        "communication/projects/mouse-visual-cortex/slides.html",
        "communication/projects/neuroscience-mobile/index.html",
        "communication/projects/neuroscience-mobile/releases/neuroscience-lab-debug.apk",
        "communication/projects/neuroscience-mobile/native/dist/index.html",
        "communication/video/renders/mouse-research-storyboard.mp4",
        "communication/video/renders/mouse-research-storyboard.vtt",
        "communication/video/renders/eeg-research-storyboard.mp4",
        "communication/video/renders/eeg-research-storyboard.vtt",
        "communication/video/renders/portfolio-research-storyboard.mp4",
        "communication/video/renders/portfolio-research-storyboard.vtt",
        "website/reviewer-dashboard.html",
        "website/eeg-label-shuffle-control.html",
        "projects/eeg-eye-state/results/metrics.json",
        "projects/eeg-eye-state/REPRODUCIBILITY_RUN.md",
        "../neuroscience-project/results/per_mouse_replication_summary.json",
        "../neuroscience-project/results/shuffled_behavior_controls.json",
    ]
    for path in required:
        require(path)

    csv = (ROOT.parent / "neuroscience-project/results/per_mouse_metrics.csv").read_text(encoding="utf-8")
    rows = [line for line in csv.splitlines() if line.strip()]
    if len(rows) != 4:
        raise SystemExit(f"EXPECTED 3 mouse rows plus header, found {len(rows)} lines")
    print("OK metrics: three mouse rows")
    for path in (
        "communication/projects/mouse-visual-cortex/index.html",
        "communication/projects/mouse-visual-cortex/slides.html",
        "communication/projects/mouse-visual-cortex/video-script.md",
        "communication/projects/neuroscience-mobile/index.html",
        "application/reviewer-packet.html",
    ):
        contains(path, r"0\.143")
        contains(path, r"0\.191")
        contains(path, r"three")

    reproducibility = (ROOT.parent / "neuroscience-project/docs/REPRODUCIBILITY_RUN.md").read_text(encoding="utf-8")
    if re.search(r"two-mouse|two mice|both animals|beyond two", reproducibility, re.IGNORECASE):
        raise SystemExit("STALE replication scope in flagship reproducibility record")
    print("OK flagship reproducibility scope: three-mouse")
    eeg_metrics = json.loads((ROOT / "projects/eeg-eye-state/results/metrics.json").read_text(encoding="utf-8"))
    blocked = eeg_metrics.get("blocked_cross_validation", [])
    if len(blocked) != 2 or any(item.get("fold_count") != 5 for item in blocked):
        raise SystemExit("EXPECTED five blocked EEG folds for both models")
    print("OK EEG expansion: five forward-chaining folds per model")
    shuffled_eeg = eeg_metrics.get("blocked_label_shuffle_control", [])
    if len(shuffled_eeg) != 2 or any(item.get("permutations") != 20 for item in shuffled_eeg):
        raise SystemExit("EXPECTED 20 label-shuffle controls for both EEG models")
    print("OK EEG negative control: 20 label shuffles per model")
    controls = json.loads((ROOT.parent / "neuroscience-project/results/shuffled_behavior_controls.json").read_text(encoding="utf-8"))
    if len(controls) != 3 or any(row.get("permutations") != 20 for row in controls):
        raise SystemExit("EXPECTED 20 behavior-shuffle controls for three mice")
    print("OK mouse negative control: 20 behavior shuffles per animal")

    apk = ROOT / "communication/projects/neuroscience-mobile/releases/neuroscience-lab-debug.apk"
    digest = hashlib.sha256(apk.read_bytes()).hexdigest()
    expected = "0549e522f492b8ea5c110554e780ca8027294e31a838b57921157774b8b5e3c1"
    if digest != expected:
        raise SystemExit(f"APK SHA mismatch: {digest}")
    print(f"OK APK SHA-256 {digest}")
    print("PORTFOLIO AUDIT PASSED")


if __name__ == "__main__":
    main()
