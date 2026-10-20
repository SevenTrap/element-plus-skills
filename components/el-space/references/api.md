# space API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/space.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name       | Description                     | Type                                                                                                                          | Default    |
| ---------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------- |
| alignment  | Controls the alignment of items | **enum**`'center' \| 'normal' \| 'stretch' \| ...` [align-items](https://developer.mozilla.org/en-US/docs/Web/CSS/align-items) | center     |
| class      | className                       | **string** / **object** / **array**                                                                                              | —          |
| direction  | Placement direction             | **enum**`'vertical' \| 'horizontal'`                                                                                           | horizontal |
| prefix-cls | Prefix for space-items          | **string**                                                                                                                     | —          |
| style      | Extra style rules               | **string** / **object**`CSSProperties \| CSSProperties[] \| string[]`                                                           | —          |
| spacer     | Spacer                          | **string** / **number** / **VNode**                                                                                              | —          |
| size       | Spacing size                    | **enum**`'default' \| 'small' \| 'large'` / **number** / **array**`[number, number]`                                             | small      |
| wrap       | Auto wrapping                   | **boolean**                                                                                                                    | false      |
| fill       | Whether to fill the container   | **boolean**                                                                                                                    | false      |
| fill-ratio | Ratio of fill                   | **number**                                                                                                                     | 100        |

### Slots

| name    | description        |
| ------- | ------------------ |
| default | Items to be spaced |
