---
name: "element-plus-design-border"
description: "Apply Element Plus 2.14.6 border, radius, and shadow tokens, checking actual theme-chalk defaults rather than legacy Element UI values."
metadata:
  author: jiaiyan
  version: "1.0.0"
  element-plus-version: "2.14.6"
---

# Border, radius, and shadow

Target **Element Plus 2.14.6**, default light theme and `el` namespace. Use tokens rather than resetting all component borders. Dark values require the dark stylesheet and `html.dark`.

## Border tokens

| Variable | Light default |
| --- | --- |
| `--el-border-width` | `1px` |
| `--el-border-style` | `solid` |
| `--el-border-color` | `#dcdfe6` |
| `--el-border-color-light` | `#e4e7ed` |
| `--el-border-color-lighter` | `#ebeef5` |
| `--el-border-color-extra-light` | `#f2f6fc` |
| `--el-border-color-dark` | `#d4d7de` |
| `--el-border-color-darker` | `#cdd0d6` |
| `--el-border-color-hover` | `var(--el-text-color-disabled)` |
| `--el-border` | width + style + color above |

The base color is `--el-border-color`; `--el-border-color-base` is not emitted by 2.14.6.

## Radius tokens

| Variable | Default |
| --- | --- |
| `--el-border-radius-base` | `4px` |
| `--el-border-radius-small` | `2px` |
| `--el-border-radius-round` | `20px` |
| `--el-border-radius-circle` | `100%` |

## Shadow tokens

These are the actual light-theme defaults; older `0 2px 12px` recipes are not the 2.14.6 base shadow.

```css
/* Reference values, not a required global override */
:root {
  --el-box-shadow: 0px 12px 32px 4px rgba(0, 0, 0, 0.04),
    0px 8px 20px rgba(0, 0, 0, 0.08);
  --el-box-shadow-light: 0px 0px 12px rgba(0, 0, 0, 0.12);
  --el-box-shadow-lighter: 0px 0px 6px rgba(0, 0, 0, 0.12);
  --el-box-shadow-dark: 0px 16px 48px 16px rgba(0, 0, 0, 0.08),
    0px 12px 32px rgba(0, 0, 0, 0.12),
    0px 8px 16px -8px rgba(0, 0, 0, 0.16);
}
```

`dark` names a shadow strength, not the dark theme. The dark theme has its own values for all four tokens.

```css
.surface {
  border: var(--el-border);
  border-radius: var(--el-border-radius-base);
  box-shadow: var(--el-box-shadow-light);
}
```

For custom themes override the Sass `$border-color`, `$border-radius`, or `$box-shadow` maps before compiling source styles, or override CSS variables after the bundled CSS. Confirm each component actually consumes the chosen token before relying on a global effect.

## Versioned sources

Validated against Element Plus **2.14.6**. Use the release sources below when checking details; the upstream `dev` branch can contain unreleased changes.

- [docs/en-US/component/border.md](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/border.md)
- [packages/theme-chalk/src/common/var.scss](https://github.com/element-plus/element-plus/blob/2.14.6/packages/theme-chalk/src/common/var.scss)
- [packages/theme-chalk/src/var.scss](https://github.com/element-plus/element-plus/blob/2.14.6/packages/theme-chalk/src/var.scss)
- [packages/theme-chalk/src/dark/var.scss](https://github.com/element-plus/element-plus/blob/2.14.6/packages/theme-chalk/src/dark/var.scss)
