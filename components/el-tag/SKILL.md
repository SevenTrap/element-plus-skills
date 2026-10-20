---
name: "el-tag"
description: "Tag component for marking and selection. Invoke when user needs to display labels, categories, or removable tags for filtering and categorization."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Tags and checkable tags

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- `ElTag` displays status/category text; `closable` emits `close` but does not remove it. Update the backing list (for example using `filter`) to remove a tag.
- Tag `type` values use `danger` rather than `error`. `effect` controls light/dark/plain appearance, `round` changes shape, and `hit` adds a border treatment.
- `ElCheckTag` is a separate boolean-selection component. Pass `checked` and handle `change(checked)`; it is not an ordinary `v-model` input.
- Provide unique keys for dynamic tag lists. `disable-transitions` can help when surrounding list animation manages transitions.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElCheckTag, ElTag } from 'element-plus'
const tags = ref(['Vue', 'Element Plus'])
const checked = ref(false)
</script>

<template>
  <el-tag v-for="tag in tags" :key="tag" closable @close="tags = tags.filter(item => item !== tag)">
    {{ tag }}
  </el-tag>
  <el-check-tag :checked="checked" @change="checked = $event">Selected</el-check-tag>
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/tag.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/tag) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/tag/checkable.vue).
