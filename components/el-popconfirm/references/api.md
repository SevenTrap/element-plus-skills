# popconfirm API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/popconfirm.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                               | Description                                                                                         | Type                                                                         | Default        |
| ---------------------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | -------------- |
| title                              | Title                                                                                               | **string**                                                                    | —              |
| effect (since 2.11.2)                   | Tooltip theme, built-in theme: `dark` / `light`                                                     | **enum**`'dark' \| 'light'` / **string**                                       | light          |
| confirm-button-text                | Confirm button text                                                                                 | **string**                                                                    | —              |
| cancel-button-text                 | Cancel button text                                                                                  | **string**                                                                    | —              |
| confirm-button-type                | Confirm button type                                                                                 | **enum**`'primary' \| 'success' \| 'warning' \| 'danger' \| 'info' \| 'text'` | primary        |
| cancel-button-type                 | Cancel button type                                                                                  | **enum**`'primary' \| 'success' \| 'warning' \| 'danger' \| 'info' \| 'text'` | text           |
| icon                               | Icon Component                                                                                      | **string** / **Component**                                                     | QuestionFilled |
| icon-color                         | Icon color                                                                                          | **string**                                                                    | #f90           |
| hide-icon                          | is hide Icon                                                                                        | **boolean**                                                                   | false          |
| hide-after                         | delay of disappear, in millisecond                                                                  | **number**                                                                    | 200            |
| teleported                         | whether popconfirm is teleported to the body                                                        | **boolean**                                                                   | true           |
| persistent                         | when popconfirm inactive and `persistent` is `false` , popconfirm will be destroyed                 | **boolean**                                                                   | false          |
| width                              | popconfirm width, min width 150px                                                                   | **string** / **number**                                                        | 150            |
| [tooltip](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/tooltip.md#attributes) | Inherits all attributes from Tooltip, except: `popper-class`, `popper-style`, `fallback-placements` | —                                                                            | —              |

### Events

| Name    | Description                        | Type                                 |
| ------- | ---------------------------------- | ------------------------------------ |
| confirm | triggers when click confirm button | **Function**`(e: MouseEvent) => void` |
| cancel  | triggers when click cancel button  | **Function**`(e: MouseEvent) => void` |

### Slots

| Name             | Description                           | Type                                                                             |
| ---------------- | ------------------------------------- | -------------------------------------------------------------------------------- |
| reference        | HTML element that triggers Popconfirm | —                                                                                |
| actions (since 2.8.1) | content of the Popconfirm footer      | **object**`{ confirm: (e: MouseEvent) => void, cancel: (e: MouseEvent) => void }` |

### Exposes

| Name                | Description                  | Type                                        |
| ------------------- | ---------------------------- | ------------------------------------------- |
| popperRef (since 2.10.7) | el-popper component instance | **object**`Ref<PopperInstance \| undefined>` |
| hide (since 2.10.7)      | hide popconfirm              | **Function**`() => void`                     |
