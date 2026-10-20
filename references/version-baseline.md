# Element Plus 2.14.6 version baseline

This library targets **2.14.6**, not the moving `dev` branch. Audited on **2026-10-20**.

| Source | Fixed commit |
| --- | --- |
| [Official 2.14.6 tag](https://github.com/element-plus/element-plus/tree/2.14.6) | `5ac2b162180d3922d77c50990bb40c2f02376796` |
| [Official dev snapshot](https://github.com/element-plus/element-plus/tree/06602dff62d3ddb300782f8254a2f28b617ec216) | `06602dff62d3ddb300782f8254a2f28b617ec216` |

## Authority and coverage

Use tag documentation for API contracts and examples, and tag `packages/components` implementations/types to resolve documentation mistakes. Published package imports use `element-plus`; this monorepo's internal `@element-plus/*` aliases are not application import paths. The source package's placeholder `0.0.0-dev.1` is replaced during release and is not the target release version.

The tag's package peer dependency is Vue `^3.3.7`. Sass source customization requires Sass 1.79.0 or later. The upstream repository's Node engine and package manager describe contributor tooling, not a universal application runtime requirement.

The library includes 78 component topic skills, 6 foundation skills and 5 design skills, plus the root router: 90 skill files. InputOtp was added to cover the target release's previously missing documentation page. Family skills cover related exports such as ImageViewer, Countdown, FormItem, TableColumn, and AutoResizer; layout covers Row and Col. These counts describe skill topics, not the number of exported Vue components.

Each component's `references/api.md` contains the API section adapted from its tag documentation. [source-manifest.json](source-manifest.json) records original document SHA-256 hashes, reference hashes, and both upstream commits. The upstream [MIT license](upstream-LICENSE) applies to adapted documentation.

## Differences excluded from dev

The relevant English component documentation changes between the tag and the recorded dev snapshot concern Drawer, Image and Scrollbar. Implementation differences also include calendar/date-panel/dropdown/table/time-picker fixes; these are not backported into this documentation baseline.

- **Drawer:** the object form of `resizable` is marked 2.14.8 in dev. 2.14.6 accepts a boolean.
- **Image/ImageViewer:** dev adds `viewer-placeholder` and related preview behavior marked 2.14.8. Do not infer those slots from current online docs.
- **Scrollbar:** dev adds `mask` and mask customization marked 2.14.8. They are absent from this baseline.
- **i18n:** dev adds Galician (`gl`) to the guide's language list. It is not part of the target tag's language list.

## Source corrections

- Drawer `before-close`: the tag documentation incorrectly suggests `done()` aborts. In `packages/components/dialog/src/use-dialog.ts`, `done(true)` cancels and `done()` / `done(false)` close. The reference corrects this description.
- InputOtp `separator`: the tag props interface declares `(index: number) => string | VNode`; the documentation's shorter callback signature omits the argument. The reference uses the implementation signature.
- TreeSelect's deprecation warning calls child instances `tree` and `select`; the actual exports are `treeRef` and `selectRef`. Use these instance properties.

- Removed legacy props still listed by tag docs: Dialog/Drawer `custom-class`, Select `suffix-transition`, Autocomplete/Cascader/Select V2 `popper-append-to-body`, and Switch `active-color` / `inactive-color` / `border-color`. They have no prop declarations or implementation in 2.14.6. Use `class`, supported teleport props, or Switch CSS variables respectively.
- Upload `handleRemove` takes one `UploadFile | UploadRawFile` argument. The tag docs' optional second `rawFile` argument and v2.2.0 removal note are stale; the implementation is asynchronous.

- Removed accessibility aliases: old `label` props on ColorPicker, Input, InputNumber, Rate, Slider, TimePicker, Switch, CheckboxGroup and RadioGroup are absent from the implementation; use `aria-label`. Checkbox's removed `controls` becomes `aria-controls`. Checkbox/Radio option `label` and deprecated `true-label` / `false-label` remain supported and are retained.
- Tabs supports `add-icon`, not the removed `addIcon` slot. Dialog/Drawer's deprecated `title` slot remains supported until the documented future removal.
- Skeleton `loading` defaults to `true` and displays skeleton content; `false` renders the default slot. The tag docs incorrectly describe the reverse and list `false`.
- Source links embedded in upstream API tables are pinned to 2.14.6 rather than following dev.

## Validation

Run from this directory:

```sh
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/validate_skills.py
```

These checks validate skill metadata, local references, code fences and version boundaries. They do not prove application behavior or replace reading the target implementation. Component examples must be used with the registration/style setup in the quickstart skill; projects should run their own Vue/TypeScript checks and relevant user-flow tests.

### Audit results (2026-10-20)

- 90 skill files passed the skill-creator validator and the local library validator.
- 78 adapted API references matched their recorded content hashes; all 78 upstream documentation hashes were verified against the tag checkout.
- 402 fixed-tag source links resolved to files or directories in the checked-out 2.14.6 source.
- All 85 Vue code blocks passed Vue SFC parsing, script compilation (where applicable), and template compilation. All 85 examples passed `vue-tsc --noEmit` against installed `element-plus@2.14.6`, `vue@3.5.26`, `typescript@5.9.3`, and `vue-tsc@3.1.5`.
- The validation script passed 19 regression tests, with 90.3% line coverage measured using the standard-library trace module.
- Independent review checked version boundaries, API/source contradictions, foundation/design facts, indexes and validation-script behavior.

These are documentation, compilation and type checks. No browser interaction suite was run; snippets containing app-specific routes, server entrypoints or business callbacks still require integration in the host application. Temporary source and dependency checkouts were removed after verification.
