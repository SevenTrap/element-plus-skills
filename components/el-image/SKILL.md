---
name: "el-image"
description: "Image component with lazy load, placeholder, and preview features. Invoke when user needs to display images with loading states, error handling, or preview functionality."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Image

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Use src and a sized container; fit follows CSS object-fit. There is no model. Non-empty preview-src-list enables preview; initial-index is zero-based. preview-teleported avoids parent clipping/transforms. lazy uses scroll-container or a detected scrolling ancestor; it is lazy loading, not virtualization. Use placeholder/error slots. Direct preview control uses ImageViewer or showPreview(), not an invented preview prop. Consult the pinned API before adopting dev-branch behavior.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-image style="width: 240px; height: 160px" src="/photo.jpg" :preview-src-list="['/photo.jpg']" fit="cover" preview-teleported><template #error>Image unavailable</template></el-image>
</template>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/image) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/image.md).
