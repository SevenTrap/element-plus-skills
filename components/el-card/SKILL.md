---
name: "el-card"
description: "Card component for integrating information in a card container. Invoke when user needs to display grouped content, dashboard cards, or content sections with headers."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Card

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Use header/default/footer slots; header and footer props are plain text. shadow is always, hover, or never. body-style accepts a CSS object or string; body-class supplies a reusable class. There is no v-model.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-card shadow="hover"><template #header>Account</template>Details<template #footer>Updated today</template></el-card>
</template>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/card) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/card.md).
