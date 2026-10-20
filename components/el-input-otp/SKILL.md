---
name: el-input-otp
description: Use Element Plus InputOtp for segmented one-time password entry, masked codes, per-character validation, and completion events.
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# InputOtp — Element Plus 2.14.6

Use `ElInputOtp` (`el-input-otp`) for segmented code entry. This component is marked **beta** in the target release.

- Keep the model a string so leading zeroes survive. A numeric initial value is accepted, but `update:modelValue`, `change`, and `finish` emit strings.
- `length` defaults to 6. `type` is a visual variant (`outlined`, `filled`, `underlined`); use `mask` to conceal characters.
- `inputmode="numeric"` requests a numeric keyboard; it does not validate input. Use `validator(char, index)` to restrict each character.
- `finish` means all fields are filled. Verify the code with the application backend; filling the inputs does not authenticate the user.
- The `separator` slot receives `{ index }`. Exposes include `inputRefs`, `focus(index?)`, and `blur()`.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElInputOtp } from 'element-plus'

const code = ref('')
const isDigit = (char: string) => /^[0-9]$/.test(char)
</script>

<template>
  <el-input-otp
    v-model="code"
    :length="6"
    inputmode="numeric"
    :validator="isDigit"
    aria-label="Verification code"
  />
</template>
```

Load Element Plus styles using the [quickstart](../../element-plus-quickstart/SKILL.md).
Read [the complete 2.14.6 API](references/api.md) for props, events, slots, and exposed methods.

Source: [2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/input-otp.md), [prop and event types](https://github.com/element-plus/element-plus/blob/2.14.6/packages/components/input-otp/src/input-otp.ts).
