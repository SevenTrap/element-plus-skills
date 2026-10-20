# scrollbar API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/scrollbar.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                              | Description                                                                                                                     | Type                                                                | Default |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------- |
| height                            | height of scrollbar                                                                                                             | **string** / **number**                                               | —       |
| max-height                        | max height of scrollbar                                                                                                         | **string** / **number**                                               | —       |
| native                            | whether to use the native scrollbar style                                                                                       | **boolean**                                                          | false   |
| wrap-style                        | style of wrap container                                                                                                         | **string** / **object**`CSSProperties \| CSSProperties[] \| string[]` | —       |
| wrap-class                        | class of wrap container                                                                                                         | **string**                                                           | —       |
| view-style                        | style of view                                                                                                                   | **string** / **object**`CSSProperties \| CSSProperties[] \| string[]` | —       |
| view-class                        | class of view                                                                                                                   | **string**                                                           | —       |
| noresize                          | do not respond to container size changes, if the container size does not change, it is better to set it to optimize performance | **boolean**                                                          | false   |
| tag                               | element tag of the view                                                                                                         | **string**                                                           | div     |
| always                            | always show scrollbar                                                                                                           | **boolean**                                                          | false   |
| min-size                          | minimum size of scrollbar                                                                                                       | **number**                                                           | 20      |
| id (since 2.4.0)                       | id of view                                                                                                                      | **string**                                                           | —       |
| role (since 2.4.0) (a11y)             | role of view                                                                                                                    | **string**                                                           | —       |
| aria-label (since 2.4.0) (a11y)       | aria-label of view                                                                                                              | **string**                                                           | —       |
| aria-orientation (since 2.4.0) (a11y) | aria-orientation of view                                                                                                        | **enum**`'horizontal' \| 'vertical'`                                 | —       |
| tabindex (since 2.8.3)                 | tabindex of wrap container                                                                                                      | **number** / **string**                                               | —       |
| distance (since 2.10.5)                | trigger end-reached event distance(px)                                                                                          | **number**                                                           | 0       |

### Events

| Name                  | Description                                           | Type                                                                     |
| --------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------ |
| scroll                | triggers when scrolling, return distance of scrolling | **Function**`({ scrollLeft: number, scrollTop: number }) => void`         |
| end-reached (since 2.10.0) | triggers when the end of a scroll is triggered        | **Function**`(direction: 'top' \| 'bottom' \| 'left' \| 'right') => void` |

### Slots

| Name    | Description               |
| ------- | ------------------------- |
| default | customize default content |

### Exposes

| Name          | Description                                | Type                                                                       |
| ------------- | ------------------------------------------ | -------------------------------------------------------------------------- |
| handleScroll  | handle scroll event                        | **Function**`() => void`                                                    |
| scrollTo      | scrolls to a particular set of coordinates | **Function**`(options: ScrollToOptions \| number, yCoord?: number) => void` |
| setScrollTop  | Set distance to scroll top                 | **Function**`(scrollTop: number) => void`                                   |
| setScrollLeft | Set distance to scroll left                | **Function**`(scrollLeft: number) => void`                                  |
| update        | update scrollbar state manually            | **Function**`() => void`                                                    |
| wrapRef       | scrollbar wrap ref                         | **object**`Ref<HTMLDivElement>`                                             |
