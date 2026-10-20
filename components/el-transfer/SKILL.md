---
name: "el-transfer"
description: "Transfer component for dual-column list selection. Invoke when user needs to move items between two lists, select multiple items from a large dataset, or manage permissions."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Dual-list transfers

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- `data` contains uniquely keyed options with `key`, `label`, and optional `disabled`. Bind `v-model` to an array of keys on the right panel, not option objects or checkbox state.
- `props` maps custom data fields. `left-default-checked` and `right-default-checked` initialize panel checkbox states without transferring items.
- `filterable` enables panel searching; `filter-method(query, item)` decides matches. `change(value, direction, movedKeys)` describes completed transfers.
- `target-order` controls right-panel ordering. Use scoped content or `render-content` for custom option labels.
- `virtual-scroll` and `item-size` are available since 2.14.3; match fixed item height to rendered option height. The default item size is 30px.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElTransfer } from 'element-plus'
const selected = ref<number[]>([1])
const options = Array.from({ length: 2000 }, (_, index) => ({
  key: index + 1, label: `Option ${index + 1}`, disabled: index % 4 === 3,
}))
</script>

<template>
  <el-transfer v-model="selected" :data="options" filterable virtual-scroll :item-size="30" />
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/transfer.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/transfer) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/transfer/virtual-scroll.vue).
