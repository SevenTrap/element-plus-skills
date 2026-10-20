# descriptions API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/descriptions.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Descriptions API

### Descriptions Attributes

| Name                 | Description                                | Type                                           | Default    |
| -------------------- | ------------------------------------------ | ---------------------------------------------- | ---------- |
| border               | with or without border                     | **boolean**                                     | false      |
| column               | numbers of `Descriptions Item` in one line | **number**                                      | 3          |
| direction            | direction of list                          | **enum**`'vertical' \| 'horizontal'`            | horizontal |
| size                 | size of list                               | **enum**`'' \| 'large' \| 'default' \| 'small'` | —          |
| title                | title text, display on the top left        | **string**                                      | ''         |
| extra                | extra text, display on the top right       | **string**                                      | ''         |
| label-width (since 2.8.8) | label width of every column                | **string** / **number**                          | —          |

### Descriptions Slots

| Name    | Description                                 | Subtags           |
| ------- | ------------------------------------------- | ----------------- |
| default | customize default content                   | Descriptions Item |
| title   | custom title, display on the top left       | —                 |
| extra   | custom extra area, display on the top right | —                 |

## DescriptionsItem API

### DescriptionsItem Attributes

| Name                 | Description                                                                                                                                                                                  | Type                                   | Default |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ------- |
| label                | label text                                                                                                                                                                                   | **string**                              | ''      |
| span                 | colspan of column                                                                                                                                                                            | **number**                              | 1       |
| rowspan (since 2.8.1)     | the number of rows a cell should span                                                                                                                                                        | **number**                              | 1       |
| width                | column width, the width of the same column in different rows is set by the max value (If no `border`, width contains label and content)                                                      | **string** / **number**                  | ''      |
| min-width            | column minimum width, columns with `width` has a fixed width, while columns with `min-width` has a width that is distributed in proportion (If no`border`, width contains label and content) | **string** / **number**                  | ''      |
| label-width (since 2.8.8) | column label width, if not set, it will be the same as the width of the column. Higher priority than the `label-width` of `Descriptions`                                                     | **string** / **number**                  | —       |
| align                | column content alignment (If no `border`, effective for both label and content)                                                                                                              | **enum**`'left' \| 'center' \| 'right'` | left    |
| label-align          | column label alignment, if omitted, the value of the above `align` attribute will be applied (If no `border`, please use `align` attribute)                                                  | **enum**`'left' \| 'center' \| 'right'` | —       |
| class-name           | column content custom class name                                                                                                                                                             | **string**                              | ''      |
| label-class-name     | column label custom class name                                                                                                                                                               | **string**                              | ''      |

### DescriptionsItem Slots

| Name    | Description               |
| ------- | ------------------------- |
| default | customize default content |
| label   | custom label              |
