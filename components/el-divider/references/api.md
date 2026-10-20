# divider API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/divider.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name             | Description                                                | Type                                                                                                                                        | Default    |
| ---------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| direction        | Set divider's direction                                    | **enum**`'horizontal' \| 'vertical'`                                                                                                         | horizontal |
| border-style     | Set the style of divider                                   | **enum**`'none' \| 'solid' \| 'hidden' \| 'dashed' \| ...` [css/border-style](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-style) | solid      |
| content-position | The position of the customized content on the divider line | **enum**`'left' \| 'right' \| 'center'`                                                                                                      | center     |

### Slots

| Name    | Description                            |
| ------- | -------------------------------------- |
| default | Customized content on the divider line |
