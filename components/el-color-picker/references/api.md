# color-picker API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/color-picker.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                        | Description                                                                                        | Type                                                                                                  | Default                                                                      |
| --------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| model-value / v-model       | binding value                                                                                      | **string**                                                                                             | —                                                                            |
| disabled                    | whether to disable the ColorPicker                                                                 | **boolean**                                                                                            | false                                                                        |
| clearable (since 2.13.1)         | whether to show clear button                                                                       | **boolean**                                                                                            | true                                                                         |
| size                        | size of ColorPicker                                                                                | **enum**`'large' \| 'default' \| 'small'`                                                              | —                                                                            |
| show-alpha                  | whether to display the alpha slider                                                                | **boolean**                                                                                            | false                                                                        |
| color-format                | color format of v-model                                                                            | **enum**`'rgb' \| 'prgb' \| 'hex' \| 'hex3' \| 'hex4' \| 'hex6' \| 'hex8' \| 'name' \| 'hsl' \| 'hsv'` | **enum**`'hex' (when show-alpha is false) \| 'rgb' (when show-alpha is true)` |
| popper-class                | custom class name for ColorPicker's dropdown                                                       | **string** / **object**                                                                                 | ''                                                                           |
| popper-style (since 2.11.4)      | custom style for ColorPicker's dropdown                                                            | **string** / **object**                                                                                 | —                                                                            |
| predefine                   | predefined color options                                                                           | **array**`string[]`                                                                                    | —                                                                            |
| validate-event              | whether to trigger form validation                                                                 | **boolean**                                                                                            | true                                                                         |
| tabindex                    | ColorPicker tabindex                                                                               | **string** / **number**                                                                                 | 0                                                                            |
| aria-label (a11y) (since 2.7.2) | ColorPicker aria-label                                                                             | **string**                                                                                             | —                                                                            |
| empty-values (since 2.10.3)      | empty values of component, [see config-provider](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/config-provider.md#empty-values-configurations) | **array**                                                                                              | —                                                                            |
| value-on-clear (since 2.10.3)    | clear return value, [see config-provider](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/config-provider.md#empty-values-configurations)        | **string** / **number** / **boolean** / **Function**                                                      | —                                                                            |
| id                          | ColorPicker id                                                                                     | **string**                                                                                             | —                                                                            |
| teleported (since 2.7.2)         | whether color-picker popper is teleported to the body                                              | **boolean**                                                                                            | true                                                                         |
| persistent (since 2.10.5)        | when color-picker inactive and persistent is false, the color panel will be destroyed              | **boolean**                                                                                            | true                                                                         |
| append-to (since 2.10.5)         | which element the color-picker panel appends to                                                    | **CSSSelector** / **HTMLElement**                                                                       | -                                                                            |

### Events

| Name            | Description                                    | Type                                     |
| --------------- | ---------------------------------------------- | ---------------------------------------- |
| change          | triggers when input value changes              | **Function**`(value: string) => void`     |
| active-change   | triggers when the current active color changes | **Function**`(value: string) => void`     |
| focus (since 2.4.0)  | triggers when Component focuses                | **Function**`(event: FocusEvent) => void` |
| blur (since 2.4.0)   | triggers when Component blurs                  | **Function**`(event: FocusEvent) => void` |
| clear (since 2.13.1) | triggers when the clear button is clicked      | **Function**`() => void`                  |

### Exposes

| Name            | Description               | Type                    |
| --------------- | ------------------------- | ----------------------- |
| color           | current color object      | **object**`Color`        |
| show (since 2.3.3)   | manually show ColorPicker | **Function**`() => void` |
| hide (since 2.3.3)   | manually hide ColorPicker | **Function**`() => void` |
| focus (since 2.3.13) | focus the picker element  | **Function**`() => void` |
| blur (since 2.3.13)  | blur the picker element   | **Function**`() => void` |
