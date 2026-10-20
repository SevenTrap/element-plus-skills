---
name: "el-avatar"
description: "Avatar component for representing people or objects with images, icons, or characters. Invoke when user needs to display user avatars, profile pictures, or entity representations."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Avatar

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Use src, an imported icon component, or default-slot fallback text; no v-model is used. size is pixels or large/default/small. fit controls image object-fit and error reports failures. el-avatar-group is available in 2.14.6; collapse options belong to the group.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-avatar :size="48" src="/avatar.png" alt="User">U</el-avatar>
</template>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/avatar) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/avatar.md).
