---
name: "el-slider"
description: "Slider component for dragging within a fixed range. Invoke when user needs to select numeric values within a range, set volume/brightness, or filter by price range."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Numeric and range sliders

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Bind a number in normal mode or a two-number array with `range`. Set `min`, `max`, and positive `step` consistently with the desired domain.
- `input` fires during dragging; `change` fires on committed changes. Use the latter for expensive side effects.
- `marks` maps numeric positions to text or styled labels; `show-stops` renders step stops. `format-tooltip` controls displayed values.
- `vertical` needs a defined `height`. `show-input` is for non-range sliders. Use `aria-label`, and `range-start-label`/`range-end-label` for range thumbs; `label` is deprecated.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElSlider } from 'element-plus'
const range = ref([4, 8])
</script>

<template>
  <el-slider v-model="range" range show-stops :max="10"
    range-start-label="Minimum" range-end-label="Maximum" />
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/slider.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/slider) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/slider/range-selection.vue).
