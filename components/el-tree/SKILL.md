---
name: "el-tree"
description: "Tree component for displaying hierarchical data with selection, filtering, and drag-drop support. Invoke when user needs to display folder structures, organization charts, category trees, or any hierarchical data with expandable nodes."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Hierarchical trees

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Use `data` with `props` mappings for label/children/disabled fields. Tree has no ordinary `v-model`; track selected/checked nodes with events and instance methods.
- Set a unique `node-key` across the entire tree before using key-based defaults, selection methods, or structural updates. Defaults initialize state; use exposed methods for later programmatic changes.
- `show-checkbox` enables checks; `check-strictly` decouples parent/child checking. `check-on-click-leaf` defaults to true, so clicking leaf text can check it even when `check-on-click-node` is false.
- Filtering requires both `filter-node-method(value, data, node)` and `treeRef.filter(value)`; setting a filter prop alone does not execute filtering.
- `lazy` uses `load(node, resolve, reject)`. Resolve with child data; `reject()` preserves the ability to retry failed loading. Use the `isLeaf` mapping when leaf status is known.
- Drag/drop uses `allow-drag`/`allow-drop` to constrain actions. Default scoped slots receive `{ node, data }`; the Node wrapper differs from raw data.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ElTree } from 'element-plus'
const data = [{ id: 1, label: 'Project', children: [{ id: 2, label: 'Task' }] }]
</script>

<template>
  <el-tree :data="data" node-key="id" show-checkbox :default-expanded-keys="[1]"
    :default-checked-keys="[2]" :check-on-click-leaf="false" />
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/tree.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/tree) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/tree/default-state.vue).
