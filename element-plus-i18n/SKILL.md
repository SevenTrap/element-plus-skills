---
name: "element-plus-i18n"
description: "Configure and switch Element Plus 2.14.6 component locales, including Day.js date localization and integration with app translations."
metadata:
  author: jiaiyan
  version: "1.0.0"
  element-plus-version: "2.14.6"
---

# Element Plus internationalization

Target **Element Plus 2.14.6**. Component strings default to English. Element Plus locales and application translations are separate systems.

## Global locale

For full registration:

```ts
import ElementPlus from 'element-plus'
import zhCn from 'element-plus/es/locale/lang/zh-cn'
import 'dayjs/locale/zh-cn'

app.use(ElementPlus, { locale: zhCn })
```

Import Day.js locale data separately for date/time components. Setting Element Plus locale alone does not bundle that data.

## Reactive locale with ConfigProvider

```vue
<script setup lang="ts">
import { computed, ref } from 'vue'
import { ElConfigProvider } from 'element-plus'
import en from 'element-plus/es/locale/lang/en'
import zhCn from 'element-plus/es/locale/lang/zh-cn'
import 'dayjs/locale/zh-cn'

const language = ref<'en' | 'zh-cn'>('en')
const locale = computed(() => language.value === 'zh-cn' ? zhCn : en)
</script>

<template>
  <button @click="language = language === 'en' ? 'zh-cn' : 'en'">Switch language</button>
  <ElConfigProvider :locale="locale">
    <router-view />
  </ElConfigProvider>
</template>
```

The `locale` prop takes a locale object, not a code string. Place the provider above consumers and load styles through the project's normal import strategy. For `vue-i18n`, derive the Element Plus object from the same application language using an explicit mapping. Map application `en-US` to Element Plus `en`, for example; do not assume every app code is a package filename.

For direct Day.js use outside Element Plus, set or pass its locale independently as needed. Avoid a shared per-user global Day.js locale during SSR; initialize request-specific application state consistently on server and client.

## CDN and custom messages

For a pinned CDN build, load `https://unpkg.com/element-plus@2.14.6/dist/locale/zh-cn.js` after the main build and pass `ElementPlusLocaleZhCn` to `app.use(ElementPlus, { locale: ... })`. Date/time locale data still needs its own setup.

For a small message override, preserve the complete locale shape:

```ts
const customZhCn = {
  ...zhCn,
  el: {
    ...zhCn.el,
    pagination: { ...zhCn.el.pagination, goto: '跳至' },
  },
}
```

Use the pinned locale directory as the supported-language inventory. Do not promise a locale merely because it exists on `dev`: Galician (`gl`) was added after 2.14.6 and is excluded here. Verify button/pagination strings and date picker month/day names after switching languages.

## Versioned sources

Validated against Element Plus **2.14.6**. Use the release sources below when checking details; the upstream `dev` branch can contain unreleased changes.

- [docs/en-US/guide/i18n.md](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/guide/i18n.md)
- [docs/en-US/component/config-provider.md](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/config-provider.md)
- [packages/locale/lang/en.ts](https://github.com/element-plus/element-plus/blob/2.14.6/packages/locale/lang/en.ts)
- [packages/locale/lang/zh-cn.ts](https://github.com/element-plus/element-plus/blob/2.14.6/packages/locale/lang/zh-cn.ts)
