---
name: "el-select-v2"
description: "Virtualized Select component for large datasets. Invoke when user needs to select from thousands of options with virtual scrolling for performance."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Virtualized select inputs

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Use `ElSelectV2` with an `options` array; do not copy the child `ElOption` structure of standard Select. This is the virtualized select, marked beta in the official docs.
- Single selection uses one value; `multiple` uses an array. For object values, `value-key` identifies the object, while `props` maps option label/value/disabled fields.
- `item-height` controls fixed option height (default 34); `estimated-option-height` supports dynamic-height virtualization. Custom option rendering must match the chosen sizing strategy.
- Remote search requires `filterable`, `remote`, `remote-method`, and application-managed loading/results. `allow-create` requires filtering.
- Configure `empty-values`/`value-on-clear` for clear behavior. Prefer `teleported` and `append-to`; `popper-append-to-body` is deprecated. `end-reached` exists in 2.14.6.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElSelectV2 } from 'element-plus'
const selected = ref('option-0')
const options = Array.from({ length: 1000 }, (_, index) => ({
  value: `option-${index}`, label: `Option ${index + 1}`,
}))
</script>

<template><el-select-v2 v-model="selected" :options="options" filterable style="width: 240px" /></template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/select-v2.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/select-v2) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/select-v2/basic-usage.vue).
