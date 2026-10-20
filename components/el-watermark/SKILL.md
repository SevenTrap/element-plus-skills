---
name: "el-watermark"
description: "Watermark component for adding text or pattern watermarks. Invoke when user needs to protect content, brand documents, or add copyright notices."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Text and image watermarks

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Wrap protected content in `ElWatermark` and supply `content` as a string or string array for multiple lines. It has no `v-model`.
- `image` renders a logo instead of text; set explicit width/height and use a high-resolution source. Cross-origin images need suitable CORS headers because rendering uses canvas.
- `font`, `rotate`, `gap`, `offset`, and `z-index` control appearance. Tune text color explicitly for light/dark backgrounds; watermark font color does not automatically provide suitable contrast for every theme.
- The component observes mutations to restore its overlay, but it is a visual deterrent rather than access control. Keep data authorization in the application/server.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ElWatermark } from 'element-plus'
</script>

<template>
  <el-watermark :content="['Internal', 'Team workspace']" :font="{ color: 'rgba(0, 0, 0, .15)' }">
    <div style="height: 300px; padding: 24px">Document preview</div>
  </el-watermark>
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/watermark.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/watermark) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/watermark/multi-line.vue).
