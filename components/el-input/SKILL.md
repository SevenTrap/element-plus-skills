---
name: "el-input"
description: "Input component for text entry with multiple types, validation, and formatting. Invoke when user needs to implement text input, textarea, or password input."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Input

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Bind a string/number; the native displayed value is text. Use InputNumber for numeric stepping and limits. type="textarea" enables autosize. formatter/parser work only with type text and should be paired. clearable and show-password supply clear/password actions. Use aria-label instead of deprecated label. v-model lazy/number/trim modifiers exist in 2.14.6. input reports typing; change reports a committed change.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-input v-model="text" clearable maxlength="80" show-word-limit aria-label="Title" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
const text = ref('')
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/input) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/input.md).
