# Native acceptance status

Status: **scaffolded; native runtime validation not yet claimed.**

This Capacitor wrapper packages the working mobile web demo at
`../index.html` as `org.asdrp.neurosciencelab`. The build script copies the
reviewed HTML and manifest into the Capacitor `dist/` directory.

## Evidence currently available

- Responsive browser demo covers mouse visual cortex and EEG eye state.
- Large tap targets, one-task screens, progress state, scope notes, and print
  research cards are implemented.
- `npm run build` is the deterministic web-asset packaging step.

## Still required before native delivery

- Produce Android/iOS builds after installing the pinned Capacitor dependencies
  with `npm install` and running `npm run sync`.
- Test real back behavior, safe-area cutouts, keyboard/rotation, printing,
  share/export behavior, and offline reopen on both platforms.
- Record device or simulator versions and build hashes in a native runbook.

No native build or device result is represented as complete by this file.

## Current environment check

- `npm install` completed with the pinned package versions; npm reported seven
  transitive audit findings that should be reviewed before public release.
- `npm run sync` passed.
- `npx cap add android` passed and generated the Android project.
- `npx cap add ios` passed and generated the iOS project; CocoaPods and Xcode
  were unavailable, so no iOS build was attempted.
- `android/gradlew assembleDebug --no-daemon` was attempted and stopped before
  compilation because Java/JAVA_HOME is unavailable in this environment.
