# Element Plus Skills Library

Version-specific skills for **Element Plus 2.14.6** and Vue `^3.3.7`.

[中文说明](README_CN.md) · [Skill entrypoint](SKILL.md) · [Component index](element-plus-components/SKILL.md) · [Version evidence](references/version-baseline.md)

## Contents

The library contains **89 topic skills plus the root routing skill (90 total)**:

| Group | Topics | Location |
| --- | --- | --- |
| Components | 78 | `components/el-*/SKILL.md` |
| Foundation | 6 | Quickstart, theming, i18n, dark mode, SSR, component index |
| Design | 5 | Overview, border, color, typography, layout |

Each component skill provides usage decisions, version-specific constraints, a Vue or service example, and a link to its complete `references/api.md`. Family skills cover companion components. InputOtp, introduced before the target release, is included. DateTimePicker is a usage mode of DatePicker rather than a separate component export.

## Use

Start with [SKILL.md](SKILL.md), select the relevant topic, and load its API reference only when exact signatures or defaults are needed. All examples target 2.14.6. Install the matching package in the application:

```sh
npm install --save-exact element-plus@2.14.6
```

Follow [quickstart](element-plus-quickstart/SKILL.md) for Vue registration, styles, icons, automatic imports and TypeScript. Importing a component alone does not load the global stylesheet.

The fixed tag is the compatibility authority. The audited `dev` snapshot contains later changes and is used for comparison. [Version evidence](references/version-baseline.md) records the commits, excluded APIs and source corrections; [source-manifest.json](references/source-manifest.json) records reference provenance.

## Maintain and validate

Keep exact version claims consistent across topic guidance, examples and API references. Verify questionable documentation against the same tag's prop definitions and implementation. Preserve the reference attribution and update its manifest hash whenever correcting adapted content.

```sh
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/validate_skills.py
```

Python 3 and PyYAML are required for the validation scripts. Structural checks do not replace running application-level Vue/TypeScript and interaction tests. See [AGENTS.md](AGENTS.md) for maintenance scope and routing conventions.

## License

This library uses the [MIT license](LICENSE). Adapted Element Plus documentation retains its [upstream MIT notice](references/upstream-LICENSE).
