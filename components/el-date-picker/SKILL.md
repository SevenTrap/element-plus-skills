---
name: "el-date-picker"
description: "DatePicker component for date input. Invoke when user needs to select dates, date ranges, months, years, or datetime values."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# DatePicker

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Without value-format the model emits Date values; format changes display only. Single types bind one value, plural dates/months/years/quarters bind arrays, and ranges bind two values. Accept empty/clear results. quarter/quarters/quarterrange are supported since 2.14.5. Use Day.js case-sensitive tokens: YYYY-MM-DD, HH:mm:ss. default-value controls the initial view, not selection; default-time takes a Date or pair. disabled-date returns true to block a date.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-date-picker v-model="date" type="date" format="YYYY-MM-DD" value-format="YYYY-MM-DD" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
const date = ref<string | null>('2026-10-20')
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/date-picker) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/date-picker.md).
