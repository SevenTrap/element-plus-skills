---
name: "el-input-number"
description: "InputNumber component for numeric input with controls. Invoke when user needs to input numbers with increment/decrement buttons, set numeric ranges, or enforce numeric input."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# InputNumber

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Bind number or null and allow an initially undefined value. precision must be a non-negative integer at least as precise as step. step-strictly restricts multiples. formatter/parser string callbacks exist since 2.14.0; formatter switches the inner input to text. Parsing uses Number.parseFloat and failed parsing emits null. value-on-clear accepts a number, null, min, or max and defaults to null. Use aria-label instead of deprecated label.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-input-number v-model="amount" :min="0" :max="100" :step="0.5" :precision="1" aria-label="Amount" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
const amount = ref<number | null>(1)
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/input-number) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/input-number.md).
