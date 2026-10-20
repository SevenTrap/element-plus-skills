---
name: "el-segmented"
description: "Segmented component for single option selection from multiple options. Invoke when user needs to create radio-style button groups, tab-like controls, or option switches."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Segmented single selection

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Bind one `string | number | boolean` value. `options` may contain primitive values or objects with `label`, `value`, and `disabled`.
- Use `props` to map custom option field names. Keep option values unique and type-consistent with the model.
- `block` fills the available width, `direction="vertical"` stacks items, and `size` controls density.
- Customize the default scoped slot for icons/rich labels while preserving meaningful accessible text; use `aria-label` to name the control.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElSegmented } from 'element-plus'
const selected = ref('Mon')
const options = ['Mon', 'Tue', 'Wed']
</script>

<template><el-segmented v-model="selected" :options="options" aria-label="Day" /></template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/segmented.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/segmented) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/segmented/basic.vue).
