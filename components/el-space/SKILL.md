---
name: "el-space"
description: "Space component for consistent spacing between elements. Invoke when user needs to create consistent gaps between components, layout spacing, or element arrangement."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Spacing component groups

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Use `ElSpace` to space direct child elements; it has no value model. `direction` controls horizontal/vertical flow and `alignment` maps cross-axis alignment.
- `size` accepts a named size, number, or `[horizontalGap, verticalGap]`. `wrap` permits horizontal wrapping.
- `fill` stretches children according to `fill-ratio`; ensure the container has the desired width. Use `spacer` for a text or VNode separator.
- For page grids or complex responsive layout, use Layout/CSS rather than assuming Space performs column layout.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ElButton, ElSpace } from 'element-plus'
</script>

<template>
  <el-space :size="[12, 8]" wrap>
    <el-button>Save</el-button><el-button>Preview</el-button><el-button>Cancel</el-button>
  </el-space>
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/space.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/space) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/space/basic.vue).
