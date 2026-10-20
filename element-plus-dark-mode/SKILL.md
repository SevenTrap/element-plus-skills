---
name: "element-plus-dark-mode"
description: "Enable or customize Element Plus 2.14.6 dark mode through html.dark, dark CSS variables, or Sass overrides."
metadata:
  author: jiaiyan
  version: "1.0.0"
  element-plus-version: "2.14.6"
---

# Element Plus dark mode

Target **Element Plus 2.14.6**. Dark mode requires both the dark variable stylesheet and a `dark` class on the HTML element.

```ts
// App entry: also keep the project's regular component styles.
import 'element-plus/theme-chalk/dark/css-vars.css'
```

```html
<html class="dark">
```

Dark mode changes Element Plus variables. Custom application surfaces should consume those variables to participate:

```css
body {
  color: var(--el-text-color-primary);
  background: var(--el-bg-color-page);
}
```

## Toggle

If the project already uses VueUse, `useDark` with `useToggle` provides preference persistence and system preference handling:

```vue
<script setup lang="ts">
import { useDark, useToggle } from '@vueuse/core'
const isDark = useDark()
const toggleDark = useToggle(isDark)
</script>

<template>
  <button @click="toggleDark()">Toggle theme</button>
</template>
```

A simple client-side toggle can instead call `document.documentElement.classList.toggle('dark')`. Do not access `document` while server rendering. For SSR, synchronize the initial theme before first paint and hydrate using the same preference to prevent flashes and markup mismatches.

## Custom CSS

Import overrides after the dark stylesheet, with matching selector specificity:

```css
html.dark {
  --el-bg-color-page: #0a0a0a;
  --el-bg-color: #181a20;
  --el-bg-color-overlay: #20232b;
}
```

Unmodified 2.14.6 dark backgrounds are page `#0a0a0a`, base `#141414`, overlay `#1d1e1f`. Dark shades are generated differently from light mode; do not paste the light palette into `html.dark` expecting the same contrast.

## Custom Sass

Configure variables before compiling the dark CSS output. Forwarding variables alone emits no theme stylesheet:

```scss
@forward 'element-plus/theme-chalk/src/dark/var.scss' with (
  $bg-color: (
    'page': #0a0a0a,
    '': #181a20,
    'overlay': #20232b,
  )
);
@use 'element-plus/theme-chalk/src/dark/css-vars.scss' as *;
```

Import this custom output instead of the precompiled dark CSS; use Sass >= 1.79.0. Check custom colors, disabled states, borders, and teleported popups in both modes.

## Versioned sources

Validated against Element Plus **2.14.6**. Use the release sources below when checking details; the upstream `dev` branch can contain unreleased changes.

- [docs/en-US/guide/dark-mode.md](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/guide/dark-mode.md)
- [packages/theme-chalk/src/dark/var.scss](https://github.com/element-plus/element-plus/blob/2.14.6/packages/theme-chalk/src/dark/var.scss)
- [packages/theme-chalk/src/dark/css-vars.scss](https://github.com/element-plus/element-plus/blob/2.14.6/packages/theme-chalk/src/dark/css-vars.scss)
