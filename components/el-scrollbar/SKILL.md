---
name: "el-scrollbar"
description: "Scrollbar component for custom scrollbars. Invoke when user needs to replace native scrollbars, create custom scroll areas, or implement infinite scrolling."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Custom scroll containers

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Give `ElScrollbar` a `height` for a fixed viewport or `max-height` to grow until content overflows. Without constrained dimensions it may not scroll.
- It has no `v-model`; use `scroll` payload `{ scrollTop, scrollLeft }` and exposed `scrollTo`, `setScrollTop`, or `setScrollLeft` for synchronization.
- `native` uses the native scrollbar. `always` controls custom-bar visibility; `noresize` disables resize observation, so call `update()` when dimensions change.
- `end-reached(direction)` and `distance` support loading at scroll boundaries. Guard concurrent loads and exhausted results in application code.
- The `mask` property and scroll-mask CSS variables on later dev revisions are not part of 2.14.6.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ElScrollbar } from 'element-plus'
</script>

<template>
  <el-scrollbar height="200px">
    <p v-for="item in 20" :key="item" style="height: 40px">Item {{ item }}</p>
  </el-scrollbar>
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/scrollbar.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/scrollbar) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/scrollbar/basic-usage.vue).
