---
name: "el-date-picker-panel"
description: "DatePickerPanel is the core panel component of DatePicker for custom date selection UI. Invoke when user needs to build custom date picker interfaces without the dropdown wrapper."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# DatePickerPanel

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

This always-visible core panel is beta in 2.14.6. Without value-format bind Date values; range modes need two values and plural modes allow arrays. Quarter variants are supported since 2.14.5. border controls its outline. Input placeholder/prefix and popup teleport settings belong to DatePicker, not the standalone panel.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-date-picker-panel v-model="date" type="date" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
const date = ref(new Date())
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/date-picker-panel) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/date-picker-panel.md).
