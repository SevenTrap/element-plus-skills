# message API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/message.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Options

| Name                     | Description                                                                                            | Type                                                                                       | Default |
| ------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------- |
| message                  | message text                                                                                           | **string** / **VNode** / **Function**`() => VNode`                                            | ''      |
| type                     | message type                                                                                           | **enum**`'primary' (2.9.11) \| 'success' \| 'warning' \| 'info' \| 'error'`                 | info    |
| plain (since 2.6.3)           | whether message is plain                                                                               | **boolean**                                                                                 | false   |
| icon                     | custom icon component, overrides `type`                                                                | **string** / **Component**                                                                   | —       |
| dangerouslyUseHTMLString | whether `message` is treated as HTML string                                                            | **boolean**                                                                                 | false   |
| customClass              | custom class name for Message                                                                          | **string**                                                                                  | ''      |
| duration                 | display duration, millisecond. If set to 0, it will not turn off automatically                         | **number**                                                                                  | 3000    |
| showClose                | whether to show a close button                                                                         | **boolean**                                                                                 | false   |
| onClose                  | callback function when closed with the message instance as the parameter                               | **Function**`() => void`                                                                    | —       |
| offset                   | set the distance to the viewport edge (top when placement is 'top', bottom when placement is 'bottom') | **number**                                                                                  | 16      |
| placement (since 2.11.0)      | message placement position                                                                             | **enum**`'top' \| 'top-left' \| 'top-right' \| 'bottom' \| 'bottom-left' \| 'bottom-right'` | top     |
| appendTo                 | set the root element for the message, default to `document.body`                                       | **CSSSelector** / **HTMLElement**                                                            | —       |
| grouping                 | merge messages with the same content, type of VNode message is not supported                           | **boolean**                                                                                 | false   |
| repeatNum                | The number of repetitions, similar to badge, is used as the initial number when used with `grouping`   | **number**                                                                                  | 1       |

### Methods

`Message` and `this.$message` returns the current Message instance. To manually close the instance, you can call `close` on it.

| Name  | Description       | Type                    |
| ----- | ----------------- | ----------------------- |
| close | close the Message | **Function**`() => void` |
