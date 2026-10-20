---
name: "el-result"
description: "Result component for feedback on operation results. Invoke when user needs to display success, error, warning, or info result pages with custom content."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Operation result panels

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Use `ElResult` to present an operation outcome; it is display-only with no `v-model`.
- Set `icon` to `primary`, `success`, `warning`, `error`, or `info`. Supply `title` and `sub-title`, or their named slots.
- The `icon` slot replaces the built-in status graphic. Put navigation/retry buttons in `extra` and wire their actions in application code.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ElButton, ElResult } from 'element-plus'
const refresh = () => window.location.reload()
</script>

<template>
  <el-result icon="success" title="Saved" sub-title="Your changes are ready.">
    <template #extra><el-button @click="refresh">Refresh</el-button></template>
  </el-result>
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/result.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/result) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/result/basic-usage.vue).
