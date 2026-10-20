---
name: "el-datetime-picker"
description: "DateTimePicker component for selecting date and time together. Invoke when user needs to select both date and time in a single picker."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# DateTimePicker

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

This is a mode of el-date-picker, not an el-datetime-picker component. Use type="datetime" or "datetimerange". Default models are Date or a pair of Dates; value-format changes serialization while format changes display. default-time takes Date objects, not time strings. Use disabled-date/disabled-hours and verify the callbacks for range endpoints. See the related DatePicker skill for the underlying component.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-date-picker v-model="date" type="datetime" format="YYYY-MM-DD HH:mm:ss" value-format="YYYY-MM-DD HH:mm:ss" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
const date = ref<string | null>('2026-10-20 12:00:00')
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- See [DatePicker](../el-date-picker/SKILL.md) for the underlying component.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/date-picker) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/datetime-picker.md).
