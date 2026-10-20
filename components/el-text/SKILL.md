---
name: "el-text"
description: "Text component for text display with styling options. Invoke when user needs to display styled text, truncated text, or text with semantic types."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Styled and truncated text

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Use `ElText` for semantic inline text styling. It has no value model; set `tag` when a different HTML element is appropriate.
- `truncated` creates a single-line ellipsis; constrain its width or its parent's width. `line-clamp` limits lines. Neither option can truncate content with unlimited available space.
- `isTruncated` is exposed in exactly 2.14.6. A component ref unwraps it, so use `textRef?.isTruncated` in templates to enable a Tooltip only when necessary.
- The component supplies a native title when truncated; set `title=""` if a custom Tooltip replaces that behavior. Measurement updates after layout, resize, and content changes.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElText, ElTooltip } from 'element-plus'
const textRef = ref<InstanceType<typeof ElText>>()
const label = 'A long label that should only show a tooltip when truncated'
</script>

<template>
  <el-tooltip :content="label" :disabled="!textRef?.isTruncated">
    <el-text ref="textRef" truncated title="" style="width: 160px">{{ label }}</el-text>
  </el-tooltip>
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/text.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/text) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/text/truncated.vue).
