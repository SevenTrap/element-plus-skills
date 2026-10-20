# date-picker API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/date-picker.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                         | Description                                                                                                                           | Type                                                                                                                                                                                                        | Default                            |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| model-value / v-model        | binding value, if it is an `range` picker, the length of the array should be 2                                                        | **number** / **string** / **Date** / **array**`number[] \| string[] \| Date[]`                                                                                                                                  | ''                                 |
| readonly                     | whether DatePicker is read only                                                                                                       | **boolean**                                                                                                                                                                                                  | false                              |
| disabled                     | whether DatePicker is disabled                                                                                                        | **boolean**                                                                                                                                                                                                  | false                              |
| size                         | size of Input                                                                                                                         | **enum**`'' \| 'large' \| 'default' \| 'small'`                                                                                                                                                              | —                                  |
| editable                     | whether the input is editable                                                                                                         | **boolean**                                                                                                                                                                                                  | true                               |
| clearable                    | whether to show clear button                                                                                                          | **boolean**                                                                                                                                                                                                  | true                               |
| placeholder                  | placeholder in non-range mode                                                                                                         | **string**                                                                                                                                                                                                   | ''                                 |
| start-placeholder            | placeholder for the start date in range mode                                                                                          | **string**                                                                                                                                                                                                   | —                                  |
| end-placeholder              | placeholder for the end date in range mode                                                                                            | **string**                                                                                                                                                                                                   | —                                  |
| type                         | type of the picker. `quarter`, `quarters`, and `quarterrange` are supported since (since 2.14.5)                                           | **enum**`'year' \| 'years' \|'month' \| 'months' \| 'date' \| 'dates' \| 'datetime' \| 'week' \| 'quarter' \| 'quarters' \| 'datetimerange' \| 'daterange' \| 'monthrange' \| 'yearrange' \| 'quarterrange'` | date                               |
| format                       | format of the displayed value in the input box                                                                                        | **string** see [date formats](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/date-picker.md#date-formats)                                                                                                                                                                 | YYYY-MM-DD                         |
| popper-class                 | custom class name for DatePicker's dropdown                                                                                           | **string**                                                                                                                                                                                                   | —                                  |
| popper-style                 | custom style for DatePicker's dropdown                                                                                                | **string** / **object**                                                                                                                                                                                       | —                                  |
| popper-options               | Customized popper option see more at [popper.js](https://popper.js.org/docs/v2/)                                                      | **object**`Partial<PopperOptions>`                                                                                                                                                                           | {}                                 |
| range-separator              | range separator                                                                                                                       | **string**                                                                                                                                                                                                   | '-'                                |
| default-value                | optional, default date of the calendar                                                                                                | **object**`Date \| [Date, Date]`                                                                                                                                                                             | —                                  |
| default-time                 | optional, the time value to use when selecting date range                                                                             | **object**`Date \| [Date, Date]`                                                                                                                                                                             | —                                  |
| value-format                 | optional, format of binding value. If not specified, the binding value will be a Date object                                          | **string** see [date formats](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/date-picker.md#date-formats)                                                                                                                                                                 | —                                  |
| id                           | same as `id` in native input                                                                                                          | **string** / **array**`[string, string]`                                                                                                                                                                      | —                                  |
| name                         | same as `name` in native input                                                                                                        | **string** / **array**`[string, string]`                                                                                                                                                                      | ''                                 |
| unlink-panels                | unlink two date-panels in range-picker                                                                                                | **boolean**                                                                                                                                                                                                  | false                              |
| single-panel (since 2.14.0)       | show only one panel in range-picker                                                                                                   | **boolean**                                                                                                                                                                                                  | false                              |
| prefix-icon                  | custom prefix icon component. By default, if the value of `type` is `TimeLikeType`, the value is `Clock`, else is `Calendar`          | **string** / **object**`Component`                                                                                                                                                                            | ''                                 |
| clear-icon                   | custom clear icon component                                                                                                           | **string** / **object**`Component`                                                                                                                                                                            | `CircleClose`                      |
| validate-event               | whether to trigger form validation                                                                                                    | **boolean**                                                                                                                                                                                                  | true                               |
| disabled-date                | a function determining if a date is disabled with that date as its parameter. Should return a Boolean                                 | **Function**`(data: Date) => boolean`                                                                                                                                                                        | —                                  |
| shortcuts                    | an object array to set shortcut options                                                                                               | **array**`Array<{ text: string, value: Date \| Function }>`                                                                                                                                                  | []                                 |
| cell-class-name              | set custom className                                                                                                                  | **Function**`(data: Date) => string`                                                                                                                                                                         | —                                  |
| teleported                   | whether date-picker dropdown is teleported to the body                                                                                | **boolean**                                                                                                                                                                                                  | true                               |
| empty-values (since 2.7.0)        | empty values of component, [see config-provider](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/config-provider.md#empty-values-configurations)                                    | **array**                                                                                                                                                                                                    | —                                  |
| value-on-clear (since 2.7.0)      | clear return value, [see config-provider](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/config-provider.md#empty-values-configurations)                                           | **string** / **number** / **boolean** / **Function**                                                                                                                                                            | —                                  |
| fallback-placements (since 2.8.4) | list of possible positions for Tooltip [popper.js](https://popper.js.org/docs/v2/modifiers/flip/#fallbackplacements)                  | **array**`Placement[]`                                                                                                                                                                                       | ['bottom', 'top', 'right', 'left'] |
| placement (since 2.8.4)           | position of dropdown                                                                                                                  | `Placement`                                                                                                                                                                                                 | bottom                             |
| show-footer (since 2.10.5)        | whether to show footer where the date picker is one **enum**`'dates' \| 'months' \| 'years' \| 'quarters'`                             | **boolean**                                                                                                                                                                                                  | true                               |
| show-confirm (since 2.11.0)       | whether to show the confirm button                                                                                                    | **boolean**                                                                                                                                                                                                  | true                               |
| show-week-number (since 2.10.3)   | show the week number besides the week                                                                                                 | **boolean**                                                                                                                                                                                                  | false                              |
| automatic-dropdown (since 2.11.4) | this prop decides if the date picker panel pops up when the input is focused. (The default value will be set to false in version 3.0) | **boolean**                                                                                                                                                                                                  | true                               |

### Events

| Name            | Description                                                           | Type                                                                                      |
| --------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| change          | triggers when user confirms the value or click outside                | **Function**`(val: typeof v-model) => void`                                                |
| blur            | triggers when Input blurs                                             | **Function**`(e: FocusEvent) => void`                                                      |
| focus           | triggers when Input focuses                                           | **Function**`(e: FocusEvent) => void`                                                      |
| clear (since 2.7.7)  | triggers when a clear button is clicked                               | **Function**`() => void`                                                                   |
| calendar-change | triggers when the calendar selected date is changed. Only for `range` | **Function**`(val: [Date, null \| Date]) => void`                                          |
| panel-change    | triggers when the navigation button click.                            | **Function**`(date: Date \| [Date, Date], mode: 'month' \| 'year', view?: string) => void` |
| visible-change  | triggers when the DatePicker's dropdown appears/disappears            | **Function**`(visibility: boolean) => void`                                                |

### Slots

| Name                | Description                    |
| ------------------- | ------------------------------ |
| default             | custom cell content            |
| range-separator     | custom range separator content |
| prev-month (since 2.8.0) | prev month icon                |
| next-month (since 2.8.0) | next month icon                |
| prev-year (since 2.8.0)  | prev year icon                 |
| next-year (since 2.8.0)  | next year icon                 |

### Exposes

| Name                  | Description                    | Type                    |
| --------------------- | ------------------------------ | ----------------------- |
| focus                 | focus the DatePicker component | **Function**`() => void` |
| blur (since 2.8.7)         | blur the DatePicker component  | **Function**`() => void` |
| handleOpen (since 2.2.16)  | open the DatePicker popper     | **Function**`() => void` |
| handleClose (since 2.2.16) | close the DatePicker popper    | **Function**`() => void` |

## Type Declarations

<details>
  <summary>Show declarations</summary>

```ts
import type { Options as PopperOptions } from '@popperjs/core'

type TimeLikeType = 'datetime' | 'datetimerange'

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
