# input-tag API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/input-tag.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                            | Description                                                                                                    | Type                                                        | Default     |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ----------- |
| model-value / v-model           | binding value                                                                                                  | **array**`string[]`                                          | —           |
| max                             | max number tags that can be enter                                                                              | **number**                                                   | —           |
| tag-type                        | tag type                                                                                                       | **enum**`'' \| 'success' \| 'info' \| 'warning' \| 'danger'` | info        |
| tag-effect                      | tag effect                                                                                                     | **enum**`'' \| 'light' \| 'dark' \| 'plain'`                 | light       |
| effect (since 2.13.2)                | tooltip theme, built-in theme: `dark` / `light`                                                                | **enum**`'dark' \| 'light'` / **string**                      | light       |
| trigger                         | the key to trigger input tag                                                                                   | **enum**`'Enter' \| 'Space'`                                 | Enter       |
| draggable                       | whether tags can be dragged                                                                                    | **boolean**                                                  | false       |
| delimiter (since 2.9.9)              | add a tag when a delimiter is matched                                                                          | **string** / **regex**                                        | —           |
| size                            | input box size                                                                                                 | **enum**`'large' \| 'default' \| 'small'`                    | —           |
| collapse-tags (since 2.11.0)         | whether to collapse tags to a text when multiple selecting                                                     | **boolean**                                                  | false       |
| collapse-tags-tooltip (since 2.11.0) | whether show all selected tags when mouse hover text of collapse-tags. To use this, collapse-tags must be true | **boolean**                                                  | false       |
| save-on-blur (since 2.9.7)           | whether to save the input value when the input loses focus                                                     | **boolean**                                                  | true        |
| clearable                       | whether to show clear button                                                                                   | **boolean**                                                  | false       |
| clear-icon (since 2.11.0)            | custom clear icon component                                                                                    | **string** / **object**`Component`                            | CircleClose |
| disabled                        | whether to disable input-tag                                                                                   | **boolean**                                                  | false       |
| validate-event                  | whether to trigger form validation                                                                             | **boolean**                                                  | true        |
| readonly                        | same as `readonly` in native input                                                                             | **boolean**                                                  | false       |
| autofocus                       | same as `autofocus` in native input                                                                            | **boolean**                                                  | false       |
| id                              | same as `id` in native input                                                                                   | **string**                                                   | —           |
| tabindex                        | same as `tabindex` in native input                                                                             | **string** / **number**                                       | —           |
| max-collapse-tags (since 2.11.0)     | the max tags number to be shown. To use this, collapse-tags must be true                                       | **number**                                                   | 1           |
| maxlength                       | same as `maxlength` in native input                                                                            | **string** / **number**                                       | —           |
| minlength                       | same as `minlength` in native input                                                                            | **string** / **number**                                       | —           |
| placeholder                     | placeholder of input                                                                                           | **string**                                                   | —           |
| autocomplete                    | same as `autocomplete` in native input                                                                         | **string**                                                   | off         |
| aria-label (a11y)              | native `aria-label` attribute                                                                                  | **string**                                                   | —           |

### Events

| Name               | Description                             | Type                                                                     |
| ------------------ | --------------------------------------- | ------------------------------------------------------------------------ |
| change             | triggers when the modelValue change     | **Function**`(value: string[]) => void`                                   |
| input              | triggers when the input value change    | **Function**`(value: string) => void`                                     |
| add-tag            | triggers when a tag is added            | **Function**`(value: string \| string []) => void`                        |
| remove-tag         | triggers when a tag is removed          | **Function**`(value: string, index: number) => void`                      |
| drag-tag (since 2.11.3) | triggers when a tag is dragged          | **Function**`(oldIndex: number, newIndex: number, value: string) => void` |
| focus              | triggers when InputTag focuses          | **Function**`(event: FocusEvent) => void`                                 |
| blur               | triggers when InputTag blurs            | **Function**`(event: FocusEvent) => void`                                 |
| clear              | triggers when the clear icon is clicked | **Function**`() => void`                                                  |

### Slots

| Name   | Description                | Type                                        |
| ------ | -------------------------- | ------------------------------------------- |
| tag    | content as tag             | **object**`{ value: string, index: number }` |
| prefix | content as InputTag prefix | —                                           |
| suffix | content as InputTag suffix | —                                           |

### Exposes

| Name  | Description             | Type                    |
| ----- | ----------------------- | ----------------------- |
| focus | focus the input element | **Function**`() => void` |
| blur  | blur the input element  | **Function**`() => void` |
