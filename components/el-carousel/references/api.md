# carousel API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/carousel.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Carousel API

### Carousel Attributes

| Name                 | Description                                           | Type                                    | Default    |
| -------------------- | ----------------------------------------------------- | --------------------------------------- | ---------- |
| height               | height of the carousel                                | **string**                               | ''         |
| initial-index        | index of the initially active slide (starting from 0) | **number**                               | 0          |
| trigger              | how indicators are triggered                          | **enum**`'hover' \| 'click'`             | hover      |
| autoplay             | whether automatically loop the slides                 | **boolean**                              | true       |
| interval             | interval of the auto loop, in milliseconds            | **number**                               | 3000       |
| indicator-position   | position of the indicators                            | **enum**`'' \| 'none' \| 'outside'`      | ''         |
| arrow                | when arrows are shown                                 | **enum**`'always' \| 'hover' \| 'never'` | hover      |
| type                 | type of the Carousel                                  | **enum**`'' \| 'card'`                   | ''         |
| card-scale (since 2.7.8)  | when type is card, scaled size of secondary cards     | **number**                               | 0.83       |
| loop                 | display the items in loop                             | **boolean**                              | true       |
| direction            | display direction                                     | **enum**`'horizontal' \| 'vertical'`     | horizontal |
| pause-on-hover       | pause autoplay when hover                             | **boolean**                              | true       |
| motion-blur (since 2.6.0) | infuse dynamism and smoothness into the carousel      | **boolean**                              | false      |

### Carousel Events

| Name   | Description                                                                                                                                              | Type                                                 |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| change | triggers when the active slide switches, it has two parameters, the one is the index of the new active slide, and other is index of the old active slide | **Function**`(current: number, prev: number) => void` |

### Carousel Slots

| Name    | Description               | Subtags       |
| ------- | ------------------------- | ------------- |
| default | customize default content | Carousel-Item |

### Carousel Exposes

| Method               | Description                                                                                                                     | Type                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| activeIndex (since 2.7.8) | active slide index                                                                                                              | **number**                                      |
| setActiveItem        | manually switch slide, index of the slide to be switched to, starting from 0; or the `name` of corresponding `el-carousel-item` | **Function**`(index: string \| number) => void` |
| prev                 | switch to the previous slide                                                                                                    | **Function**`() => void`                        |
| next                 | switch to the next slide                                                                                                        | **Function**`() => void`                        |

## Carousel-Item API

### Carousel-Item Attributes

| Name  | Description                                      | Type                  | Default |
| ----- | ------------------------------------------------ | --------------------- | ------- |
| name  | name of the item, can be used in `setActiveItem` | **string**             | ''      |
| label | text content for the corresponding indicator     | **string** / **number** | ''      |

### Carousel-Item Slots

| Name    | Description               |
| ------- | ------------------------- |
| default | customize default content |
