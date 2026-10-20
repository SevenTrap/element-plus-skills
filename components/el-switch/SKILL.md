---
name: "el-switch"
description: "Switch component for toggling between two opposing states. Invoke when user needs to enable/disable features, toggle settings, or switch between on/off states."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Binary switches

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Default `v-model` is boolean. Custom `active-value` and `inactive-value` can be strings or numbers; the model must exactly match one of them.
- `before-change` returns boolean or `Promise<boolean>`; false or a rejected Promise blocks the change. Use `loading` while checking asynchronously and provide error feedback.
- `active-text`/`inactive-text`, action icons, and action slots customize the control. Use `inline-prompt` to place text/icons inside it.
- Use `aria-label` instead of deprecated `label`. Use CSS variables `--el-switch-on-color`, `--el-switch-off-color`, and `--el-switch-border-color` instead of deprecated color props.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElSwitch } from 'element-plus'
const enabled = ref(false)
const loading = ref(false)
const beforeChange = async () => {
  loading.value = true
  try {
    await Promise.resolve()
    return true
  } finally {
    loading.value = false
  }
}
</script>

<template><el-switch v-model="enabled" :loading="loading" :before-change="beforeChange" aria-label="Enabled" /></template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/switch.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/switch) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/switch/prevent-switching.vue).
