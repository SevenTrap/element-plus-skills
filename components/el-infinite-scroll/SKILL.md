---
name: "el-infinite-scroll"
description: "InfiniteScroll directive for loading more data when scrolling to bottom. Invoke when user needs to implement infinite scrolling, lazy loading, or pagination on scroll."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Infinite Scroll

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Use v-infinite-scroll="load", not an el-infinite-scroll component. The directive is deprecated for removal in 3.0.0; Scrollbar is the recommended replacement, while this directive remains available in 2.14.6. Give the scroll container height/overflow. immediate defaults to true and may keep loading until filled. Disable while loading or exhausted. It appends rows without virtualizing them.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <ul v-infinite-scroll="load" :infinite-scroll-disabled="count >= 30" style="height: 200px; overflow: auto"><li v-for="item in count" :key="item" style="height: 40px">{{ item }}</li></ul>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { ElInfiniteScroll as vInfiniteScroll } from 'element-plus'
const count = ref(10)
const load = () => { count.value = Math.min(30, count.value + 5) }
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- See [Scrollbar](../el-scrollbar/SKILL.md) for the recommended replacement.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/infinite-scroll) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/infinite-scroll.md).
