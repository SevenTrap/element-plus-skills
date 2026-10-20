---
name: "el-progress"
description: "Progress component for showing operation progress and status. Invoke when user needs to display upload progress, task completion, or loading states."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Progress indicators

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Pass numeric `percentage` in the inclusive range 0–100; Progress is display-only and has no `v-model`.
- Choose `type="line"`, `circle`, or `dashboard`. `status` is `success`, `exception`, or `warning`; it does not use the Button error/danger vocabulary.
- `text-inside` applies to line progress; use enough `stroke-width` for its label. For circular variants use `width` for diameter.
- `color` accepts a string, percentage-to-color function, or threshold array. `indeterminate` animates an unknown amount of work; `duration` controls that animation, not completion.
- `format(percentage)` customizes text; the default slot supports richer content.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ElProgress } from 'element-plus'
const format = (value: number) => value === 100 ? 'Complete' : `${value}%`
</script>

<template><el-progress :percentage="60" :format="format" /></template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/progress.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/progress) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/progress/linear-progress-bar.vue).
