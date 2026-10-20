---
name: "el-cascader"
description: "Cascader component for hierarchical option selection. Invoke when user needs to select from multi-level data like regions, categories, or organizational structures."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Cascader

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Options default to value/label/children keys, remapped through props. Default v-model is a selected path array. props.emitPath=false returns the node value; props.multiple=true returns multiple paths (or values when emitPath=false). checkStrictly allows intermediate levels. lazyLoad resolves real children; this component does not virtualize nodes. popper-append-to-body is deprecated; use teleported.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-cascader v-model="value" :options="options" clearable />
</template>

<script setup lang="ts">
import { ref } from 'vue'
const value = ref<string[]>([])
const options = [{ value: 'guide', label: 'Guide', children: [{ value: 'install', label: 'Installation' }] }]
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/cascader) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/cascader.md).
