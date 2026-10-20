# calendar API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/calendar.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                      | Description                                                                                                                                                    | Type                                                                      | Default |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------- |
| model-value / v-model     | binding value                                                                                                                                                  | **Date**                                                                   | —       |
| range                     | time range, including start time and end time. Start time must be start day of week, end time must be end day of week, the time span cannot exceed two months. | **array**`[Date, Date]`                                                    | —       |
| controller-type (since 2.13.1) | type of the controller for Calendar header                                                                                                                     | **enum**`'button' \| 'select'`                                             | button  |
| formatter (since 2.13.1)       | format label when `controller-type` is 'select'                                                                                                                | **Function**`(value: number, type: 'year' \| 'month') => string \| number` | —       |

### Slots

| Name      | Description                                                                                                                                                                                                                                               | Type                                                                                                                         |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| date-cell | `type` indicates which month the date belongs, optional values are prev-month, current-month, next-month; `isSelected` indicates whether the date is selected; `day` is the formatted date in the format `YYYY-MM-DD`; `date` is date the cell represents | **object**`{ data: { type: 'prev-month' \| 'current-month' \| 'next-month', isSelected: boolean, day: string, date: Date } }` |
| header    | content of the Calendar header                                                                                                                                                                                                                            | **object**`{ date: string }`                                                                                                  |

### Exposes

| Name                        | Description                                                            | Type                                                                                          |
| --------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| selectedDay                 | currently selected date                                                | **object**`ComputedRef<Dayjs \| undefined>`                                                    |
| pickDay                     | select a specific date                                                 | **Function**`(day: dayjs.Dayjs) => void`                                                       |
| selectDate                  | select date                                                            | **Function**`(type: CalendarDateType) => void`                                                 |
| calculateValidatedDateRange | Calculate the validate date range according to the start and end dates | **Function**`(startDayjs: dayjs.Dayjs, endDayjs: dayjs.Dayjs) => [dayjs.Dayjs, dayjs.Dayjs][]` |

## Type Declarations

<details>
  <summary>Show declarations</summary>

```ts
type CalendarDateType =
  'prev-month' | 'next-month' | 'prev-year' | 'next-year' | 'today'
```

</details>
