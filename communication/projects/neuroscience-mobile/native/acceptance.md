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

- Install the pinned Capacitor dependencies with `npm install`.
- Run `npm run sync` and produce Android/iOS builds.
- Test real back behavior, safe-area cutouts, keyboard/rotation, printing,
  share/export behavior, and offline reopen on both platforms.
- Record device or simulator versions and build hashes in a native runbook.

No native build or device result is represented as complete by this file.
