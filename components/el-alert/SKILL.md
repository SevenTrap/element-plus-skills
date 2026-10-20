---
name: "el-alert"
description: "Alert component for displaying important alert messages. Invoke when user needs to show non-dismissible notifications, status messages, or important information that requires user attention."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Alert

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

An inline alert has no v-model or automatic timeout. Types are primary, success, warning, info, error; effect is light or dark. closable controls dismissal and close reports it. Use title/default/description/icon slots for rich content.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-alert title="Saved" type="success" show-icon :closable="false" />
</template>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/alert) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/alert.md).
