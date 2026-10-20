---
name: "el-badge"
description: "Badge component for displaying numbers or status marks on buttons and icons. Invoke when user needs to show notification counts, status indicators, or attention markers."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Badge

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

value is a string or number, not v-model. max only caps numeric values; strings display as supplied. is-dot shows a status dot; hidden suppresses the badge. show-zero defaults to true. offset is [left, top] relative to the usual position.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-badge :value="12" :max="9"><el-button>Messages</el-button></el-badge>
</template>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/badge) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/badge.md).
