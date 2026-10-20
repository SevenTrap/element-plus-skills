---
name: "el-radio"
description: "Radio component for single selection among multiple options. Invoke when user needs to allow users to select one option from a list, create radio groups, or implement mutually exclusive choices."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Single-choice controls

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Use a scalar `string | number | boolean` model on `ElRadioGroup`, with `ElRadio` or `ElRadioButton` children. Values must match the model's type (`:value="3"` differs from `value="3"`).
- Set each radio's `value` explicitly. The fallback where `label` acts as the value is deprecated and scheduled for removal in 3.0.0; labels/slots provide display text.
- Group `options` and `props` mappings are available in 2.14.6 as an alternative to child declarations.
- Use `aria-label` for accessible group naming; the RadioGroup `label` accessibility alias is deprecated. Group size styles radio buttons and bordered radios.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElRadio, ElRadioGroup } from 'element-plus'
const value = ref(3)
</script>

<template>
  <el-radio-group v-model="value" aria-label="Plan">
    <el-radio :value="3">Basic</el-radio>
    <el-radio :value="6">Advanced</el-radio>
  </el-radio-group>
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/radio.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/radio) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/radio/radio-group.vue).
