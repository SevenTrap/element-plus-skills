---
name: "el-carousel"
description: "Carousel component for looping images or texts in limited space. Invoke when user needs to display image sliders, content carousels, or rotating banners."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Carousel

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Compose el-carousel with el-carousel-item and a usable height. There is no v-model: use initial-index, change, and navigation exposes. interval is milliseconds; autoplay, loop, and pause-on-hover control motion. Vertical mode needs explicit height. type="card" and card-scale enable card presentation. change emits current and previous indices.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-carousel height="160px" :autoplay="false"><el-carousel-item v-for="item in 3" :key="item"><h3>{{ item }}</h3></el-carousel-item></el-carousel>
</template>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/carousel) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/carousel.md).
