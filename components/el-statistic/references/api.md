# statistic API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/statistic.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Statistic API

### Statistic Attributes

| Attribute         | Description                    | Type                                                                | Default |
| ----------------- | ------------------------------ | ------------------------------------------------------------------- | ------- |
| value             | Numerical content              | **number**                                                           | 0       |
| decimal-separator | Setting the decimal point      | **string**                                                           | .       |
| formatter         | Custom numerical presentation  | **Function**`(value: number) => string \| number`                    | —       |
| group-separator   | Sets the thousandth identifier | **string**                                                           | ,       |
| precision         | numerical precision            | **number**                                                           | 0       |
| prefix            | Sets the prefix of a number    | **string**                                                           | —       |
| suffix            | Sets the suffix of a number    | **string**                                                           | —       |
| title             | Numeric titles                 | **string**                                                           | —       |
| value-style       | Styles numeric values          | **string** / **object**`CSSProperties \| CSSProperties[] \| string[]` | —       |

### Statistic Slots

| Name   | Description                 |
| ------ | --------------------------- |
| prefix | Numeric prefix              |
| suffix | Suffixes for numeric values |
| title  | Numeric titles              |

### Statistic Exposes

| Name         | Description           | Type                             |
| ------------ | --------------------- | -------------------------------- |
| displayValue | current display value | **object**`Ref<string \| number>` |

## Countdown API

### Countdown Attributes

| Attribute   | Description                      | Type                                                                | Default  |
| ----------- | -------------------------------- | ------------------------------------------------------------------- | -------- |
| value       | target time                      | **number** / **Dayjs**                                                | —        |
| format      | Formatting the countdown display | **string**                                                           | HH:mm:ss |
| prefix      | Sets the prefix of a countdown   | **string**                                                           | —        |
| suffix      | Sets the suffix of a countdown   | **string**                                                           | —        |
| title       | countdown titles                 | **string**                                                           | —        |
| value-style | Styles countdown values          | **string** / **object**`CSSProperties \| CSSProperties[] \| string[]` | —        |

### Countdown Events

| Name   | Description                  | Type                                 |
| ------ | ---------------------------- | ------------------------------------ |
| change | Time difference change event | **Function**`(value: number) => void` |
| finish | countdown end event          | **Function**`() => void`              |

### Countdown Slots

| Name   | Description            |
| ------ | ---------------------- |
| prefix | countdown value prefix |
| suffix | countdown value suffix |
| title  | countdown title        |

### Countdown Exposes

| Name         | Description           | Type                   |
| ------------ | --------------------- | ---------------------- |
| displayValue | current display value | **object**`Ref<string>` |
