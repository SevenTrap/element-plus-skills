---
name: "el-message"
description: "Message notification component for displaying feedback messages. Invoke when user needs to show success, warning, error, or info messages."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Feedback service

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Import `ElMessage` for Composition API; call `ElMessage(options)` or `ElMessage.success(message)`. It is a service, without `v-model`.
- Types include `primary`, `success`, `warning`, `info`, and `error`. The default type is `info`, duration is 3000 ms; `duration: 0` persists until closed.
- Keep the returned handler to call `close()`; `ElMessage.closeAll()` closes all instances. `grouping: true` merges matching message content.
- `placement` is supported in this version. Use the API reference for its allowed values, rather than Notification's `position` option.
- Pass `appContext` as the second argument when a locally imported service needs application providers. Never enable `dangerouslyUseHTMLString` for untrusted text.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ElButton, ElMessage } from 'element-plus'
const notify = () => ElMessage.success({ message: 'Saved', showClose: true })
</script>

<template><el-button @click="notify">Save</el-button></template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/message.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/message) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/message/basic.vue).
