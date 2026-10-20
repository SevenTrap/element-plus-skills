---
name: "element-plus-design-typography"
description: "Apply Element Plus 2.14.6 typography tokens and distinguish documented font recommendations from actual emitted CSS defaults."
metadata:
  author: jiaiyan
  version: "1.0.0"
  element-plus-version: "2.14.6"
---

# Element Plus typography

Target **Element Plus 2.14.6**, default `el` namespace. The typography guide recommends an Inter-first font stack, while theme-chalk's actual default `--el-font-family` starts with Helvetica Neue. Do not confuse the recommendation with the emitted theme token.

## Font stack

Documented application recommendation:

```css
body {
  font-family: Inter, 'Helvetica Neue', Helvetica, 'PingFang SC',
    'Hiragino Sans GB', 'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
}
```

Element Plus does not load Inter for the application. Use the project's existing font assets/loading strategy if choosing it. To align with the actual component theme token use `font-family: var(--el-font-family)`; its default is the above stack without Inter.

## Emitted typography variables

| Variable | Default |
| --- | --- |
| `--el-font-size-extra-large` | `20px` |
| `--el-font-size-large` | `18px` |
| `--el-font-size-medium` | `16px` |
| `--el-font-size-base` | `14px` |
| `--el-font-size-small` | `13px` |
| `--el-font-size-extra-small` | `12px` |
| `--el-font-weight-primary` | `500` |
| `--el-font-line-height-primary` | `24px` |

`--el-font-weight-secondary` and `--el-font-line-height-secondary` are not emitted by this release. Set application values explicitly rather than relying on those nonexistent tokens. The typography demo illustrates unitless line-height values 1, 1.3, 1.5, and 1.7; these are examples, not additional theme variables.

```css
.heading {
  font-size: var(--el-font-size-extra-large);
  font-weight: var(--el-font-weight-primary);
  color: var(--el-text-color-primary);
}
.body-copy {
  font-family: var(--el-font-family);
  font-size: var(--el-font-size-base);
  line-height: 1.5;
  color: var(--el-text-color-regular);
}
```

## Text component

```vue
<template>
  <el-text type="primary" size="large">Heading-like text</el-text>
  <el-text style="width: 160px" truncated>Long single-line content</el-text>
  <el-text :line-clamp="2">Long content limited to two lines</el-text>
</template>
```

Text supports semantic `type` values `primary`, `success`, `warning`, `danger`, `info`, plus the default empty type; sizes are `large`, `default`, `small`. Give truncation a width constraint. Use actual heading elements or Text's `tag` prop when heading semantics are required; font size alone does not create a heading. Dark mode changes the consumed text colors, not font size or family.

For detailed Text props use the sibling [Text skill](../components/el-text/SKILL.md). For text colors use [color tokens](../element-plus-design-color/SKILL.md).

## Versioned sources

Validated against Element Plus **2.14.6**. Use the release sources below when checking details; the upstream `dev` branch can contain unreleased changes.

- [docs/en-US/component/typography.md](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/typography.md)
- [docs/en-US/component/text.md](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/text.md)
- [packages/theme-chalk/src/common/var.scss](https://github.com/element-plus/element-plus/blob/2.14.6/packages/theme-chalk/src/common/var.scss)
- [packages/theme-chalk/src/var.scss](https://github.com/element-plus/element-plus/blob/2.14.6/packages/theme-chalk/src/var.scss)
- [docs/examples/typography/line-height.vue](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/typography/line-height.vue)
