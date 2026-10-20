---
name: "element-plus-ssr"
description: "Integrate Element Plus 2.14.6 with Vue SSR or Nuxt, ensuring stable IDs, z-index initialization, and correct teleport hydration."
metadata:
  author: jiaiyan
  version: "1.0.0"
  element-plus-version: "2.14.6"
---

# Element Plus SSR

Target **Element Plus 2.14.6**. Nuxt projects can use `@element-plus/nuxt` to handle Element Plus SSR integration; inspect the module version and existing configuration before adding manual equivalents.

## Per-app initialization

Create a fresh application and injection objects for each server request. Initialize equivalent objects on the client before hydration:

```ts
// app.ts, shared by server and client
import { createSSRApp } from 'vue'
import ElementPlus, { ID_INJECTION_KEY, ZINDEX_INJECTION_KEY } from 'element-plus'
import App from './App.vue'

export function createApp() {
  const app = createSSRApp(App)
  app.use(ElementPlus)
  app.provide(ID_INJECTION_KEY, { prefix: 1024, current: 0 })
  app.provide(ZINDEX_INJECTION_KEY, { current: 0 })
  return app
}
```

Use the same `prefix` and starting counters on server and client; if multiple apps share one page, give each app a different stable prefix. Do not share an injection object across requests. `ZINDEX_INJECTION_KEY` is the increasing counter, separate from the configured base z-index (2000 by default). Import styles through the bundler's client entry or existing SSR style pipeline.

```ts
// entry-client.ts
import { createApp } from './app'
createApp().mount('#app')
```

The server renders a new app from `createApp()` with `renderToString`. Keep initial route, locale, theme, and data consistent with client hydration.

## Teleports

Dialog, Drawer, Tooltip, Dropdown, Select, and date picker overlays may teleport. Choose according to whether their initial content must be server rendered:

- Client-only overlay rendering is simplest when SSR content is unnecessary. In Nuxt use `ClientOnly`; in Vue guard with a flag set in `onMounted`.
- To preserve SSR overlay content, collect the render context's teleports and insert each in its actual target in the HTML document.

```vue
<script setup lang="ts">
import { onMounted, ref } from 'vue'
const mounted = ref(false)
onMounted(() => { mounted.value = true })
</script>

<template>
  <el-tooltip v-if="mounted" content="Help">
    <el-button>Help</el-button>
  </el-tooltip>
</template>
```

For the default `el` namespace, popper container targets start with `#el-popper-container-`. A server adapter can construct their wrappers from the renderer's own teleport output:

```ts
function renderTeleports(teleports?: Record<string, string>) {
  if (!teleports) return ''
  return Object.entries(teleports).reduce((html, [target, content]) => {
    if (target.startsWith('#el-popper-container-')) {
      return `${html}<div id="${target.slice(1)}">${content}</div>`
    }
    return html
  }, teleports.body || '')
}
```

Insert the result next to the app root inside `<body>`, as in the pinned SSR guide. Do not interpolate arbitrary user-provided target selectors into this helper. Custom `namespace` or `append-to` values require corresponding target handling; other targets must also be rendered explicitly. Rendering only `#app` and ignoring `ctx.teleports` loses overlay markup.

Verify the production SSR build by loading directly into an overlay-containing route and checking hydration warnings, matching IDs, open/close behavior, and repeated requests. Client-only guards should cover only components that need them.

## Versioned sources

Validated against Element Plus **2.14.6**. Use the release sources below when checking details; the upstream `dev` branch can contain unreleased changes.

- [docs/en-US/guide/ssr.md](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/guide/ssr.md)
- [packages/hooks/use-id/index.ts](https://github.com/element-plus/element-plus/blob/2.14.6/packages/hooks/use-id/index.ts)
- [packages/hooks/use-z-index/index.ts](https://github.com/element-plus/element-plus/blob/2.14.6/packages/hooks/use-z-index/index.ts)
- [packages/hooks/use-popper-container/index.ts](https://github.com/element-plus/element-plus/blob/2.14.6/packages/hooks/use-popper-container/index.ts)
