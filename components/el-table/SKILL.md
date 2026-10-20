---
name: "el-table"
description: "Table component for displaying data with sorting, filtering, selection, and pagination. Invoke when user needs to display tabular data or implement data grid functionality."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Standard data tables

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Compose `ElTable :data="rows"` with `ElTableColumn` definitions. `prop` reads a row field; `#default="{ row, column, $index }"` renders cells. There is no whole-table `v-model`.
- Use stable unique `row-key` for tree data and reserved selection. `type="selection"` adds checkboxes; track `selection-change`. `reserve-selection` belongs on the selection column.
- `sortable` sorts locally; `sortable="custom"` emits `sort-change` for server sorting. Server filtering similarly needs application-managed data. Set `column-key` for identifying filter changes.
- `height` fixes the scrollable viewport; `max-height` caps it. When container layout changes while hidden, call exposed `doLayout()` after showing it if needed.
- Tree rows use `children`/`hasChildren` or `tree-props` mappings. Lazy trees require `lazy`, `load`, and `row-key`.
- `toggleRowSelection(row, selected?, ignoreSelectable = true)` may bypass `selectable`; pass false to respect it. `getHalfSelectionRows()` is available since 2.14.2. Do not replace normal Table APIs with Table V2 column configuration.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ElTable, ElTableColumn } from 'element-plus'
const rows = [{ id: 1, name: 'Ada', status: 'Ready' }, { id: 2, name: 'Lin', status: 'Pending' }]
</script>

<template>
  <el-table :data="rows" row-key="id" style="width: 100%">
    <el-table-column prop="name" label="Name" sortable />
    <el-table-column prop="status" label="Status" />
  </el-table>
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/table) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/table/basic.vue).
