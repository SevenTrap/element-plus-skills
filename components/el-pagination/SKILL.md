---
name: "el-pagination"
description: "Pagination component for splitting large datasets into pages. Invoke when user needs to display paginated data, navigate through pages, or control page size and current page."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Controlled pagination

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Use numeric `v-model:current-page` and `v-model:page-size`. Pages are one-based. Supply `total` (item count) or `page-count` (page count); `page-count` takes precedence.
- A supplied `current-page` requires an update listener. When `sizes` is in the layout, controlled page size also needs an update listener; use the named models to satisfy these contracts.
- Use `total` when page sizes can change. `layout` is comma-separated (`total, sizes, prev, pager, next, jumper`); `->` aligns subsequent controls to the right.
- Pagination changes state, not the dataset: slice local data or fetch the requested server page. Avoid fetching twice through both model watchers and change handlers.
- Use `size="small"`; the `small` boolean is deprecated. `pager-count` must be an odd integer between 5 and 21.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElPagination } from 'element-plus'
const page = ref(1)
const pageSize = ref(20)
</script>

<template>
  <el-pagination v-model:current-page="page" v-model:page-size="pageSize"
    :total="200" :page-sizes="[20, 50, 100]"
    layout="total, sizes, prev, pager, next, jumper" />
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/pagination.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/pagination) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/pagination/more-elements.vue).
