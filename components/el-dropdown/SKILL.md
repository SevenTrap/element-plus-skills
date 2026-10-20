---
name: "el-dropdown"
description: "Dropdown component for toggleable menus displaying lists of links and actions. Invoke when user needs to create dropdown menus, action menus, or context menus."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Dropdown

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Provide one focusable default-slot trigger and a dropdown slot containing el-dropdown-menu/el-dropdown-item. trigger defaults to hover; click is useful for actions. command emits the selected item's command; there is no v-model. split-button has a separate main-button click action. hide-on-click controls dismissal. Avoid deprecated button type="text".

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-dropdown trigger="click" @command="select"><el-button>Actions</el-button><template #dropdown><el-dropdown-menu><el-dropdown-item command="edit">Edit</el-dropdown-item></el-dropdown-menu></template></el-dropdown>
  <p>{{ action }}</p>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const action = ref('')
const select = (command: string) => { action.value = command }
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/dropdown) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/dropdown.md).
