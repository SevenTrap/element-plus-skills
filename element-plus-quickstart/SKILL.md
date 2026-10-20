---
name: "element-plus-quickstart"
description: "Install and configure Element Plus 2.14.6 in Vue 3, choosing full, automatic, or manual imports and the matching style pipeline."
metadata:
  author: jiaiyan
  version: "1.0.0"
  element-plus-version: "2.14.6"
---

# Element Plus quick start

Target **Element Plus 2.14.6**. Inspect the project's existing bundler and import strategy before adding another style or component import pipeline.

```sh
npm install --save-exact element-plus@2.14.6
```

## Full import

```ts
import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'

createApp(App)
  .use(ElementPlus, { size: 'small', zIndex: 3000 })
  .mount('#app')
```

`size` accepts `large`, `default`, or `small`; the initial popup z-index is 2000 when not configured. For global component type checking, merge `element-plus/global` into `compilerOptions.types` without discarding existing entries.

## Automatic on-demand import

```sh
npm install -D unplugin-vue-components unplugin-auto-import
```

Merge these plugins into the existing Vite config (keep its Vue plugin):

```ts
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'

export default defineConfig({
  plugins: [
    vue(),
    AutoImport({ resolvers: [ElementPlusResolver()] }),
    Components({ resolvers: [ElementPlusResolver()] }),
  ],
})
```

`Components` resolves template components; `AutoImport` resolves APIs such as `ElMessage`. The resolver imports component styles as well. Do not also add full `dist/index.css` unless the project deliberately wants all styles. External plugin versions are separate from the Element Plus release; keep compatible versions in the project lockfile.

For Webpack use the same plugins from `/webpack` rather than `/vite`.

## Explicit component imports

```vue
<script setup lang="ts">
import { ElButton } from 'element-plus'
import 'element-plus/es/components/button/style/css'
</script>

<template>
  <ElButton type="primary">Save</ElButton>
</template>
```

Alternatively install `unplugin-element-plus` and add `ElementPlus()` from `unplugin-element-plus/vite` to automate styles for explicit imports. Choose one coherent style pipeline. Use `ElConfigProvider` for global settings in an on-demand setup:

```vue
<template>
  <el-config-provider size="small" :z-index="3000">
    <router-view />
  </el-config-provider>
</template>
```

## Nuxt and environment checks

Use `@element-plus/nuxt` in `modules` for Nuxt; its version is independent of Element Plus. The official quick-start notes that pnpm/Nuxt may require explicit `dayjs` installation or hoisting when dependency conversion fails. Prefer fixing the actual dependency issue over changing unrelated package-manager settings.

2.14.6 requires Sass >= 1.79.0 when compiling source styles. It does not support IE. Confirm installed package version, render a button, and verify popup styling and generated types before declaring setup complete.

## Versioned sources

Validated against Element Plus **2.14.6**. Use the release sources below when checking details; the upstream `dev` branch can contain unreleased changes.

- [docs/en-US/guide/quickstart.md](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/guide/quickstart.md)
- [docs/en-US/guide/installation.md](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/guide/installation.md)
