---
name: "el-calendar"
description: "Calendar component for displaying dates. Invoke when user needs to display a calendar view, select dates, or show scheduled events."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Calendar

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

v-model is a Date, not a formatted string; there is no value-format. date-cell receives data with date, day, type, and isSelected. range is a two-Date array subject to calendar week/month restrictions. controller-type="select" and its formatter are available in 2.14.6.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-calendar v-model="date" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
const date = ref(new Date())
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/calendar) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/calendar.md).
