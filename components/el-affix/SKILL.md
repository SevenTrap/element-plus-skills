---
name: "el-affix"
description: "Affix component for fixing elements to a specific visible area. Invoke when user needs to create sticky navigation, fixed headers, or elements that remain visible while scrolling."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Affix

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Use el-affix without v-model; offset is measured from top or bottom. target constrains the fixed element to a CSS selector's bounds; it does not designate a scrolling container. The official target example uses a container without its own scrollbar. Use change for the fixed boolean and update()/updateRoot() after relevant layout changes.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-affix :offset="20"><el-button>Fixed action</el-button></el-affix>
</template>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/affix) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/affix.md).
