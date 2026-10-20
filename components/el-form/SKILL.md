---
name: "el-form"
description: "Form component for data collection, validation, and submission. Invoke when user needs to create forms, implement validation, or handle form data."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Form

Target **Element Plus 2.14.6** with Vue 3. APIs added to dev after this release are outside this skill.

## Implementation guidance

Use :model, not a form v-model. Each validated/resettable FormItem needs prop matching its model path. Rules follow async-validator. validate() without a callback returns a Promise that rejects on invalid data: catch it or use a callback. resetFields restores initial field values and validation state; clearValidate only clears validation. setInitialValues is available since 2.13.1. With multiple controls in an item, label each control accessibly.

## Working example

Assumes Element Plus 2.14.6 components and CSS are registered in the application. Icons and local directives are imported explicitly when used.

```vue
<template>
  <el-form ref="form" :model="model" :rules="rules" label-width="auto"><el-form-item label="Name" prop="name"><el-input v-model="model.name" /></el-form-item><el-button @click="submit">Validate</el-button></el-form>
  <p>{{ result }}</p>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import type { FormInstance, FormRules } from 'element-plus'
const form = ref<FormInstance>()
const model = ref({ name: '' })
const rules: FormRules = { name: [{ required: true, message: 'Enter a name', trigger: 'blur' }] }
const result = ref('')
const submit = () => {
  form.value?.validate(valid => { result.value = valid ? 'Valid' : 'Check the form' })
}
</script>
```

## Versioned reference

- Read [the complete 2.14.6 API](references/api.md) for props, events, slots, exposes, defaults, and callback types before adding options.
- Check [2.14.6 source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/form) and [release documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/form.md).
