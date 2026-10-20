# input-otp API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/input-otp.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                  | Description                                                                                                                                | Type                                                      | Default    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------- | ---------- |
| model-value / v-model | The value of the OTP fields. Since numbers must not have leading zeros, `modelValue` is allowed to be a number only during initialization. | **string** / **number**                                     | undefined  |
| length                | The OTP fields length                                                                                                                      | **number**                                                 | 6          |
| validator             | Custom validator function                                                                                                                  | **Function**`(char: string, index: number) => boolean`     | () => true |
| inputmode             | Native `inputmode` attribute                                                                                                               | **string**                                                 | —          |
| type                  | The type of the OTP fields                                                                                                                 | **enum**`'outlined' \| 'filled' \| 'underlined'`           | 'outlined' |
| size                  | The size of the OTP fields                                                                                                                 | **enum**`'large' \| 'default' \| 'small'`                  | —          |
| mask                  | Whether to enable password mode                                                                                                            | **boolean**                                                | —          |
| disabled              | Whether the OTP fields are disabled                                                                                                        | **boolean**                                                | undefined  |
| separator             | The separator between OTP fields                                                                                                           | **string** / **VNode** / **Function**`(index: number) => string \| VNode` | —          |
| validate-event        | Whether to trigger form validation                                                                                                         | **boolean**                                                | true       |
| readonly              | Same as `readonly` in native input                                                                                                         | **boolean**                                                | false      |
| id                    | Native `id` attribute                                                                                                                      | **string**                                                 | —          |
| aria-label (a11y)    | Native `aria-label` attribute                                                                                                              | **string**                                                 | —          |

### Events

| Name              | Description                                      | Type                                     |
| ----------------- | ------------------------------------------------ | ---------------------------------------- |
| update:modelValue | Triggers when value updates                      | **Function**`(value: string) => void`     |
| change            | Triggers when the value changes after input blur | **Function**`(value: string) => void`     |
| finish            | Fires when all fields have been filled           | **Function**`(value: string) => void`     |
| focus             | Triggers when input is focused                   | **Function**`(event: FocusEvent) => void` |
| blur              | Triggers when input is blurred                   | **Function**`(event: FocusEvent) => void` |

### Slots

| Name      | Description                      | Type                         |
| --------- | -------------------------------- | ---------------------------- |
| separator | The separator between OTP fields | **object**`{ index: number }` |

### Exposes

| Name      | Description                      | Type                                              |
| --------- | -------------------------------- | ------------------------------------------------- |
| inputRefs | HTML input elements array        | **object**`Ref<(HTMLInputElement \| undefined)[]>` |
| focus     | Focus an OTP input field         | **Function**`(index?: number) => void`             |
| blur      | Blur the focused OTP input field | **Function**`() => void`                           |

Implementation correction: the `separator` callback receives the field index; see [input-otp.ts](https://github.com/element-plus/element-plus/blob/2.14.6/packages/components/input-otp/src/input-otp.ts). Model updates emit strings.
