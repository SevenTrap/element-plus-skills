---
name: "el-collapse"
description: "Collapse component for storing expandable content. Invoke when user needs to create accordion panels, FAQ sections, or collapsible content areas."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Collapse

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Normal v-model is an array of item names; accordion mode uses one string or number. Give items stable explicit names. before-collapse may return false or a rejected Promise to block a change. title/icon slots customize headers. Collapse does not provide virtual scrolling.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-collapse v-model="active" accordion><el-collapse-item title="Details" name="details">Details</el-collapse-item><el-collapse-item title="History" name="history">History</el-collapse-item></el-collapse>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const active = ref('details')
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/collapse) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/collapse.md).
