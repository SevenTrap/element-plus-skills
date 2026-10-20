---
name: "el-container"
description: "Container components for scaffolding basic page structure with header, aside, main, and footer sections. Invoke when user needs to create page layouts."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Container

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Compose el-container with el-header/el-aside/el-main/el-footer; there is no model. Direct header/footer children make the container vertical, otherwise horizontal. Explicit direction avoids detection problems introduced by wrappers. Header/footer height and Aside width use CSS strings. Set an application height for internally scrolling layouts.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-container style="height: 300px"><el-header>Header</el-header><el-container><el-aside width="160px">Navigation</el-aside><el-main>Content</el-main></el-container></el-container>
</template>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/container) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/container.md).
