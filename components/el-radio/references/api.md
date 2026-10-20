# radio API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/radio.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Radio API

### Radio Attributes

| Name                  | Description                                                            | Type                                     | Default |
| --------------------- | ---------------------------------------------------------------------- | ---------------------------------------- | ------- |
| model-value / v-model | binding value                                                          | **string** / **number** / **boolean**       | —       |
| value (since 2.6.0)        | the value of Radio                                                     | **string** / **number** / **boolean**       | —       |
| label                 | the label of Radio. If there's no `value`, `label` will act as `value` | **string** / **number** / **boolean**       | —       |
| disabled              | whether Radio is disabled                                              | **boolean**                               | false   |
| border                | whether to add a border around Radio                                   | **boolean**                               | false   |
| size                  | size of the Radio                                                      | **enum**`'large' \| 'default' \| 'small'` | —       |
| name                  | native `name` attribute                                                | **string**                                | —       |

### Radio Events

| Name   | Description                           | Type                                                      |
| ------ | ------------------------------------- | --------------------------------------------------------- |
| change | triggers when the bound value changes | **Function**`(value: string \| number \| boolean) => void` |

### Radio Slots

| Name    | Description               |
| ------- | ------------------------- |
| default | customize default content |

## RadioGroup API

### RadioGroup Attributes

| Name                        | Description                                                                                    | Type                                                            | Default                                                  |
| --------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------- |
| model-value / v-model       | binding value                                                                                  | **string** / **number** / **boolean**                              | —                                                        |
| size                        | the size of radio buttons or bordered radios                                                   | **string**                                                       | default                                                  |
| disabled                    | whether the nesting radios are disabled                                                        | **boolean**                                                      | false                                                    |
| validate-event              | whether to trigger form validation                                                             | **boolean**                                                      | true                                                     |
| text-color                  | font color when button is active                                                               | **string**                                                       | #ffffff                                                  |
| fill                        | border and background color when button is active                                              | **string**                                                       | #409eff                                                  |
| aria-label (a11y) (since 2.7.2) | same as `aria-label` in RadioGroup                                                             | **string**                                                       | —                                                        |
| name                        | native `name` attribute                                                                        | **string**                                                       | —                                                        |
| id                          | native `id` attribute                                                                          | **string**                                                       | —                                                        |
| options (since 2.11.2)           | data of the options, the key of `value` and `label` and `disabled` can be customize by `props` | **array**`Array<{[key: string]: any}>`                           | —                                                        |
| props (since 2.11.2)             | configuration options                                                                          | **object**`{ value?: string, label?: string, disabled?: string}` | `{value: 'value', label: 'label', disabled: 'disabled'}` |
| type (since 2.11.5)              | component type to render options (e.g. `'button'`)                                             | **enum**`'radio' \| 'button'`                                    | 'radio'                                                  |

### RadioGroup Events

| Name   | Description                           | Type                                                      |
| ------ | ------------------------------------- | --------------------------------------------------------- |
| change | triggers when the bound value changes | **Function**`(value: string \| number \| boolean) => void` |

### RadioGroup Slots

| Name    | Description               | Subtags             |
| ------- | ------------------------- | ------------------- |
| default | customize default content | Radio / RadioButton |

## RadioButton API

### RadioButton Attributes

| Name           | Description                                                            | Type                               | Default |
| -------------- | ---------------------------------------------------------------------- | ---------------------------------- | ------- |
| value (since 2.6.0) | the value of Radio                                                     | **string** / **number** / **boolean** | —       |
| label          | the label of Radio. If there's no `value`, `label` will act as `value` | **string** / **number** / **boolean** | —       |
| disabled       | whether Radio is disabled                                              | **boolean**                         | false   |
| name           | native 'name' attribute                                                | **string**                          | —       |

### RadioButton Slots

| Name    | Description               |
| ------- | ------------------------- |
| default | customize default content |
