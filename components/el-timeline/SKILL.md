---
name: "el-timeline"
description: "Timeline component for visually displaying timeline activities. Invoke when user needs to display chronological events, activity history, or process logs."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Event timelines

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Compose `ElTimeline` with `ElTimelineItem` entries; it has no model and does not sort by timestamp. Supply entries in the intended order, or use `reverse` to reverse rendering.
- `mode` supports `start`, `alternate`, `alternate-reverse`, and `end`. Item timestamps are display text, not parsed dates.
- Item `placement` places timestamps above/below content. `hide-timestamp` hides them; the `dot` slot replaces the node graphic; render rich timestamps in item content when needed.
- Node `type` uses Button-style values including `danger`; use `color` for a custom color and an icon component for `icon`.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ElTimeline, ElTimelineItem } from 'element-plus'
const events = [
  { id: 1, time: '2026-10-19', text: 'Created' },
  { id: 2, time: '2026-10-20', text: 'Approved' },
]
</script>

<template>
  <el-timeline mode="alternate">
    <el-timeline-item v-for="event in events" :key="event.id" :timestamp="event.time">
      {{ event.text }}
    </el-timeline-item>
  </el-timeline>
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/timeline.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/timeline) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/timeline/mode.vue).
