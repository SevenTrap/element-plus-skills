---
name: "el-message-box"
description: "MessageBox component for modal dialogs simulating system alerts, confirms, and prompts. Invoke when user needs to show alert messages, confirm actions, or prompt for user input."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Alert, confirm, and prompt service

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Import `ElMessageBox`; use `.alert(message, title, options)`, `.confirm(...)`, or `.prompt(...)`. Complex forms belong in Dialog. There is no component `v-model`.
- Handle the returned Promise: confirmation resolves, cancellation/closing rejects. Prompt resolves with `{ value, action }`. Set `distinguishCancelAndClose` when these dismissal paths matter.
- `beforeClose(action, instance, done)` takes over closing; call `done()` when ready. Keep asynchronous business failures separate from user cancellation.
- `inputValidator` returns `true` for valid input or `false`/an error string for invalid input. `message` may be a VNode factory receiving `{ confirm, cancel, close }` (available since 2.14.0).
- Use trusted text/VNodes; raw HTML is unsafe for untrusted content. `confirmButtonType`/`cancelButtonType` accept supported Button types; `text` is deprecated.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ElButton, ElMessage, ElMessageBox } from 'element-plus'
const confirm = async () => {
  try {
    await ElMessageBox.confirm('Continue with this operation?', 'Confirm', {
      type: 'warning', distinguishCancelAndClose: true,
    })
    ElMessage.success('Confirmed')
  } catch (action) {
    if (action === 'cancel' || action === 'close') return
    throw action
  }
}
</script>

<template><el-button @click="confirm">Confirm operation</el-button></template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/message-box.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/message-box) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/message-box/confirm.vue).
