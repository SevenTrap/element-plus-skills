---
name: "el-input-tag"
description: "InputTag component for adding content as tags. Invoke when user needs to create tag inputs, multi-value inputs, or keyword/tag entry fields."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# InputTag

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Bind string[]. trigger is Enter or Space; delimiter can also create tags. max limits stored tag count while max-collapse-tags controls how many tags remain visible with collapse-tags. draggable enables ordering; drag-tag reports old/new indices and value. input reports unfinished text, change/add-tag/remove-tag report stored tags. Customize tags through the tag slot. No virtual scrolling is provided.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-input-tag v-model="tags" :max="5" clearable draggable aria-label="Tags" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
const tags = ref<string[]>(['Vue'])
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/input-tag) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/input-tag.md).
