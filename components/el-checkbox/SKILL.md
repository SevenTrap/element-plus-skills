---
name: "el-checkbox"
description: "Checkbox component for multiple choice selection. Invoke when user needs to allow users to select multiple options from a list, create check-all functionality, or toggle between states."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Checkbox

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Standalone v-model is normally boolean; true-value/false-value allow custom values. CheckboxGroup binds an array and children need explicit value. Using label as the stored value is deprecated for removal in 3.0.0. true-label/false-label are deprecated in favor of true-value/false-value; controls is deprecated in favor of aria-controls. indeterminate changes appearance only.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-checkbox-group v-model="selected"><el-checkbox value="vue">Vue</el-checkbox><el-checkbox value="ep">Element Plus</el-checkbox></el-checkbox-group>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const selected = ref<string[]>(['vue'])
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/checkbox) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/checkbox.md).
