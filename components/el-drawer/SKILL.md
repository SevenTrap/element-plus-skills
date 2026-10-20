---
name: "el-drawer"
description: "Drawer component for displaying content in a slide-out panel. Invoke when user needs to create side panels, slide-out menus, or form drawers."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Drawer

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Bind a visibility boolean. direction is rtl/ltr/ttb/btt; size sets width or height. resizable is boolean only in 2.14.6; newer object configuration is unavailable. before-close(done) pauses closing: done() closes, done(true) cancels; the release docs incorrectly describe the no-argument case, so follow source behavior. Guard footer model assignments explicitly. Content is lazy; destroy-on-close removes it. Use append-to-body for nesting. visible.sync, custom-class, and the old title slot should be replaced by v-model, class, and header.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-button @click="open = true">Open</el-button>
  <el-drawer v-model="open" title="Details" size="40%" resizable><p>Content</p><template #footer><el-button @click="open = false">Close</el-button></template></el-drawer>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const open = ref(false)
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/drawer) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/drawer.md).
