# backtop API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/backtop.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name              | Description                                                          | Type      | Default |
| ----------------- | -------------------------------------------------------------------- | --------- | ------- |
| target            | the target to trigger scroll.                                        | **string** | —       |
| visibility-height | the button will not show until the scroll height reaches this value. | **number** | 200     |
| right             | right distance.                                                      | **number** | 40      |
| bottom            | bottom distance.                                                     | **number** | 40      |

### Events

| Name  | Description          | Parameters                             |
| ----- | -------------------- | -------------------------------------- |
| click | triggers when click. | **Function**`(evt: MouseEvent) => void` |

### Slots

| Name    | Description                |
| ------- | -------------------------- |
| default | customize default content. |
