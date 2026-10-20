---
name: "el-color-picker"
description: "ColorPicker component for color selection. Invoke when user needs to select colors, set theme colors, or customize color values."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# ColorPicker

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Bind a color string and allow null or the configured clear value. show-alpha enables alpha; default format is hex without alpha, rgb with alpha. Set color-format when storage requires a fixed representation. active-change reports intermediate movement; change reports commitment. label is deprecated for accessibility: use aria-label. Use ColorPickerPanel for an always-visible editor.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-color-picker v-model="color" show-alpha color-format="rgb" aria-label="Accent" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
const color = ref<string | null>('rgba(64, 158, 255, 0.8)')
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/color-picker) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/color-picker.md).
