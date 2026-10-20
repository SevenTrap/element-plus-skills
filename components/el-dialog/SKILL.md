---
name: "el-dialog"
description: "Dialog modal component for displaying content in a layer above the page. Invoke when user needs modal dialogs, confirmations, or form popups."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Dialog

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Bind a visibility boolean. Use header/footer slots; the old title slot is deprecated but the title prop remains valid. custom-class is deprecated: use class. before-close(done) intercepts component close requests: done() closes, leaving it uncalled keeps open. Custom footer assignments need their own guard. Content renders lazily; use open/opened and nextTick for refs. destroy-on-close discards contents. Use append-to-body for nested dialogs.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-button @click="open = true">Open</el-button>
  <el-dialog v-model="open" title="Details" width="480px"><p>Content</p><template #footer><el-button @click="open = false">Close</el-button></template></el-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const open = ref(false)
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/dialog) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/dialog.md).
