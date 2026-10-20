---
name: "el-descriptions"
description: "Descriptions component for displaying multiple fields in list form. Invoke when user needs to display detailed information, product specifications, or profile data."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Descriptions

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Compose el-descriptions with el-descriptions-item for read-only fields; there is no model. column counts items per row; item span/rowspan affect table layout. direction="vertical" places labels above values. label-width can be shared or overridden per item. Use label/default slots for richer fields.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-descriptions title="Account" :column="2" border><el-descriptions-item label="Name">Alex</el-descriptions-item><el-descriptions-item label="Status">Active</el-descriptions-item></el-descriptions>
</template>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/descriptions) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/descriptions.md).
