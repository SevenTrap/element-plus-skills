---
name: "el-tabs"
description: "Tabs component for dividing data collections into different types. Invoke when user needs to create tabbed interfaces, dynamic tabs, or card-style tabs."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Tab navigation

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Bind a string or number `v-model` to the active `ElTabPane` name. Set explicit unique `name` values to avoid relying on positional defaults.
- `default-value` initializes the active tab without the initial transition when no controlled model is supplied; it is available in 2.14.6.
- `before-leave(newName, oldName)` can return false or reject a Promise to cancel navigation. Use `tab-change` for actual active-name changes; `tab-click` also reports clicks on an already active tab.
- `editable`/`closable` only expose add/remove controls and events; update pane data and active state yourself. `lazy` delays initial pane rendering.
- Use `add-icon` slot; the camelCase `addIcon` slot is deprecated. Do not treat tabs as route navigation unless explicitly wired to a router.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElTabPane, ElTabs } from 'element-plus'
const active = ref('overview')
</script>

<template>
  <el-tabs v-model="active">
    <el-tab-pane label="Overview" name="overview">Overview</el-tab-pane>
    <el-tab-pane label="Settings" name="settings" lazy>Settings</el-tab-pane>
  </el-tabs>
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/tabs.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/tabs) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/tabs/basic.vue).
