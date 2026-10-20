---
name: "element-plus-design-color"
description: "Use Element Plus 2.14.6 semantic palettes and neutral CSS tokens for application surfaces and theme changes."
metadata:
  author: jiaiyan
  version: "1.0.0"
  element-plus-version: "2.14.6"
---

# Element Plus color tokens

Target **Element Plus 2.14.6**, default `el` namespace. Values below describe the default light theme; dark mode changes neutral and derived palette values when its stylesheet is loaded and `html.dark` is enabled.

## Semantic colors

| Token | Base |
| --- | --- |
| `--el-color-primary` | `#409eff` |
| `--el-color-success` | `#67c23a` |
| `--el-color-warning` | `#e6a23c` |
| `--el-color-danger` | `#f56c6c` |
| `--el-color-error` | `#f56c6c` |
| `--el-color-info` | `#909399` |

Each type has emitted `-light-3`, `-light-5`, `-light-7`, `-light-8`, `-light-9`, and `-dark-2` CSS variables. The Sass map computes light levels 1–9, but the global CSS palette emits only the listed levels. Primary defaults:

| Suffix | Value |
| --- | --- |
| `light-3` | `#79bbff` |
| `light-5` | `#a0cfff` |
| `light-7` | `#c6e2ff` |
| `light-8` | `#d9ecff` |
| `light-9` | `#ecf5ff` |
| `dark-2` | `#337ecc` |

`--el-color-error` exists as a theme token; it does not imply every component accepts `type="error"`. Check component-specific type unions.

## Neutral tokens

| Token | Light value |
| --- | --- |
| `--el-text-color-primary` | `#303133` |
| `--el-text-color-regular` | `#606266` |
| `--el-text-color-secondary` | `#909399` |
| `--el-text-color-placeholder` | `#a8abb2` |
| `--el-text-color-disabled` | `#c0c4cc` |
| `--el-bg-color` | `#ffffff` |
| `--el-bg-color-page` | `#f2f3f5` |
| `--el-bg-color-overlay` | `#ffffff` |
| `--el-fill-color` | `#f0f2f5` |
| `--el-fill-color-light` | `#f5f7fa` |
| `--el-fill-color-lighter` | `#fafafa` |
| `--el-fill-color-extra-light` | `#fafcff` |
| `--el-fill-color-dark` | `#ebedf0` |
| `--el-fill-color-darker` | `#e6e8eb` |
| `--el-fill-color-blank` | `#ffffff` |

Use border tokens such as `--el-border-color` for boundaries, and text tokens for hierarchy. White/black are available as `--el-color-white` and `--el-color-black`.

```css
.notice {
  color: var(--el-color-success);
  background: var(--el-color-success-light-9);
  border: 1px solid var(--el-color-success-light-5);
}
.caption { color: var(--el-text-color-secondary); }
```

Changing only `--el-color-primary` at runtime does not regenerate its compiled variants. Override the full relevant palette (including RGB tokens if consumers use them), or configure Sass `$colors` and rebuild. Evaluate custom combinations in light and dark mode; semantic color names do not guarantee accessible contrast for arbitrary text sizes.

## Versioned sources

Validated against Element Plus **2.14.6**. Use the release sources below when checking details; the upstream `dev` branch can contain unreleased changes.

- [docs/en-US/component/color.md](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/color.md)
- [packages/theme-chalk/src/common/var.scss](https://github.com/element-plus/element-plus/blob/2.14.6/packages/theme-chalk/src/common/var.scss)
- [packages/theme-chalk/src/mixins/_var.scss](https://github.com/element-plus/element-plus/blob/2.14.6/packages/theme-chalk/src/mixins/_var.scss)
- [packages/theme-chalk/src/dark/var.scss](https://github.com/element-plus/element-plus/blob/2.14.6/packages/theme-chalk/src/dark/var.scss)
