# input-number API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/input-number.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                          | Description                                              | Type                                          | Default                 |
| ----------------------------- | -------------------------------------------------------- | --------------------------------------------- | ----------------------- |
| model-value / v-model         | binding value                                            | **number** / **null**                           | —                       |
| min                           | the minimum allowed value                                | **number**                                     | Number.MIN_SAFE_INTEGER |
| max                           | the maximum allowed value                                | **number**                                     | Number.MAX_SAFE_INTEGER |
| step                          | incremental step                                         | **number**                                     | 1                       |
| step-strictly                 | whether input value can only be multiple of step         | **boolean**                                    | false                   |
| precision                     | precision of input value                                 | **number**                                     | —                       |
| size                          | size of the component                                    | **enum**`'large' \| 'default' \| 'small'`      | default                 |
| readonly (since 2.2.16)            | same as `readonly` in native input                       | **boolean**                                    | false                   |
| disabled                      | whether the component is disabled                        | **boolean**                                    | false                   |
| controls                      | whether to enable the control buttons                    | **boolean**                                    | true                    |
| controls-position             | position of the control buttons                          | **enum**`'' \| 'right'`                        | —                       |
| name                          | same as `name` in native input                           | **string**                                     | —                       |
| aria-label (a11y) (since 2.7.2)   | same as `aria-label` in native input                     | **string**                                     | —                       |
| placeholder                   | same as `placeholder` in native input                    | **string**                                     | —                       |
| id                            | same as `id` in native input                             | **string**                                     | —                       |
| value-on-clear (since 2.2.0)       | value should be set when input box is cleared            | **number** / **null** / **enum**`'min' \| 'max'` | —                       |
| validate-event                | whether to trigger form validation                       | **boolean**                                    | true                    |
| inputmode (since 2.10.3)           | same as `inputmode` in native input                      | **string**                                     | —                       |
| align (since 2.10.5)               | alignment for the inner input text                       | **enum**`'left' \| 'center' \| 'right'`        | 'center'                |
| disabled-scientific (since 2.10.5) | disables input of scientific notation (e.g. 'e')         | **boolean**                                    | false                   |
| tabindex (since 2.14.0)            | same as `tabindex` in native input                       | **string** / **number**                         | 0                       |
| formatter (since 2.14.0)           | specifies the format of the value presented in the input | **Function**`(value: string) => string`        | —                       |
| parser (since 2.14.0)              | specifies the value extracted from the formatted input   | **Function**`(value: string) => string`        | —                       |

### Slots

| Name                   | Description                           |
| ---------------------- | ------------------------------------- |
| decrease-icon (since 2.6.3) | custom input box button decrease icon |
| increase-icon (since 2.6.3) | custom input box button increase icon |
| prefix (since 2.8.4)        | content as Input prefix               |
| suffix (since 2.8.4)        | content as Input suffix               |

### Events

| Name   | Description                     | Type                                                                                    |
| ------ | ------------------------------- | --------------------------------------------------------------------------------------- |
| change | triggers when the value changes | **Function**`(currentValue: number \| undefined, oldValue: number \| undefined) => void` |
| blur   | triggers when Input blurs       | **Function**`(event: FocusEvent) => void`                                                |
| focus  | triggers when Input focuses     | **Function**`(event: FocusEvent) => void`                                                |

### Exposes

| Name  | Description                      | Type                    |
| ----- | -------------------------------- | ----------------------- |
| focus | get focus the input component    | **Function**`() => void` |
| blur  | remove focus the input component | **Function**`() => void` |
