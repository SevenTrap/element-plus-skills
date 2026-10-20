# affix API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/affix.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                 | Description                                                                                    | Type                            | Default |
| -------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------- | ------- |
| offset               | offset distance                                                                                | **number**                       | 0       |
| position             | position of affix                                                                              | **enum**`'top' \| 'bottom'`      | top     |
| target               | target container (CSS selector)                                                                | **string**                       | —       |
| z-index              | `z-index` of affix                                                                             | **number**                       | 100     |
| teleported (since 2.13.0) | whether affix element is teleported, if `true` it will be teleported to where `append-to` sets | **boolean**                      | false   |
| append-to (since 2.13.0)  | which element the affix element appends to                                                     | **CSSSelector** / **HTMLElement** | body    |

### Events

| Name   | Description                       | Type                                                                |
| ------ | --------------------------------- | ------------------------------------------------------------------- |
| change | triggers when fixed state changed | **Function**`(fixed: boolean) => void`                               |
| scroll | triggers when scrolling           | **Function**`(value: { scrollTop: number, fixed: boolean }) => void` |

### Slots

| Name    | Description               |
| ------- | ------------------------- |
| default | customize default content |

### Exposes

| Name       | Description                 | Type                    |
| ---------- | --------------------------- | ----------------------- |
| update     | update affix state manually | **Function**`() => void` |
| updateRoot | update rootRect info        | **Function**`() => void` |
