---
name: "el-select"
description: "Select dropdown component for single or multiple selection with filtering, remote search, and grouping. Invoke when user needs dropdown selection functionality."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Standard select inputs

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Bind a scalar for single selection and an array for `multiple`. Options support string, number, boolean, and object values; use an explicit unique `value-key` for object values.
- Declare `ElOption` children or pass `options` with optional `props` mappings. `ElOptionGroup` supplies grouped children. Give the select a usable width in flex/inline layouts.
- `filterable` enables local filtering. Remote search needs `remote`, `filterable`, `remote-method`, and controlled `loading`/options. Guard stale responses.
- `allow-create` requires `filterable`. `empty-values` and `value-on-clear` determine whether empty string is a selectable value and what clearing emits.
- `end-reached(direction)` is available since 2.14.0. `suffix-transition` is deprecated; do not introduce it in new examples.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElOption, ElSelect } from 'element-plus'
const selected = ref('one')
const options = [{ value: 'one', label: 'One' }, { value: 'two', label: 'Two' }]
</script>

<template>
  <el-select v-model="selected" filterable style="width: 240px">
    <el-option v-for="option in options" :key="option.value" v-bind="option" />
  </el-select>
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/select.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/select) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/select/basic-usage.vue).
