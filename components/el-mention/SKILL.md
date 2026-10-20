---
name: "el-mention"
description: "Mention component for mentioning users or items in input. Invoke when user needs to implement @mentions, user tagging, or item references in text inputs."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Mention

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Bind the entire input text string. Options use value/label/disabled or aliases through props. prefix is one character or an array of one-character triggers. search emits pattern/prefix; select emits option/prefix. Guard remote responses against stale requests. type="textarea" enables multiline text. whole/check-is-whole controls deletion of complete mentions. Customize labels with the label slot; there is no virtual scrolling API.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-mention v-model="text" :options="options" placeholder="Type @ to mention" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
const text = ref('')
const options = [{ value: 'alex', label: 'Alex' }, { value: 'sam', label: 'Sam' }]
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/mention) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/mention.md).
