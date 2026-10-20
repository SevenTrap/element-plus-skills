---
name: "el-autocomplete"
description: "Autocomplete component for input suggestions. Invoke when user needs to provide input suggestions, autocomplete functionality, or search-as-you-type features."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Autocomplete

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Bind a string; fetch-suggestions(query, callback) passes suggestion objects to callback. value-key defaults to value; select receives the whole object. Use the default slot's item to customize rendering. debounce defaults to 300 ms. Guard remote responses against stale requests. popper-append-to-body is deprecated; use teleported.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-autocomplete v-model="query" :fetch-suggestions="search" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
const query = ref('')
const search = (text: string, callback: (items: { value: string }[]) => void) => {
  callback([{ value: 'Vue' }, { value: 'Element Plus' }].filter(item => item.value.toLowerCase().includes(text.toLowerCase())))
}
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/autocomplete) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/autocomplete.md).
