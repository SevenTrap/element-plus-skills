---
name: "el-skeleton"
description: "Skeleton component for loading placeholders. Invoke when user needs to display loading states, content placeholders, or improve perceived loading performance."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Loading placeholders

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- `loading` is a boolean prop, default true; Skeleton has no `v-model`. Default-slot content appears when loading finishes.
- Use `#template` and `ElSkeletonItem` variants to match the final layout and reduce layout shifts. `rows` affects only the built-in template, whose first title row is additional to the requested rows.
- `count` repeats the template. `animated` enables shimmer. `throttle` accepts a number or `{ leading, trailing, initVal }` to tune transitions and initial loading behavior.
- Keep data loading/error handling outside the visual skeleton; reserve its dimensions to match loaded content.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElButton, ElSkeleton, ElSkeletonItem } from 'element-plus'
const loading = ref(true)
</script>

<template>
  <el-button @click="loading = !loading">Toggle loading</el-button>
  <el-skeleton :loading="loading" animated style="width: 240px">
    <template #template><el-skeleton-item variant="text" /></template>
    <template #default><p>Loaded content</p></template>
  </el-skeleton>
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/skeleton.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/skeleton) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/skeleton/loading-state.vue).
