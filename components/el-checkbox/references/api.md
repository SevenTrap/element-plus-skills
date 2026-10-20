# checkbox API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/checkbox.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Checkbox API

### Checkbox Attributes

| Name                           | Description                                                                                                                                                    | Type                                           | Default |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ------- |
| model-value / v-model          | binding value                                                                                                                                                  | **string** / **number** / **boolean**             | —       |
| value (since 2.6.0)                 | value of the Checkbox when used inside a `checkbox-group`                                                                                                      | **string** / **number** / **boolean** / **object** | —       |
| label                          | label of the Checkbox when used inside a `checkbox-group`. If there's no value, `label` will act as `value`                                                    | **string** / **number** / **boolean** / **object** | —       |
| true-value (since 2.6.0)            | value of the Checkbox if it's checked                                                                                                                          | **string** / **number**                          | —       |
| false-value (since 2.6.0)           | value of the Checkbox if it's not checked                                                                                                                      | **string** / **number**                          | —       |
| disabled                       | whether the Checkbox is disabled                                                                                                                               | **boolean**                                     | false   |
| border                         | whether to add a border around Checkbox                                                                                                                        | **boolean**                                     | false   |
| size                           | size of the Checkbox                                                                                                                                           | **enum**`'large' \| 'default' \| 'small'`       | —       |
| name                           | native 'name' attribute                                                                                                                                        | **string**                                      | —       |
| checked                        | if the Checkbox is checked                                                                                                                                     | **boolean**                                     | false   |
| indeterminate                  | Set indeterminate state, only responsible for style control                                                                                                    | **boolean**                                     | false   |
| validate-event                 | whether to trigger form validation                                                                                                                             | **boolean**                                     | true    |
| tabindex                       | input tabindex                                                                                                                                                 | **string** / **number**                          | —       |
| id                             | input id                                                                                                                                                       | **string**                                      | —       |
| aria-controls (a11y) (since 2.7.2) | same as [aria-controls](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-controls), takes effect when `indeterminate` is `true` | **string**                                      | —       |
| aria-label (a11y)             | native `aria-label` attribute                                                                                                                                  | **string**                                      | —       |
| true-label (deprecated)       | value of the Checkbox if it's checked                                                                                                                          | **string** / **number**                          | —       |
| false-label (deprecated)      | value of the Checkbox if it's not checked                                                                                                                      | **string** / **number**                          | —       |

### Checkbox Events

| Name   | Description                             | Type                                                      |
| ------ | --------------------------------------- | --------------------------------------------------------- |
| change | triggers when the binding value changes | **Function**`(value: string \| number \| boolean) => void` |

### Checkbox Slots

| Name    | Description               |
| ------- | ------------------------- |
| default | customize default content |

## CheckboxGroup API

### CheckboxGroup Attributes

| Name                        | Description                                                                                    | Type                                                            | Default                                                  |
| --------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------- |
| model-value / v-model       | binding value                                                                                  | **array**`string[] \| number[]`                                  | []                                                       |
| size                        | size of checkbox                                                                               | **enum**`'large' \| 'default' \| 'small'`                        | —                                                        |
| disabled                    | whether the nesting checkboxes are disabled                                                    | **boolean**                                                      | false                                                    |
| min                         | minimum number of checkbox checked                                                             | **number**                                                       | —                                                        |
| max                         | maximum number of checkbox checked                                                             | **number**                                                       | —                                                        |
| aria-label (a11y) (since 2.7.2) | native `aria-label` attribute                                                                  | **string**                                                       | —                                                        |
| text-color                  | font color when button is active                                                               | **string**                                                       | #ffffff                                                  |
| fill                        | border and background color when button is active                                              | **string**                                                       | #409eff                                                  |
| tag                         | element tag of the checkbox group                                                              | **string**                                                       | div                                                      |
| validate-event              | whether to trigger form validation                                                             | **boolean**                                                      | true                                                     |
| options (since 2.11.2)           | data of the options, the key of `value` and `label` and `disabled` can be customize by `props` | **array**`Array<{[key: string]: any}>`                           | —                                                        |
| props (since 2.11.2)             | configuration options                                                                          | **object**`{ value?: string, label?: string, disabled?: string}` | `{value: 'value', label: 'label', disabled: 'disabled'}` |
| type (since 2.11.5)              | component type to render options (e.g. `'button'`)                                             | **enum**`'checkbox' \| 'button'`                                 | 'checkbox'                                               |

### CheckboxGroup Events

| Name   | Description                             | Type                                               |
| ------ | --------------------------------------- | -------------------------------------------------- |
| change | triggers when the binding value changes | **Function**`(value: string[] \| number[]) => void` |

### CheckboxGroup Slots

| Name    | Description               | Subtags                    |
| ------- | ------------------------- | -------------------------- |
| default | customize default content | Checkbox / Checkbox-button |

## CheckboxButton API

### CheckboxButton Attributes

| Name                      | Description                                                                                                 | Type                                           | Default |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ------- |
| value (since 2.6.0)            | value of the checkbox when used inside a `checkbox-group`                                                   | **string** / **number** / **boolean** / **object** | —       |
| label                     | label of the checkbox when used inside a `checkbox-group`. If there's no value, `label` will act as `value` | **string** / **number** / **boolean** / **object** | —       |
| true-value (since 2.6.0)       | value of the checkbox if it's checked                                                                       | **string** / **number**                          | —       |
| false-value (since 2.6.0)      | value of the checkbox if it's not checked                                                                   | **string** / **number**                          | —       |
| disabled                  | whether the checkbox is disabled                                                                            | **boolean**                                     | false   |
| name                      | native 'name' attribute                                                                                     | **string**                                      | —       |
| checked                   | if the checkbox is checked                                                                                  | **boolean**                                     | false   |
| true-label (deprecated)  | value of the checkbox if it's checked                                                                       | **string** / **number**                          | —       |
| false-label (deprecated) | value of the checkbox if it's not checked                                                                   | **string** / **number**                          | —       |

### CheckboxButton Slots

| Name    | Description               |
| ------- | ------------------------- |
| default | customize default content |
