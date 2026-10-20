# watermark API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/watermark.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name    | Description                                                                                     | Type                         | Default                    |
| ------- | ----------------------------------------------------------------------------------------------- | ---------------------------- | -------------------------- |
| width   | The width of the watermark, the default value of `content` is its own width                     | **number**                    | 120                        |
| height  | The height of the watermark, the default value of `content` is its own height                   | **number**                    | 64                         |
| rotate  | When the watermark is drawn, the rotation Angle, unit `°`                                       | **number**                    | -22                        |
| z-index | The z-index of the appended watermark element                                                   | **number**                    | 9                          |
| image   | Image source, it is recommended to export 2x or 3x image, high priority                         | **string**                    | —                          |
| content | Watermark text content                                                                          | **string**/**array**`string[]` | Element Plus               |
| font    | Text style                                                                                      | [Font](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/watermark.md#font)                | [Font](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/watermark.md#font)              |
| gap     | The spacing between watermarks                                                                  | **array**`[number, number]`   | \[100, 100\]               |
| offset  | The offset of the watermark from the upper left corner of the container. The default is `gap/2` | **array**`[number, number]`   | \[gap\[0\]/2, gap\[1\]/2\] |

### Font

| Name              | Description   | Type                                                                                 | Default         |
| ----------------- | ------------- | ------------------------------------------------------------------------------------ | --------------- |
| color             | font color    | **string**                                                                            | rgba(0,0,0,.15) |
| fontSize          | font size     | **number** / **string**                                                                | 16              |
| fontWeight        | font weight   | **enum**`'normal' \| 'bold' \| 'lighter' \| 'bolder' \| number`                       | normal          |
| fontFamily        | font family   | **string**                                                                            | sans-serif      |
| fontGap (since 2.11.5) | font gap      | **number**                                                                            | 3               |
| fontStyle         | font style    | **enum**`'none' \| 'normal' \| 'italic' \| 'oblique'`                                 | normal          |
| textAlign         | text align    | **enum**`'left' \| 'right' \| 'center' \| 'start' \| 'end' `                          | center          |
| textBaseline      | text baseline | **enum**`'top' \| 'hanging' \| 'middle' \| 'alphabetic' \| 'ideographic' \| 'bottom'` | hanging         |

### Slots

| Name    | Description                    |
| ------- | ------------------------------ |
| default | container for adding watermark |
