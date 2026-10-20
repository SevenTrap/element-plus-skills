# alert API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/alert.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Alert API

### Attributes

| Name        | Description                              | Type                                                                       | Default |
| ----------- | ---------------------------------------- | -------------------------------------------------------------------------- | ------- |
| title       | alert title.                             | **string**                                                                  | —       |
| type        | alert type.                              | **enum**`'primary' (2.9.11) \| 'success' \| 'warning' \| 'info' \| 'error'` | info    |
| description | descriptive text.                        | **string**                                                                  | —       |
| closable    | whether alert can be dismissed.          | **boolean**                                                                 | true    |
| center      | whether content is placed in the center. | **boolean**                                                                 | false   |
| close-text  | customized close button text.            | **string**                                                                  | —       |
| show-icon   | whether a type icon is displayed.        | **boolean**                                                                 | false   |
| effect      | theme style.                             | **enum**`'light' \| 'dark'`                                                 | light   |

### Events

| Name  | Description                   | Type                                     |
| ----- | ----------------------------- | ---------------------------------------- |
| close | trigger when alert is closed. | **Function**`(event: MouseEvent) => void` |

### Slots

| Name          | Description                       |
| ------------- | --------------------------------- |
| default       | content of the alert description. |
| title         | content of the alert title.       |
| icon (since 2.9.7) | content of the alert icon.        |
