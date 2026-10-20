---
name: "el-popover"
description: "Popover component for displaying rich content in a popup. Invoke when user needs to show complex content, nested operations, or rich information in a popup."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Rich floating content

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Use `#reference` for one trigger element. Put rich content in the default slot, or use `title` and `content` strings.
- Default trigger is `hover`; `click`, `focus`, and `contextmenu` are also available. A boolean `v-model:visible` enables controlled visibility; manage it explicitly instead of relying on trigger behavior.
- For an external trigger use `virtual-triggering` and `:virtual-ref="element"`. `v-popover` is deprecated; prefer virtual triggering.
- Floating content is teleported by default. Use `append-to`/`teleported` deliberately when container clipping or scoped styling affects the overlay.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ElButton, ElPopover } from 'element-plus'
</script>

<template>
  <el-popover title="Details" content="Additional information" trigger="click" :width="240">
    <template #reference><el-button>Details</el-button></template>
  </el-popover>
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/popover.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/popover) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/popover/basic-usage.vue).
