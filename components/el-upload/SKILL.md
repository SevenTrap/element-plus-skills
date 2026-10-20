---
name: "el-upload"
description: "Upload component for file uploads via click or drag-and-drop. Invoke when user needs to upload files, images, or documents with preview, validation, and progress tracking."
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# File uploads and controlled file lists

Target Element Plus **2.14.6** with Vue 3. Check the pinned API before adopting examples from the moving `dev` branch.

## Usage decisions

- Use `ElUpload` with an actual application `action` endpoint, or override `http-request`. Bind `v-model:file-list` to `UploadUserFile[]`; it is not a model of raw browser File objects.
- `auto-upload` defaults true. Set false and use an `UploadInstance` ref's `submit()` for manual uploads. Exposed `abort()`, `clearFiles()`, and `handleStart()` manage queued operations.
- `before-upload(rawFile)` can return false or reject to stop an upload; validate type/size there. `accept` is a picker hint, not validation, and server-side validation remains necessary.
- `limit` plus `on-exceed` reports excess files; it does not replace an existing file automatically. Implement replacement using `clearFiles`, `genFileId`, and `handleStart` when required.
- Custom `http-request` receives progress/success/error callbacks. If it returns a Promise, Upload attaches success/error handlers; avoid firing the callbacks again for the same completion.
- `directory` (2.13.1) selects folders and flattens their files. Use hook props such as `:on-success`, `:on-error`, and `:before-remove`, rather than assuming they are native DOM events.

## Example

This SFC assumes Element Plus 2.14.6 CSS is loaded by the application.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { ElButton, ElUpload } from 'element-plus'
import type { UploadInstance, UploadUserFile } from 'element-plus'
const uploadRef = ref<UploadInstance>()
const files = ref<UploadUserFile[]>([])
const submit = () => uploadRef.value?.submit()
</script>

<template>
  <el-upload ref="uploadRef" v-model:file-list="files" action="/api/upload" :auto-upload="false">
    <template #trigger><el-button>Select files</el-button></template>
    <el-button type="primary" @click="submit">Upload</el-button>
  </el-upload>
</template>
```

## References

- Read [the 2.14.6 API](references/api.md) for complete props, events, slots, and exposed methods.
- [Official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/upload.md).
- [Component source](https://github.com/element-plus/element-plus/tree/2.14.6/packages/components/upload) and [upstream example](https://github.com/element-plus/element-plus/blob/2.14.6/docs/examples/upload/manual.vue).
