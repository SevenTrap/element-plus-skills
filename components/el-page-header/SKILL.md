---
name: "el-page-header"
description: "PageHeader component for page navigation headers. Invoke when user needs to create page headers with back navigation, breadcrumbs, or title sections."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Page header and back action

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Use `ElPageHeader` for a page title and a back affordance; it emits `back` but does not perform navigation. Attach the application's router/history action explicitly.
- Set `title` for the back-area text and `content` for the main heading, or use their named slots. There is no `v-model`.
- `breadcrumb` appears above the heading, `extra` holds actions, and the default slot holds page content below it.
- `icon` accepts an icon component; use `icon=""` to suppress it. The `icon` slot provides custom markup.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ElPageHeader } from 'element-plus'
const goBack = () => window.history.back()
</script>

<template><el-page-header title="Back" content="Details" @back="goBack" /></template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/page-header.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/page-header) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/page-header/basic.vue).
