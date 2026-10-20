---
name: "el-tour"
description: "Tour component for guiding users through products. Invoke when user needs to create product tours, onboarding guides, or feature walkthroughs."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Guided application tours

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Compose `ElTour` with `ElTourStep`. Boolean `v-model` controls opening; numeric `v-model:current` selects the zero-based step.
- `target` accepts an HTMLElement, query-selector string, or function returning an element. Component refs need their DOM element (for example buttonRef?.$el). Missing targets show a centered card.
- Open after the targets are mounted and visible; when navigation creates the next target, coordinate route changes and rendering before continuing.
- `mask` can be boolean or a style/color object. `:mask="false"` supports non-modal tours; `target-area-clickable` controls interaction through the highlighted area.
- Use `close` for dismissal and `finish` for completion. Per-step settings override tour-level placement/mask presentation.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElButton, ElTour, ElTourStep } from 'element-plus'
const open = ref(false)
const current = ref(0)
</script>

<template>
  <el-button id="tour-start" @click="open = true">Begin tour</el-button>
  <el-tour v-model="open" v-model:current="current">
    <el-tour-step target="#tour-start" title="Start here" description="This opens the tour." />
    <el-tour-step title="Ready" description="You can now continue." />
  </el-tour>
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/tour.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/tour) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/tour/target.vue).
