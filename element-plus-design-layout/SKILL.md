---
name: "element-plus-design-layout"
description: "Build responsive Element Plus 2.14.6 layouts with Row/Col, 24-column spans, gutters, offsets, and display utilities."
metadata:
  author: jiaiyan
  version: "1.0.0"
  element-plus-version: "2.14.6"
---

# Element Plus layout grid

Target **Element Plus 2.14.6**. Row uses flex layout by default; do not add the old `type="flex"` option. A column spans 0–24 units and its default span is 24. Avoid `display: inline` and related styles on the parent when the grid must fill available width.

```vue
<template>
  <el-row :gutter="20" justify="space-between" align="middle">
    <el-col :xs="24" :sm="12" :md="8" :lg="6" :xl="4">
      <div class="panel">Responsive content</div>
    </el-col>
    <el-col :xs="24" :sm="{ span: 10, offset: 2 }" :md="{ span: 8, offset: 0 }">
      <div class="panel">Responsive offset</div>
    </el-col>
  </el-row>
</template>
```

`gutter` is a numeric pixel spacing (default 0). Row uses negative horizontal margins and Col uses half-gutter padding, so check outer container overflow. It does not provide vertical row gaps automatically; add appropriate application CSS for wrapped rows.

## Row and column decisions

- Row `justify`: `start` (default), `center`, `end`, `space-around`, `space-between`, `space-evenly`.
- Row `align`: `top`, `middle`, `bottom`; no default prop value is specified.
- Col `offset`, `push`, `pull`: numeric column units, default 0. Offset creates left space; push/pull visually reposition columns without changing their DOM order.
- Row and Col `tag`: custom element name, default `div`.

## Breakpoints

| Prop | Activation |
| --- | --- |
| `xs` | `<768px` |
| `sm` | `≥768px` |
| `md` | `≥992px` |
| `lg` | `≥1200px` |
| `xl` | `≥1920px` |

`sm` and larger rules apply upward until overridden. Each responsive prop takes a number or `{ span?, offset?, pull?, push? }`. Reset offsets explicitly at larger breakpoints when a previous rule should stop applying.

## Hide utilities

Import the additional stylesheet:

```ts
import 'element-plus/theme-chalk/display.css'
```

Available classes: `hidden-xs-only`, `hidden-sm-only`, `hidden-sm-and-down`, `hidden-sm-and-up`, `hidden-md-only`, `hidden-md-and-down`, `hidden-md-and-up`, `hidden-lg-only`, `hidden-lg-and-down`, `hidden-lg-and-up`, `hidden-xl-only`.

Test near 768, 992, 1200, and 1920px for unexpected wrapping and offsets. For application page chrome use the Container components; this skill addresses the Row/Col grid.

## Versioned sources

Validated against Element Plus **2.14.6**. Use the release sources below when checking details; the upstream `dev` branch can contain unreleased changes.

- [docs/en-US/component/layout.md](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/layout.md)
- [packages/components/row/src/row.ts](https://github.com/element-plus/element-plus/blob/2.14.6/packages/components/row/src/row.ts)
- [packages/components/col/src/col.ts](https://github.com/element-plus/element-plus/blob/2.14.6/packages/components/col/src/col.ts)
- [packages/theme-chalk/src/common/var.scss](https://github.com/element-plus/element-plus/blob/2.14.6/packages/theme-chalk/src/common/var.scss)
- [packages/theme-chalk/src/display.scss](https://github.com/element-plus/element-plus/blob/2.14.6/packages/theme-chalk/src/display.scss)
