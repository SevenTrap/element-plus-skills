---
name: "el-icon"
description: "Icon component for displaying SVG icons. Invoke when user needs to display icons, customize icon sizes and colors, or use Element Plus icon collection."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Icon

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Import SVG icons from @element-plus/icons-vue; el-icon styles its child component with size/color. Component icon props take imported bindings such as :icon="Edit". Old Element UI CSS icon classes are not this API. No model is used; label icon-only actions. Alias names such as Menu if native-tag naming conflicts arise.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-icon :size="24" color="#409eff"><Edit /></el-icon>
</template>

<script setup lang="ts">
import { Edit } from '@element-plus/icons-vue'
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/icon) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/icon.md).
