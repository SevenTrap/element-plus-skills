---
name: "el-steps"
description: "Steps component for guiding users through processes. Invoke when user needs to display step progress, wizard interfaces, or process workflows."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Workflow steps

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Compose `ElSteps` with `ElStep` children. `active` is a zero-based numeric prop; there is no `v-model` or automatic workflow progression.
- `process-status` styles the active step; `finish-status` styles preceding steps. An individual step's `status` overrides inferred state.
- `direction="vertical"` requires a height for useful spacing. `simple` removes descriptions and other rich step presentation.
- Set `title`, `description`, and an icon component or slots. Advance only after application validation succeeds; reaching the number of steps marks all as finished.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElButton, ElStep, ElSteps } from 'element-plus'
const active = ref(0)
const next = () => { active.value = (active.value + 1) % 4 }
</script>

<template>
  <el-steps :active="active" finish-status="success">
    <el-step title="Details" /><el-step title="Review" /><el-step title="Done" />
  </el-steps>
  <el-button @click="next">Next</el-button>
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/steps.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/steps) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/steps/basic.vue).
