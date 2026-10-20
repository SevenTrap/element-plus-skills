---
name: "el-time-select"
description: "TimeSelect component for selecting from fixed time options. Invoke when user needs to select from predefined time slots or schedule times."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Fixed-interval time selection

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- `ElTimeSelect` offers discrete string times. Bind `string | null` rather than Date objects; use TimePicker for arbitrary time selection.
- `start`, `end`, and `step` define available choices, typically `HH:mm`; `format` controls display. Tokens are case-sensitive (`HH` for 24-hour clock, `mm` for minutes).
- `min-time` and `max-time` disable choices outside the permitted interval; `include-end-time` includes the end choice even when interval stepping does not land on it.
- For dependent start/end fields, bind the later field's `min-time` to the selected start time and validate the final interval in application code.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElTimeSelect } from 'element-plus'
const time = ref('')
</script>

<template>
  <el-time-select v-model="time" start="08:30" end="18:30" step="00:15"
    placeholder="Select time" style="width: 240px" />
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/time-select.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/time-select) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/time-select/basic.vue).
