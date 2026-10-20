# mention API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/mention.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                                 | Description                                                                            | Type                                                                         | Default                                                  |
| ------------------------------------ | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------- |
| options                              | mention options list                                                                   | **array**`MentionOption[]`                                                    | `[]`                                                     |
| props (since 2.11.3)                      | configuration options                                                                  | **object**`MentionOptionProps`                                                | `{value: 'value', label: 'label', disabled: 'disabled'}` |
| prefix                               | prefix character to trigger mentions. The string length must be exactly 1              | **string** \| **array**`string[]`                                              | `'@'`                                                    |
| split                                | character to split mentions. The string length must be exactly 1                       | **string**                                                                    | `' '`                                                    |
| filter-option                        | customize filter option logic                                                          | **false** \| **Function**`(pattern: string, option: MentionOption) => boolean` | —                                                        |
| placement                            | set popup placement                                                                    | **string**`'bottom' \| 'top'`                                                 | `'bottom'`                                               |
| show-arrow                           | whether the dropdown panel has an arrow                                                | **boolean**                                                                   | `false`                                                  |
| offset                               | offset of the dropdown panel                                                           | **number**                                                                    | `0`                                                      |
| whole                                | when backspace is pressed to delete, whether the mention content is deleted as a whole | **boolean**                                                                   | `false`                                                  |
| check-is-whole                       | when backspace is pressed to delete, check if the mention is a whole                   | **Function**`(pattern: string, prefix: string) => boolean`                    | —                                                        |
| loading                              | whether the dropdown panel of mentions is in a loading state                           | **boolean**                                                                   | `false`                                                  |
| model-value / v-model                | input value                                                                            | **string**                                                                    | —                                                        |
| popper-class                         | custom class name for dropdown panel                                                   | **string** / **object**                                                        | ''                                                       |
| popper-style (since 2.11.5)               | custom style for dropdown panel                                                        | **string** / **object**                                                        | —                                                        |
| popper-options                       | [popper.js](https://popper.js.org/docs/v2/) parameters                                 | **object** refer to [popper.js doc](https://popper.js.org/docs/v2/)           | —                                                        |
| [input props](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/input.md#attributes) | —                                                                                      | —                                                                            | —                                                        |

### Events

| Name                              | Description                                                                                 | Type                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| search                            | trigger when prefix hit                                                                     | **Function**`(pattern: string, prefix: string) => void`       |
| select                            | trigger when user select the option                                                         | **Function**`(option: MentionOption, prefix: string) => void` |
| whole-remove (since 2.10.4)            | trigger when a whole mention is removed and `whole` is `true` or `check-is-whole` is `true` | **Function**`(pattern: string, prefix: string) => void`       |
| [input events](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/input.md#events) | —                                                                                           | —                                                            |

### Slots

| Name                            | Description                           | Type                                              |
| ------------------------------- | ------------------------------------- | ------------------------------------------------- |
| label                           | content as option label               | **object**`{ item: MentionOption, index: number }` |
| loading                         | content as option loading             | —                                                 |
| header                          | content at the top of the dropdown    | —                                                 |
| footer                          | content at the bottom of the dropdown | —                                                 |
| [input slots](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/input.md#slots) | —                                     | —                                                 |

### Exposes

| Name                     | Description                   | Type                                    |
| ------------------------ | ----------------------------- | --------------------------------------- |
| input                    | el-input component instance   | **object**`Ref<InputInstance \| null>`   |
| tooltip                  | el-tooltip component instance | **object**`Ref<TooltipInstance \| null>` |
| dropdownVisible (since 2.8.5) | tooltip display status        | **object**`ComputedRef<boolean>`         |

## Type Declarations

<details>
  <summary>Show declarations</summary>

```ts
type MentionOption = {
  value?: string
  label?: string
  disabled?: boolean
  [key: string]: any
}

type MentionOptionProps = {
  value?: string
  label?: string
  disabled?: string
  [key: string]: string | undefined
}
```

</details>
