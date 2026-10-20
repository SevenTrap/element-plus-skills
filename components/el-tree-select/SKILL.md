---
name: "el-tree-select"
description: "TreeSelect component combining Tree and Select functionality. Invoke when user needs to select from hierarchical data in a dropdown, like organization structures or category trees."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Tree-backed select inputs

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- TreeSelect combines Select and Tree. Single mode binds a node key; `multiple` binds key arrays. It cannot bind whole option objects as standard Select can.
- The default value field is `value`; set `node-key` for another unique identifier. Keys must be unique across the whole tree. `props` maps labels/children/disabled fields.
- Default selection targets leaves; `check-strictly` permits selecting any level. `show-checkbox` enables checking; leaf text is checkable by default through `check-on-click-leaf`.
- Lazy loading follows Tree's `load` contract. `cache-data` supplies labels for selected nodes whose data has not loaded yet.
- Direct forwarded Tree/Select methods are deprecated for 3.0.0. In 2.14.6 the actual exposed instance names are `treeRef` and `selectRef`: use `treeSelectRef.value?.treeRef.getCheckedKeys()` or `.selectRef.focus()` after mount. The source/types take precedence over prose mentioning `tree`/`select`.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElTreeSelect } from 'element-plus'
const selected = ref<number[]>([2])
const data = [{ id: 1, label: 'Group', children: [{ id: 2, label: 'Item' }] }]
</script>

<template>
  <el-tree-select v-model="selected" :data="data" node-key="id" multiple
    show-checkbox default-expand-all style="width: 240px" />
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/tree-select.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/tree-select) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/tree-select/node-key.vue).
