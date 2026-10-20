---
name: "el-divider"
description: "Divider component for separating content. Invoke when user needs to create visual separation between content sections, add horizontal or vertical dividers."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Divider

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Use horizontal or vertical direction without a model. Default-slot content and content-position apply to horizontal dividers. border-style accepts CSS styles such as dashed.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <p>Overview</p><el-divider content-position="left" border-style="dashed">Details</el-divider><p>Content</p>
</template>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/divider) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/divider.md).
