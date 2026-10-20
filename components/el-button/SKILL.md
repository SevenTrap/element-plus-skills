---
name: "el-button"
description: "Button component with various types, sizes, and styles. Invoke when user needs to implement buttons, button groups, or customize button appearance."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Button

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Use loading during pending actions. type controls appearance; native-type="submit" controls form submission. type="text" is deprecated: use text or link boolean props instead. color takes precedence over semantic type colors. Import icon components explicitly and label icon-only actions. There is no v-model.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-button type="primary" :loading="saving" @click="save">Save</el-button>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const saving = ref(false)
const save = async () => {
  saving.value = true
  try { await new Promise(resolve => setTimeout(resolve, 300)) }
  finally { saving.value = false }
}
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/button) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/button.md).
