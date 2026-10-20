---
name: "el-empty"
description: "Empty component for placeholder hints in empty states. Invoke when user needs to display empty data states, no results found, or placeholder content."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Empty

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Use el-empty without a model. description is text; image supplies a URL; image-size is image width in pixels. image/description slots replace those parts; the default slot is the bottom action area.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-empty description="No saved items"><el-button>Create item</el-button></el-empty>
</template>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/empty) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/empty.md).
