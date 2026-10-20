---
name: "el-link"
description: "Link component for text hyperlinks. Invoke when user needs to create text links, navigation links, or styled anchor elements."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Link

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Use el-link href without a model. underline accepts always/hover/never; boolean values are deprecated for removal in 3.0.0. href goes directly to the native anchor: validate externally supplied destinations and protocols. disabled prevents normal activation.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-link href="https://element-plus.org/" type="primary" underline="hover" target="_blank" rel="noopener noreferrer">Element Plus</el-link>
</template>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/link) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/link.md).
