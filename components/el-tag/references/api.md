# tag API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/tag.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Tag API

### Tag Attributes

| Name                | Description                          | Type                                                               | Default |
| ------------------- | ------------------------------------ | ------------------------------------------------------------------ | ------- |
| type                | type of Tag                          | **enum**`'primary' \| 'success' \| 'info' \| 'warning' \| 'danger'` | primary |
| closable            | whether Tag can be removed           | **boolean**                                                         | false   |
| disable-transitions | whether to disable animations        | **boolean**                                                         | false   |
| hit                 | whether Tag has a highlighted border | **boolean**                                                         | false   |
| color               | background color of the Tag          | **string**                                                          | —       |
| size                | size of Tag                          | **enum**`'large' \| 'default' \| 'small'`                           | —       |
| effect              | theme of Tag                         | **enum**`'dark' \| 'light' \| 'plain'`                              | light   |
| round               | whether Tag is rounded               | **boolean**                                                         | false   |

### Tag Events

| Name  | Description                  | Type                                   |
| ----- | ---------------------------- | -------------------------------------- |
| click | triggers when Tag is clicked | **Function**`(evt: MouseEvent) => void` |
| close | triggers when Tag is removed | **Function**`(evt: MouseEvent) => void` |

### Tag Slots

| Name    | Description               |
| ------- | ------------------------- |
| default | customize default content |

## CheckTag API

### CheckTag Attributes

| Name                      | Description                       | Type                                                               | Default |
| ------------------------- | --------------------------------- | ------------------------------------------------------------------ | ------- |
| checked / v-model:checked | is checked                        | **boolean**                                                         | false   |
| disabled (since 2.8.2)         | whether the check-tag is disabled | **boolean**                                                         | false   |
| type (since 2.5.4)             | type of CheckTag                  | **enum**`'primary' \| 'success' \| 'info' \| 'warning' \| 'danger'` | primary |

### CheckTag Events

| Name   | Description                        | Type                                  |
| ------ | ---------------------------------- | ------------------------------------- |
| change | triggers when Check Tag is clicked | **Function**`(value: boolean) => void` |

### CheckTag Slots

| Name    | Description               |
| ------- | ------------------------- |
| default | customize default content |
