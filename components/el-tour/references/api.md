# tour API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/tour.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Tour API

> **Tip** 
tour-step component configuration with the same name has higher priority

### Tour Attributes

| Property                  | Description                                                                      | Type                                                                                                                                                                        | Default                            |
| ------------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| append-to                 | which element the TourContent appends to                                         | **CSSSelector** / **HTMLElement**                                                                                                                                             | `body`                             |
| show-arrow                | whether to show the arrow                                                        | `boolean`                                                                                                                                                                   | true                               |
| placement                 | position of the guide card relative to the target element                        | **enum**`'top' \| 'top-start' \| 'top-end' \| 'bottom' \| 'bottom-start' \| 'bottom-end' \| 'left' \| 'left-start' \| 'left-end' \| 'right' \| 'right-start' \| 'right-end'` | `bottom`                           |
| content-style             | custom style for content                                                         | `CSSProperties`                                                                                                                                                             | —                                  |
| mask                      | whether to enable masking, change mask style and fill color by pass custom props | `boolean` \| **Object**`{ style?: CSSProperties; color?: string; }`                                                                                                          | `true`                             |
| gap                       | transparent gap between mask and target                                          | `TourGap`                                                                                                                                                                   | **Object**`{ offset: 6, radius: 2}` |
| type                      | type, affects the background color and text color                                | `default` \| `primary`                                                                                                                                                      | `default`                          |
| model-value / v-model     | open tour                                                                        | `boolean`                                                                                                                                                                   | `false`                            |
| current / v-model:current | what is the current step                                                         | `number`                                                                                                                                                                    | `0`                                |
| scroll-into-view-options  | support pass custom scrollIntoView options                                       | `boolean` \| `ScrollIntoViewOptions`                                                                                                                                        | **Object**`{ block: 'center' }`     |
| z-index                   | Tour's zIndex                                                                    | `number`                                                                                                                                                                    | `2001`                             |
| show-close                | whether to show a close button                                                   | `boolean`                                                                                                                                                                   | `true`                             |
| close-icon                | custom close icon, default is Close                                              | `string` \| `Component`                                                                                                                                                     | —                                  |
| close-on-press-escape     | whether the Dialog can be closed by pressing ESC                                 | `boolean`                                                                                                                                                                   | `true`                             |
| target-area-clickable     | whether the target element can be clickable, when using mask                     | `boolean`                                                                                                                                                                   | `true`                             |

### Tour slots

| Name       | Description             | Type                                          |
| ---------- | ----------------------- | --------------------------------------------- |
| default    | tourStep component list | —                                             |
| indicators | custom indicator        | **object**`{ current: number, total: number }` |

### Tour events

| Name   | Description                    | Type                                   |
| ------ | ------------------------------ | -------------------------------------- |
| close  | callback function on shutdown  | **Function**`(current: number) => void` |
| finish | callback function on finished  | **Function**`() => void`                |
| change | callback when the step changes | **Function**`(current: number) => void` |

## TourStep API

### TourStep Attributes

| Property                 | Description                                                                                                                                                                                            | Type                                                                                                                                                                        | Default   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| target                   | get the element the guide card points to. Empty makes it show in center of screen. the string and Function types are supported since (since 2.5.2). the string type is selectors of document.querySelector. | `HTMLElement` \| `string` \| **Function**`() => HTMLElement`                                                                                                                 | —         |
| show-arrow               | whether to show the arrow                                                                                                                                                                              | `boolean`                                                                                                                                                                   | —         |
| title                    | title                                                                                                                                                                                                  | `string`                                                                                                                                                                    | —         |
| description              | description                                                                                                                                                                                            | `string`                                                                                                                                                                    | —         |
| placement                | position of the guide card relative to the target element                                                                                                                                              | **enum**`'top' \| 'top-start' \| 'top-end' \| 'bottom' \| 'bottom-start' \| 'bottom-end' \| 'left' \| 'left-start' \| 'left-end' \| 'right' \| 'right-start' \| 'right-end'` | `bottom`  |
| content-style            | custom style for content                                                                                                                                                                               | `CSSProperties`                                                                                                                                                             | —         |
| mask                     | whether to enable masking, change mask style and fill color by pass custom props                                                                                                                       | `boolean` \| **Object**`{ style?: CSSProperties; color?: string; }`                                                                                                          | —         |
| type                     | type, affects the background color and text color                                                                                                                                                      | `default` \| `primary`                                                                                                                                                      | `default` |
| next-button-props        | properties of the Next button                                                                                                                                                                          | **Object**`{ children: VueNode \| string; onClick: Function }`                                                                                                               | —         |
| prev-button-props        | properties of the previous button                                                                                                                                                                      | **Object**`{ children: VueNode \| string; onClick: Function }`                                                                                                               | —         |
| scroll-into-view-options | support pass custom scrollIntoView options, the default follows the `scrollIntoViewOptions` property of Tour                                                                                           | `boolean` \| `ScrollIntoViewOptions`                                                                                                                                        | —         |
| show-close               | whether to show a close button                                                                                                                                                                         | `boolean`                                                                                                                                                                   | —         |
| close-icon               | custom close icon, default is Close                                                                                                                                                                    | `string` \| `Component`                                                                                                                                                     | —         |

### TourStep slots

| Name    | Description           |
| ------- | --------------------- |
| default | custom description    |
| header  | custom header content |

### TourStep events

| Name  | Description                   | Arguments               |
| ----- | ----------------------------- | ----------------------- |
| close | callback function on shutdown | **Function**`() => void` |
