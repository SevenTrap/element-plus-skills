---
name: "el-loading"
description: "Loading component for showing animation while loading data. Invoke when user needs to display loading states, async operation feedback, or data fetching indicators."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Loading

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Use v-loading or ElLoading.service(), not el-loading. The directive accepts a boolean or documented options object. Service returns an instance whose close() must run in finally after async work. Fullscreen service calls share one active instance. Directive body/fullscreen/lock modifiers control placement and scroll locking. Containers need a measurable height. Spinner/svg values may render HTML: use trusted content only.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <div v-loading="loading" element-loading-text="Loading…" style="height: 160px">Content</div>
  <el-button @click="loading = !loading">Toggle</el-button>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { ElLoading } from 'element-plus'
const vLoading = ElLoading.directive
const loading = ref(true)
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/loading) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/loading.md).
