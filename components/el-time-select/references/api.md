# time-select API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/time-select.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                      | Description                                                                                        | Type                                                                                             | Default     |
| ------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ----------- |
| model-value / v-model     | binding value                                                                                      | **string**                                                                                        | —           |
| disabled                  | whether TimeSelect is disabled                                                                     | **boolean**                                                                                       | false       |
| editable                  | whether the input is editable                                                                      | **boolean**                                                                                       | true        |
| clearable                 | whether to show clear button                                                                       | **boolean**                                                                                       | true        |
| include-end-time (since 2.9.3) | whether `end` is included in options                                                               | **boolean**                                                                                       | false       |
| size                      | size of Input                                                                                      | **enum**`'large' \| 'default' \| 'small'`                                                         | default     |
| placeholder               | placeholder in non-range mode                                                                      | **string**                                                                                        | —           |
| name (since 2.13.3)            | same as `name` in native input                                                                     | **string**                                                                                        | —           |
| effect                    | Tooltip theme, built-in theme: `dark` / `light`                                                    | **string** / **enum**`'dark' \| 'light'`                                                           | light       |
| prefix-icon               | custom prefix icon component                                                                       | **string** / **Component**                                                                         | Clock       |
| clear-icon                | custom clear icon component                                                                        | **string** / **Component**                                                                         | CircleClose |
| start                     | start time                                                                                         | **string**                                                                                        | 09:00       |
| end                       | end time                                                                                           | **string**                                                                                        | 18:00       |
| step                      | time step                                                                                          | **string**                                                                                        | 00:30       |
| min-time                  | minimum time, any time before this time will be disabled                                           | **string**                                                                                        | —           |
| max-time                  | maximum time, any time after this time will be disabled                                            | **string**                                                                                        | —           |
| format                    | set format of time                                                                                 | **string** see [formats](https://day.js.org/docs/en/display/format#list-of-all-available-formats) | HH:mm       |
| empty-values (since 2.7.0)     | empty values of component, [see config-provider](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/config-provider.md#empty-values-configurations) | **array**                                                                                         | —           |
| value-on-clear (since 2.7.0)   | clear return value, [see config-provider](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/config-provider.md#empty-values-configurations)        | **string** / **number** / **boolean** / **Function**                                                 | —           |
| popper-class (since 2.11.4)    | custom class name for TimeSelect's dropdown                                                        | **string**                                                                                        | ''          |
| popper-style (since 2.11.4)    | custom style for TimeSelect's dropdown                                                             | **string** / **object**                                                                            | —           |

### Events

| Name           | Description                                                       | Type                                     |
| -------------- | ----------------------------------------------------------------- | ---------------------------------------- |
| change         | triggers when user confirms the value                             | **Function**`(value: string) => void`     |
| blur           | triggers when Input blurs                                         | **Function**`(event: FocusEvent) => void` |
| focus          | triggers when Input focuses                                       | **Function**`(event: FocusEvent) => void` |
| clear (since 2.7.7) | triggers when the clear icon is clicked in a clearable TimeSelect | **Function**`() => void`                  |

### Exposes

| Method | Description               | Type                    |
| ------ | ------------------------- | ----------------------- |
| focus  | focus the Input component | **Function**`() => void` |
| blur   | blur the Input component  | **Function**`() => void` |
