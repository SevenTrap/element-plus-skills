---
name: "el-tree-v2"
description: "Virtualized Tree component for large hierarchical datasets with blazing fast scrolling. Invoke when user needs to display large tree structures (1000+ nodes) with virtual scrolling for performance."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Virtualized hierarchical trees

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- `ElTreeV2` is the beta virtualized tree. Pass a numeric `height` and data; `props.value` maps node identity (default `id`). This differs from standard Tree's `node-key`.
- Use stable unique keys across the whole tree. `item-size` is the fixed row height (default 26px); custom row content must fit it.
- There is no whole-tree `v-model`; use checked/current events and exposed key-based methods. `show-checkbox` enables checks; `check-strictly` decouples ancestry.
- `check-on-click-leaf` defaults to true. Set false when checkbox-only leaf interaction is intended.
- Filtering uses `filter-method` plus the exposed `filter(query)` call. `setData` replaces large data collections without requiring deep reactive tracking.
- `setChecked(key, checked, deep?)` supports its third argument in 2.14.6 (added 2.14.0). Do not assume standard Tree lazy-loading or drag/drop features are present.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ElTreeV2 } from 'element-plus'
const data = [{ id: 'root', label: 'Project', children: [{ id: 'task', label: 'Task' }] }]
const props = { value: 'id', label: 'label', children: 'children' }
</script>

<template>
  <el-tree-v2 :data="data" :props="props" :height="200" show-checkbox
    :default-expanded-keys="['root']" :check-on-click-leaf="false" />
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/tree-v2.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/tree-v2) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/tree-v2/basic.vue).
