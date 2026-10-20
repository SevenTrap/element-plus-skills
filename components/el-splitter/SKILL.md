---
name: "el-splitter"
description: "Splitter component for dividing areas horizontally or vertically. Invoke when user needs to create resizable panels, split views, or collapsible layouts."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Resizable panels

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Compose `ElSplitter` with `ElSplitterPanel`; give the splitter's container explicit dimensions. `layout="vertical"` divides height; the default horizontal layout divides width.
- Panel `size`/`min`/`max` accept pixel numbers or percentage strings. Bind `v-model:size` on panels for controlled sizing; there is no whole-splitter value model.
- `resizable="false"` must be bound as `:resizable="false"`; `collapsible` enables collapsing. Choose compatible minimum and maximum dimensions.
- `resize-start`, `resize`, and `resize-end` report the affected index and panel-size array. `lazy` defers content resizing until dragging ends.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElSplitter, ElSplitterPanel } from 'element-plus'
const size = ref(180)
</script>

<template>
  <div style="height: 240px; width: 100%">
    <el-splitter>
      <el-splitter-panel v-model:size="size" :min="100" :max="300">Navigation</el-splitter-panel>
      <el-splitter-panel>Content</el-splitter-panel>
    </el-splitter>
  </div>
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/splitter.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/splitter) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/splitter/size.vue).
