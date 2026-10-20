---
name: "element-plus-theming"
description: "Customize Element Plus 2.14.6 themes with Sass maps or CSS variables, including correct full and on-demand style compilation."
metadata:
  author: jiaiyan
  version: "1.0.0"
  element-plus-version: "2.14.6"
---

# Element Plus theming

Target **Element Plus 2.14.6**. Choose CSS variables for runtime or isolated changes and Sass for generating a complete consistent theme. Default tokens below assume the `el` namespace.

## Runtime overrides

Load overrides after Element Plus styles. A single primary override does not regenerate precompiled light/dark variants, so update the relevant palette variables too when changing a brand at runtime.

```css
:root {
  --el-color-primary: #008060;
  --el-color-primary-light-3: #4da690;
  --el-color-primary-light-5: #80c0b0;
  --el-color-primary-light-7: #b3d9cf;
  --el-color-primary-light-8: #cce6df;
  --el-color-primary-light-9: #e6f2ef;
  --el-color-primary-dark-2: #00664d;
}

.special-tag { --el-tag-bg-color: #ecf5ff; }
```

Use component variables locally where practical. Teleported overlays may not inherit variables from a local wrapper; apply the theme at an appropriate ancestor or to the overlay's actual target/class. Browser-only runtime updates can use `element.style.setProperty('--el-color-primary', value)`.

## Sass: full styles

Use Sass >= 1.79.0 and Sass modules. Configure maps before Element Plus first loads them:

```scss
// src/styles/element.scss
@forward 'element-plus/theme-chalk/src/common/var.scss' with (
  $colors: (
    'primary': ('base': #008060),
  )
);
@use 'element-plus/theme-chalk/src/index.scss' as *;
```

Import this file in the app entry instead of the built `element-plus/dist/index.css`. Source maps also include `$text-color`, `$border-color`, `$fill-color`, `$bg-color`, `$border-radius`, and component maps such as `$button`; inspect the pinned source for valid keys. Do not use Element UI's old `$--color-primary` syntax.

## Sass: on-demand styles

Keep a variables-only file to avoid emitting the entire stylesheet into each component:

```scss
// src/styles/element-variables.scss
@forward 'element-plus/theme-chalk/src/common/var.scss' with (
  $colors: ('primary': ('base': #008060))
);
```

Inject that file into SCSS compilation using the existing Vite configuration:

```ts
css: {
  preprocessorOptions: {
    scss: {
      additionalData: '@use "@/styles/element-variables.scss" as *;',
    },
  },
},
```

The `@` alias must already resolve to `src`. Choose the source-style setting matching the importer:

- `ElementPlusResolver({ importStyle: 'sass' })` for `unplugin-vue-components` (and the corresponding auto-import resolver).
- `ElementPlus({ useSource: true })` for `unplugin-element-plus` and explicit component imports.

Do not import compiled CSS afterward, which can override the custom theme. Test button normal/hover/active states and an overlay; configure dark variables separately when dark mode is enabled.

## Versioned sources

Validated against Element Plus **2.14.6**. Use the release sources below when checking details; the upstream `dev` branch can contain unreleased changes.

- [docs/en-US/guide/theming.md](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/guide/theming.md)
- [docs/en-US/guide/installation.md](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/guide/installation.md)
- [packages/theme-chalk/src/common/var.scss](https://github.com/element-plus/element-plus/blob/2.14.6/packages/theme-chalk/src/common/var.scss)
- [packages/theme-chalk/src/var.scss](https://github.com/element-plus/element-plus/blob/2.14.6/packages/theme-chalk/src/var.scss)
