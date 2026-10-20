# anchor API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/anchor.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Anchor API

### Anchor Attributes

| Property                   | Description                                                | Type                                  | Default    |
| -------------------------- | ---------------------------------------------------------- | ------------------------------------- | ---------- |
| container                  | Scroll container.                                          | `string` \| `HTMLElement` \| `Window` | —          |
| offset                     | Set the offset of the anchor scroll.                       | `number`                              | 0          |
| bound                      | The offset of the element starting to trigger the anchor.  | `number`                              | 15         |
| duration                   | Set the scroll duration of the container, in milliseconds. | `number`                              | 300        |
| marker                     | Whether to show the marker.                                | **boolean**                            | true       |
| type                       | Set Anchor type.                                           | **enum**`'default' \| 'underline'`     | `default`  |
| direction                  | Set Anchor direction.                                      | **enum**`'vertical' \| 'horizontal'`   | `vertical` |
| select-scroll-top (since 2.9.2) | Scroll whether link is selected at the top                 | **boolean**                            | false      |

### Anchor Events

| Name   | Description                                | Type                                                |
| ------ | ------------------------------------------ | --------------------------------------------------- |
| change | Callback when the step changes             | **Function**`(href: string) => void`                 |
| click  | Triggered when the user clicks on the link | **Function**`(e: MouseEvent, href?: string) => void` |

### Anchor Exposes

| Name     | Description                               | Type                                |
| -------- | ----------------------------------------- | ----------------------------------- |
| scrollTo | Manually scroll to the specific position. | **Function**`(href: string) => void` |

### Anchor Slots

| Name    | Description               |
| ------- | ------------------------- |
| default | AnchorLink component list |

### AnchorLink Attributes

| Property | Description                          | Type     | Default |
| -------- | ------------------------------------ | -------- | ------- |
| title    | The text content of the anchor link. | `string` | —       |
| href     | The address of the anchor link.      | `string` | —       |

### AnchorLink Slots

| Name     | Description                     |
| -------- | ------------------------------- |
| default  | The content of the anchor link. |
| sub-link | Slots for child links.          |
