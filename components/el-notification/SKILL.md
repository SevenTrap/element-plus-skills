---
name: "el-notification"
description: "Notification component for displaying notification messages at the corner of the page. Invoke when user needs to show persistent notifications with custom content."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Corner notification service

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Call imported `ElNotification(options)` or a typed helper such as `.success(options)`; there is no `v-model`. The returned handler has `close()`; `.closeAll()` closes all notifications.
- `position` is `top-right` (default), `top-left`, `bottom-right`, or `bottom-left`. Default duration is 4500 ms; zero disables automatic closing.
- `progress: true` or a Progress-options object enables the countdown bar (2.14.4); `pauseOnHover` defaults to true. The progress object excludes `percentage`, `type`, `duration`, `indeterminate`, and `width`.
- `message` accepts text, VNodes, or a VNode factory. Do not pass untrusted HTML with `dangerouslyUseHTMLString`.
- Pass application context as the second argument for local imports requiring providers. Keep offsets consistent for concurrent instances; `updateOffsets(position)` recalculates their positions.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ElButton, ElNotification } from 'element-plus'
const notify = () => ElNotification({
  title: 'Saved', message: 'Your changes are ready.', type: 'success',
  duration: 6000, progress: true, pauseOnHover: true,
})
</script>

<template><el-button @click="notify">Show notification</el-button></template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/notification.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/notification) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/notification/progress-bar.vue).
