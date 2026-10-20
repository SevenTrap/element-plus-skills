---
name: "el-anchor"
description: "Anchor component for anchor navigation. Invoke when user needs to create page anchor navigation, table of contents, or quick navigation to specific sections."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Anchor

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Compose el-anchor with el-anchor-link and matching section IDs. container accepts a selector, HTMLElement, or Window; offset changes the scroll destination, bound changes activation tolerance. The click event receives a MouseEvent: preventDefault() to suppress hash/history navigation. Horizontal mode does not support nested sub-link slots. There is no v-model.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-anchor><el-anchor-link href="#details" title="Details" /></el-anchor>
  <section id="details" style="margin-top: 500px; height: 800px">Details</section>
</template>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/anchor) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/anchor.md).
