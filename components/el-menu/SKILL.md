---
name: "el-menu"
description: "Menu component for website navigation with horizontal and vertical modes. Invoke when user needs to create navigation menus, sidebars, or dropdown menus."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Menu

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Use unique string item indices with el-menu-item/el-sub-menu. There is no v-model: default-active, select, and exposed methods manage selection. mode="horizontal" is a top bar; collapse is for vertical mode. menu-trigger controls horizontal submenus. router uses index as the path or accepts route; keep active state aligned with current route. Deprecated background-color/text-color/active-text-color props should become --el-menu-bg-color/--el-menu-text-color/--el-menu-active-color CSS variables.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-menu :default-active="active" @select="select"><el-menu-item index="overview">Overview</el-menu-item><el-sub-menu index="settings"><template #title>Settings</template><el-menu-item index="profile">Profile</el-menu-item></el-sub-menu></el-menu>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const active = ref('overview')
const select = (index: string) => { active.value = index }
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/menu) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/menu.md).
