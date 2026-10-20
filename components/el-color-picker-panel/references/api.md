# color-picker-panel API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/color-picker-panel.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                       | Description                                | Type                                                                                                  | Default                                                                      |
| -------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| model-value / v-model      | binding value                              | **string**                                                                                             | —                                                                            |
| border                     | whether the color picker panel is bordered | **boolean**                                                                                            | true                                                                         |
| disabled                   | whether to disable the color picker        | **boolean**                                                                                            | false                                                                        |
| show-alpha                 | whether to display the alpha slider        | **boolean**                                                                                            | false                                                                        |
| color-format               | color format of v-model                    | **enum**`'rgb' \| 'prgb' \| 'hex' \| 'hex3' \| 'hex4' \| 'hex6' \| 'hex8' \| 'name' \| 'hsl' \| 'hsv'` | **enum**`'hex' (when show-alpha is false) \| 'rgb' (when show-alpha is true)` |
| predefine                  | predefined color options                   | **array**`string[]`                                                                                    | —                                                                            |
| validate-event (since 2.11.7)   | whether to trigger form validation         | **boolean**                                                                                            | true                                                                         |
| hue-slider-class (since 2.13.6) | class names will be passed to hue-slider   | **object**`string \| string[] \| Record<string, boolean>`                                              | —                                                                            |
| hue-slider-style (since 2.13.6) | styles will be passed to hue-slider        | **string** / **object**`StyleValue`                                                                     | —                                                                            |

### Slots

| Name   | Description                       |
| ------ | --------------------------------- |
| footer | content to append after the Input |

### Exposes

| Name             | Description           | Type                     |
| ---------------- | --------------------- | ------------------------ |
| color            | current color object  | **object**`Color`         |
| inputRef         | custom input ref      | **object**`InputInstance` |
| update (since 2.11.4) | update sub components | **Function**`() => void`  |
