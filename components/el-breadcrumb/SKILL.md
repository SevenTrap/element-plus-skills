---
name: "el-breadcrumb"
description: "Breadcrumb component for displaying the location of the current page. Invoke when user needs to show navigation paths, page hierarchy, or enable easier browsing back."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Breadcrumb

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Compose el-breadcrumb with el-breadcrumb-item. Use plain text for the current page; to and replace integrate with an installed Vue Router. separator-icon takes an imported icon component and overrides separator. There is no v-model.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-breadcrumb separator="/"><el-breadcrumb-item>Home</el-breadcrumb-item><el-breadcrumb-item>Settings</el-breadcrumb-item></el-breadcrumb>
</template>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/breadcrumb) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/breadcrumb.md).
