# text API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/text.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                | Description        | Type                                                               | Default |
| ------------------- | ------------------ | ------------------------------------------------------------------ | ------- |
| type                | text type          | **enum**`'primary' \| 'success' \| 'warning' \| 'danger' \| 'info'` | —       |
| size                | text size          | **enum**`'large' \| 'default' \| 'small'`                           | default |
| truncated           | render ellipsis    | **boolean**                                                         | false   |
| line-clamp (since 2.4.0) | maximum lines      | **string** / **number**                                              | —       |
| tag                 | custom element tag | **string**                                                          | span    |

### Slots

| Name    | Description     |
| ------- | --------------- |
| default | default content |

### Exposes

| Name                  | Description                   | Type                    |
| --------------------- | ----------------------------- | ----------------------- |
| isTruncated (since 2.14.6) | whether the text is truncated | **object**`Ref<boolean>` |
