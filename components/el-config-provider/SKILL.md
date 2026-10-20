---
name: "el-config-provider"
description: "ConfigProvider component for global configuration. Invoke when user needs to configure global settings, i18n, theme, or component defaults."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Config Provider

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Wrap the intended subtree; this provider has no model or layout DOM wrapper. Import real Element Plus locale objects and the matching Day.js locale for date formatting. namespace must match the CSS build. size/z-index configure descendant defaults. empty-values/value-on-clear affect supported inputs; use a function returning undefined if undefined is the intended clear result. Check each configuration object's actual shape.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-config-provider :locale="zhCn" size="small"><el-date-picker v-model="date" /></el-config-provider>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import zhCn from 'element-plus/es/locale/lang/zh-cn'
import 'dayjs/locale/zh-cn'
const date = ref<Date>()
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/config-provider) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/config-provider.md).
