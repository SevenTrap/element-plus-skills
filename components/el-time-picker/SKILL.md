---
name: "el-time-picker"
description: "TimePicker component for time input. Invoke when user needs to select time values, time ranges, or limit time selections."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Arbitrary time selection

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Without `value-format`, the selected value is a Date; `is-range` uses a two-element pair. The public model also accepts timestamps/strings; initialize it to match the chosen format and allow clearing.
- `format` controls display only. `value-format` changes serialization, using Dayjs tokens with case-sensitive hours/minutes/seconds. Do not confuse display format with the model type.
- `disabled-hours`, `disabled-minutes`, and `disabled-seconds` return arrays of unavailable numeric units. Their range-role arguments support different start/end constraints.
- `arrow-control` uses arrows instead of scrolling. Bind `v-model` for selection; `change` reflects committed edits, and `visible-change` reports panel visibility.
- Use `aria-label`; the old `label` alias is deprecated. For fixed interval choices use the separate TimeSelect component.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElTimePicker } from 'element-plus'
const time = ref<string | null>('09:30:00')
</script>

<template>
  <el-time-picker v-model="time" format="HH:mm" value-format="HH:mm:ss" aria-label="Start time" />
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/time-picker.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/time-picker) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/time-picker/basic.vue).
