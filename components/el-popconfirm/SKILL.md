---
name: "el-popconfirm"
description: "Popconfirm component for simple confirmation dialogs. Invoke when user needs to confirm actions before execution, like delete operations or irreversible actions."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Inline confirmation popover

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Put one trigger element in `#reference` and provide `title`; `content` is ignored. Popconfirm uses a click trigger by default.
- Run the operation on `confirm`, not on the reference button's click; handle `cancel` separately. There is no ordinary value model; controlled visibility is inherited from Tooltip.
- Configure confirmation/cancellation text and button types, `icon`/`hide-icon`, and placement as needed. Consult the inherited Popover/Tooltip options for positioning.
- `actions` slot receives `confirm` and `cancel`; call these to preserve the component's event/closing behavior when replacing buttons.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElButton, ElPopconfirm } from 'element-plus'
const deleted = ref(false)
</script>

<template>
  <el-popconfirm title="Delete this item?" @confirm="deleted = true">
    <template #reference><el-button :disabled="deleted">Delete</el-button></template>
  </el-popconfirm>
  <p v-if="deleted">Deleted</p>
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/popconfirm.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/popconfirm) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/popconfirm/trigger-event.vue).
