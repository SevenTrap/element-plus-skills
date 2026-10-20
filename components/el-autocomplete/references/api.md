# autocomplete API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/autocomplete.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                                 | Description                                                                                                                | Type                                                                                     | Default      |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------ |
| model-value / v-model                | binding value                                                                                                              | **string**                                                                                | —            |
| placeholder                          | the placeholder of Autocomplete                                                                                            | **string**                                                                                | —            |
| clearable                            | whether to show clear button                                                                                               | **boolean**                                                                               | false        |
| disabled                             | whether Autocomplete is disabled                                                                                           | **boolean**                                                                               | false        |
| value-key                            | key name of the input suggestion object for display                                                                        | **string**                                                                                | value        |
| debounce                             | debounce delay when typing, in milliseconds                                                                                | **number**                                                                                | 300          |
| placement                            | placement of the popup menu                                                                                                | **enum**`'top' \| 'top-start' \| 'top-end' \| 'bottom' \| 'bottom-start' \| 'bottom-end'` | bottom-start |
| fetch-suggestions                    | a method to fetch input suggestions. When suggestions are ready, invoke `callback(data:[])` to return them to Autocomplete | **array** / **Function**`(queryString: string, callback: callbackfn) => void`              | —            |
| trigger-on-focus                     | whether show suggestions when input focus                                                                                  | **boolean**                                                                               | true         |
| select-when-unmatched                | whether to emit a `select` event on enter when there is no autocomplete match                                              | **boolean**                                                                               | false        |
| name                                 | same as `name` in native input                                                                                             | **string**                                                                                | —            |
| aria-label (a11y) (since 2.7.2)          | native `aria-label` attribute                                                                                              | **string**                                                                                | —            |
| hide-loading                         | whether to hide the loading icon in remote search                                                                          | **boolean**                                                                               | false        |
| popper-class                         | custom class name for autocomplete's dropdown                                                                              | **string** / **object**                                                                    | ''           |
| popper-style (since 2.11.4)               | custom style for autocomplete's dropdown                                                                                   | **string** / **object**                                                                    | —            |
| popper-options (since 2.14.0)             | [popper.js](https://popper.js.org/docs/v2/) parameters                                                                     | **object**refer to [popper.js](https://popper.js.org/docs/v2/) doc                        | {}           |
| show-arrow (since 2.14.0)                 | whether the dropdown has an arrow                                                                                          | **boolean**                                                                               | true         |
| teleported                           | whether select dropdown is teleported to the body                                                                          | **boolean**                                                                               | true         |
| append-to (since 2.9.9)                   | which select dropdown appends to                                                                                           | **CSSSelector** / **HTMLElement**                                                          | —            |
| highlight-first-item                 | whether to highlight first item in remote search suggestions by default                                                    | **boolean**                                                                               | false        |
| fit-input-width                      | whether the width of the dropdown is the same as the input                                                                 | **boolean**                                                                               | false        |
| loop-navigation (since 2.11.4)            | whether keyboard navigation loops from end to start                                                                        | **boolean**                                                                               | true         |
| [input props](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/input.md#attributes) | —                                                                                                                          | —                                                                                        | —            |

### Events

| Name   | Description                                                     | Type                                             |
| ------ | --------------------------------------------------------------- | ------------------------------------------------ |
| blur   | triggers when Input blurs                                       | **Function**`(event: FocusEvent) => void`         |
| focus  | triggers when Input focuses                                     | **Function**`(event: FocusEvent) => void`         |
| input  | triggers when the Input value change                            | **Function**`(value: string \| number) => void`   |
| clear  | triggers when the Input is cleared by clicking the clear button | **Function**`() => void`                          |
| select | triggers when a suggestion is clicked                           | **Function**`(item: Record<string, any>) => void` |
| change | triggers when the icon inside Input value change                | **Function**`(value: string \| number) => void`   |

### Slots

| Name             | Description                           | Type                                     |
| ---------------- | ------------------------------------- | ---------------------------------------- |
| default          | custom content for input suggestions  | **object**`{ item: Record<string, any> }` |
| header (since 2.10.6) | content at the top of the dropdown    | -                                        |
| footer (since 2.10.6) | content at the bottom of the dropdown | -                                        |
| prefix           | content as Input prefix               | -                                        |
| suffix           | content as Input suffix               | -                                        |
| prepend          | content to prepend before Input       | -                                        |
| append           | content to append after Input         | -                                        |
| loading (since 2.5.0) | override loading content              | -                                        |

### Exposes

| Name             | Description                                 | Type                                                |
| ---------------- | ------------------------------------------- | --------------------------------------------------- |
| activated        | if autocomplete activated                   | **object**`Ref<boolean>`                             |
| blur             | blur the input element                      | **Function**`() => void`                             |
| close            | collapse suggestion list                    | **Function**`() => void`                             |
| focus            | focus the input element                     | **Function**`() => void`                             |
| handleSelect     | triggers when a suggestion is clicked       | **Function**`(item: any) => Promise<void>`           |
| handleKeyEnter   | handle keyboard enter event                 | **Function**`() => Promise<void>`                    |
| highlightedIndex | the index of the currently highlighted item | **object**`Ref<number>`                              |
| highlight        | highlight an item in a suggestion           | **Function**`(itemIndex: number) => void`            |
| inputRef         | el-input component instance                 | **object**`Ref<ElInputInstance>`                     |
| loading          | remote search loading indicator             | **object**`Ref<boolean>`                             |
| popperRef        | el-tooltip component instance               | **object**`Ref<ElTooltipInstance>`                   |
| suggestions      | fetch suggestions result                    | **object**`Ref<record<string, any>[]>`               |
| getData (since 2.8.4) | loading suggestion list                     | **Function**`(queryString: string) => Promise<void>` |
