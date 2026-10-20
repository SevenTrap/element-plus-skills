# skeleton API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/skeleton.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Skeleton API

### Skeleton Attributes

| Name     | Description                                                                                                                                                                                                                                 | Type                                                                              | Default |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------- |
| animated | whether showing the animation                                                                                                                                                                                                               | **boolean**                                                                        | false   |
| count    | how many fake items to render to the DOM                                                                                                                                                                                                    | **number**                                                                         | 1       |
| loading | whether to show skeleton content; false renders the default slot | **boolean** | true |
| rows     | numbers of the row, only useful when no template slot were given                                                                                                                                                                            | **number**                                                                         | 3       |
| throttle | rendering delay in milliseconds. Numbers represent delayed display, and can also be set to delay hide, for example `{ leading: 500, trailing: 500 }`. When needing to control the initial value of loading, you can set `{ initVal: true }` | **number** / **object**`{ leading?: number, trailing?: number, initVal?: boolean }` | 0       |

### Skeleton Slots

| Name     | Description                            | Type                       |
| -------- | -------------------------------------- | -------------------------- |
| default  | real rendering DOM                     | **object**`$attrs`          |
| template | content as rendering skeleton template | **object**`{ key: number }` |

## SkeletonItem API

### SkeletonItem Attributes

| Name    | Description                         | Type                                                                                             | Default |
| ------- | ----------------------------------- | ------------------------------------------------------------------------------------------------ | ------- |
| variant | the current rendering skeleton type | **enum**`'p' \| 'text' \| 'h1' \| 'h3' \| 'caption' \| 'button' \| 'image' \| 'circle' \| 'rect'` | text    |
