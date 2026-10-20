# progress API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/progress.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                   | Description                                                                           | Type                                                                                                        | Default |
| ---------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------- |
| percentage (required) | percentage                                                                            | **number**`(0-100)`                                                                                          | 0       |
| type                   | the type of progress bar                                                              | **enum**`'line' \| 'circle' \| 'dashboard'`                                                                  | line    |
| stroke-width           | the width of progress bar                                                             | **number**                                                                                                   | 6       |
| text-inside            | whether to place the percentage inside progress bar, only works when `type` is 'line' | **boolean**                                                                                                  | false   |
| status                 | the current status of progress bar                                                    | **enum**`'success' \| 'exception' \| 'warning'`                                                              | —       |
| indeterminate          | set indeterminate progress                                                            | **boolean**                                                                                                  | false   |
| duration               | control the animation duration of indeterminate progress or striped flow progress     | **number**                                                                                                   | 3       |
| color                  | background color of progress bar. Overrides `status` prop                             | **string** / **function**`(percentage: number) => string` / **Array**`{ color: string; percentage: number }[]` | ''      |
| width                  | the canvas width of circle progress bar                                               | **number**                                                                                                   | 126     |
| show-text              | whether to show percentage                                                            | **boolean**                                                                                                  | true    |
| stroke-linecap         | circle/dashboard type shape at the end path                                           | **enum**`'butt' \| 'round' \| 'square'`                                                                      | round   |
| format                 | custom text format                                                                    | **Function**`(percentage: number) => string`                                                                 | —       |
| striped (since 2.3.4)       | stripe over the progress bar's color                                                  | **boolean**                                                                                                  | false   |
| striped-flow (since 2.3.4)  | get the stripes to flow                                                               | **boolean**                                                                                                  | false   |

### Slots

| Name    | Description        | Type                              |
| ------- | ------------------ | --------------------------------- |
| default | Customized content | **object**`{ percentage: number }` |
