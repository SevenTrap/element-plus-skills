---
name: "el-color-picker-panel"
description: "ColorPickerPanel is the core panel component of ColorPicker for custom color selection UI. Invoke when user needs to build custom color picker interfaces without the dropdown wrapper."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# ColorPickerPanel

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

This standalone panel is beta in 2.14.6. Bind a color string or null; show-alpha changes the default format from hex to rgb. Choose color-format explicitly for storage. border controls the outline and predefine supplies presets. Popup trigger/teleport props belong to ColorPicker, not this panel.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-color-picker-panel v-model="color" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
const color = ref<string | null>('#409EFF')
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/color-picker-panel) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/color-picker-panel.md).
