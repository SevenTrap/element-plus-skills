---
name: "el-backtop"
description: "Backtop component for back-to-top button. Invoke when user needs to provide quick navigation back to the top of a long page."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Backtop

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

target is the CSS selector of the actual scrolling element and must resolve on mounting; without it document scrolling is used. Give custom scroll containers a finite height and overflow. visibility-height defaults to 200 px. The default slot customizes a 40×40 px control. There is no v-model.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <div class="backtop-scroll" style="height: 200px; overflow: auto"><div style="height: 1000px">Scroll down</div></div>
  <el-backtop target=".backtop-scroll" :visibility-height="100" />
</template>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/backtop) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/backtop.md).
