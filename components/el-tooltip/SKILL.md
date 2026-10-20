---
name: "el-tooltip"
description: "Tooltip component for displaying prompt information on mouse hover. Invoke when user needs to show hints, tips, or additional information on hover."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Contextual tooltips

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Put one real trigger element in the default slot; use `content` for plain text or `#content` for rich markup. Wrap disabled controls in a usable element because disabled controls cannot emit normal pointer/focus events.
- `v-model:visible` or a supplied boolean `visible` controls visibility. In controlled mode, manage opening and closing yourself rather than expecting trigger behavior to do it.
- Default trigger is hover. Customize `show-after`/`hide-after`, `effect`, and placement. Tooltips are teleported by default; use `append-to`/`teleported` for deliberate overlay containment.
- `virtual-triggering` with `virtual-ref` attaches to an external element; virtual triggering requires application-managed visibility/events.
- `raw-content` interprets `content` as HTML; never use it with untrusted content. Escape plain text or use VNodes/slots instead.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ElButton, ElTooltip } from 'element-plus'
</script>

<template>
  <el-tooltip content="Save your changes" placement="top">
    <el-button>Save</el-button>
  </el-tooltip>
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/tooltip.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/tooltip) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/tooltip/basic.vue).
