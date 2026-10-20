---
name: "el-table-v2"
description: "Virtualized Table component for rendering massive data efficiently. Invoke when user needs to display large datasets with virtual scrolling for performance."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Virtualized data tables

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Use `ElTableV2` with `columns` and `data` arrays, not `ElTableColumn` children. It is a separate beta component and does not support every feature of standard Table.
- Supply numeric `width` and `height`. Each column needs `key`, `dataKey`, `title`, and `width`; rows need stable identifiers (default `row-key` is `id`).
- `row-height` controls fixed-height rows; `estimated-row-height` enables dynamic measurement. `ElAutoResizer` can provide viewport dimensions when its parent has a real size.
- Use renderers such as `cellRenderer` for custom cells. Sorting indicators (`sort-by`/`sort-state`) and sorting events do not sort data automatically; update a new data array in application code.
- Build selection/filter controls explicitly using renderer/event APIs; do not assume standard Table's selection-column or filter behavior exists here.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ElTableV2 } from 'element-plus'
const columns = [
  { key: 'name', dataKey: 'name', title: 'Name', width: 240 },
  { key: 'status', dataKey: 'status', title: 'Status', width: 200 },
]
const rows = Array.from({ length: 1000 }, (_, id) => ({
  id, name: `Person ${id}`, status: 'Ready',
}))
</script>

<template><el-table-v2 :columns="columns" :data="rows" :width="600" :height="400" /></template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/table-v2) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/table-v2/basic.vue).
