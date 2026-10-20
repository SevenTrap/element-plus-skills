---
name: "el-statistic"
description: "Statistic component for displaying numerical statistics. Invoke when user needs to display counts, amounts, rankings, or countdown timers."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Statistics and countdowns

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- `ElStatistic` formats a `value`; use `precision`, decimal/group separators, `prefix`/`suffix`, or a `formatter`. These are display components without `v-model`.
- `ElCountdown` counts down to an absolute timestamp or Dayjs value. Pass `Date.now() + duration`, not a number of remaining seconds.
- `format` uses Dayjs format tokens; bracket literal text. `change` reports remaining milliseconds and `finish` signals reaching zero.
- Use `title`, `prefix`, and `suffix` slots for rich markup. Keep time computation reactive only where needed; do not recreate the target on every render.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ElCountdown, ElStatistic } from 'element-plus'
const deadline = Date.now() + 60_000
</script>

<template>
  <el-statistic title="Orders" :value="12345" />
  <el-countdown title="Time remaining" :value="deadline" format="mm:ss" />
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/statistic.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/statistic) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/statistic/countdown.vue).
