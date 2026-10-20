---
name: "el-rate"
description: "Rate component for rating functionality. Invoke when user needs to collect user ratings, display star ratings, or allow feedback scoring."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Numeric ratings

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Bind a numeric `v-model`; default score is 0 and default `max` is 5. `allow-half` enables half-step selection.
- `disabled` makes the rating read-only; use `score-template` with `show-score` for a numeric display. `show-text` uses `texts` instead.
- `clearable` lets selecting the same score reset to zero. `change` reports committed user changes.
- Use `aria-label` for its accessible name; the old `label` alias is deprecated. Custom icons are Vue components, not legacy CSS icon names.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElRate } from 'element-plus'
const score = ref(3.5)
</script>

<template><el-rate v-model="score" allow-half clearable aria-label="Rating" /></template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/rate.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/rate) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/rate/allow-half.vue).
