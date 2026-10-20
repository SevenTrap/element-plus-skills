# time-picker API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/time-picker.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                         | Description                                                                                                          | Type                                                                                            | Default                            |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ---------------------------------- |
| model-value / v-model        | binding value, if it is an array, the length should be 2                                                             | **number** / **string** / **object**`Date \| [Date, Date] \| [number, number] \| [string, string]` | ''                                 |
| readonly                     | whether TimePicker is read only                                                                                      | **boolean**                                                                                      | false                              |
| disabled                     | whether TimePicker is disabled                                                                                       | **boolean**                                                                                      | false                              |
| editable                     | whether the input is editable                                                                                        | **boolean**                                                                                      | true                               |
| clearable                    | whether to show clear button                                                                                         | **boolean**                                                                                      | true                               |
| size                         | size of Input                                                                                                        | **enum**`'large' \| 'default' \| 'small'`                                                        | —                                  |
| placeholder                  | placeholder in non-range mode                                                                                        | **string**                                                                                       | ''                                 |
| start-placeholder            | placeholder for the start time in range mode                                                                         | **string**                                                                                       | —                                  |
| end-placeholder              | placeholder for the end time in range mode                                                                           | **string**                                                                                       | —                                  |
| is-range                     | whether to pick a time range                                                                                         | **boolean**                                                                                      | false                              |
| arrow-control                | whether to pick time using arrow buttons                                                                             | **boolean**                                                                                      | false                              |
| popper-class                 | custom class name for TimePicker's dropdown                                                                          | **string**                                                                                       | ''                                 |
| popper-style                 | custom style for TimePicker's dropdown                                                                               | **string** / **object**                                                                           | —                                  |
| popper-options               | Customized popper option see more at [popper.js](https://popper.js.org/docs/v2/)                                     | **object**`Partial<PopperOptions>`                                                               | {}                                 |
| fallback-placements (since 2.8.4) | list of possible positions for Tooltip [popper.js](https://popper.js.org/docs/v2/modifiers/flip/#fallbackplacements) | **array**`Placement[]`                                                                           | ['bottom', 'top', 'right', 'left'] |
| placement (since 2.8.4)           | position of dropdown                                                                                                 | `Placement`                                                                                     | bottom                             |
| range-separator              | range separator                                                                                                      | **string**                                                                                       | '-'                                |
| format                       | format of the displayed value in the input box                                                                       | **string** see [date formats](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/date-picker.md#date-formats)                                     | —                                  |
| default-value                | optional, default date of the calendar                                                                               | **Date** / **array**`[Date, Date]`                                                                | —                                  |
| value-format                 | optional, format of binding value. If not specified, the binding value will be a Date object                         | **string** see [date formats](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/date-picker.md#date-formats)                                     | —                                  |
| id                           | same as `id` in native input                                                                                         | **string** / **array**`[string, string]`                                                          | —                                  |
| name                         | same as `name` in native input                                                                                       | **string**                                                                                       | ''                                 |
| aria-label (a11y) (since 2.7.2)  | same as `aria-label` in native input                                                                                 | **string**                                                                                       | —                                  |
| prefix-icon                  | Custom prefix icon component                                                                                         | **string** / **Component**                                                                        | Clock                              |
| clear-icon                   | Custom clear icon component                                                                                          | **string** / **Component**                                                                        | CircleClose                        |
| disabled-hours               | To specify the array of hours that cannot be selected                                                                | **Function**`(role: string, comparingDate?: Dayjs) => number[]`                                  | —                                  |
| disabled-minutes             | To specify the array of minutes that cannot be selected                                                              | **Function**`(hour: number, role: string, comparingDate?: Dayjs) => number[]`                    | —                                  |
| disabled-seconds             | To specify the array of seconds that cannot be selected                                                              | **Function**`(hour: number, minute: number, role: string, comparingDate?: Dayjs) => number[]`    | —                                  |
| teleported                   | whether time-picker dropdown is teleported to the body                                                               | **boolean**                                                                                      | true                               |
| tabindex                     | input tabindex                                                                                                       | **string** / **number**                                                                           | 0                                  |
| empty-values (since 2.7.0)        | empty values of component, [see config-provider](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/config-provider.md#empty-values-configurations)                   | **array**                                                                                        | —                                  |
| value-on-clear (since 2.7.0)      | clear return value, [see config-provider](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/config-provider.md#empty-values-configurations)                          | **string** / **number** / **boolean** / **Function**                                                | —                                  |
| save-on-blur (since 2.13.4)       | Whether to auto-fill the input with the current time on focus when no value is selected                              | **boolean**                                                                                      | true                               |

### Events

| Name           | Description                                                       | Type                                                                                                         |
| -------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| change         | triggers when user confirms the value                             | **Function**`(val: number \| string \| Date \| [number, number] \| [string, string] \| [Date, Date]) => void` |
| blur           | triggers when Input blurs                                         | **Function**`(e: FocusEvent) => void`                                                                         |
| focus          | triggers when Input focuses                                       | **Function**`(e: FocusEvent) => void`                                                                         |
| clear (since 2.7.7) | triggers when the clear icon is clicked in a clearable TimePicker | **Function**`() => void`                                                                                      |
| visible-change | triggers when the TimePicker's dropdown appears/disappears        | **Function**`(visibility: boolean) => void`                                                                   |

### Exposes

| Name                  | Description                    | Type                    |
| --------------------- | ------------------------------ | ----------------------- |
| focus                 | focus the TimePicker component | **Function**`() => void` |
| blur                  | blur the TimePicker component  | **Function**`() => void` |
| handleOpen (since 2.2.16)  | open the TimePicker popper     | **Function**`() => void` |
| handleClose (since 2.2.16) | close the TimePicker popper    | **Function**`() => void` |

## Type Declarations

<details>
  <summary>Show declarations</summary>

```ts
type Placement =
  | 'top'
  | 'top-start'
  | 'top-end'
  | 'bottom'
  | 'bottom-start'
  | 'bottom-end'
  | 'left'
  | 'left-start'
  | 'left-end'
  | 'right'
  | 'right-start'
  | 'right-end'
```

</details>
