# segmented API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/segmented.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                     | Description                                    | Type                                           | Default    |
| ------------------------ | ---------------------------------------------- | ---------------------------------------------- | ---------- |
| model-value / v-model    | binding value                                  | **string** / **number** / **boolean**             | —          |
| options                  | data of the options                            | **array**`Option[]`                             | []         |
| [props](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/segmented.md#props) (since 2.9.8) | configuration options, see the following table | **object**                                      | —          |
| size                     | size of component                              | **enum**`'' \| 'large' \| 'default' \| 'small'` | ''         |
| block                    | fit width of parent content                    | **boolean**                                     | false      |
| disabled                 | whether segmented is disabled                  | **boolean**                                     | false      |
| validate-event           | whether to trigger form validation             | **boolean**                                     | true       |
| name                     | native `name` attribute                        | **string**                                      | —          |
| id                       | native `id` attribute                          | **string**                                      | —          |
| aria-label (a11y)       | native `aria-label` attribute                  | **string**                                      | —          |
| direction (since 2.8.7)       | display direction                              | **enum**`'horizontal' \| 'vertical'`            | horizontal |

### props

| Attribute | Description                                                     | Type      | Default  |
| --------- | --------------------------------------------------------------- | --------- | -------- |
| value     | specify which key of node object is used as the node's value    | **string** | value    |
| label     | specify which key of node object is used as the node's label    | **string** | label    |
| disabled  | specify which key of node object is used as the node's disabled | **string** | disabled |

### Events

| Name   | Description                                                                   | Type                            |
| ------ | ----------------------------------------------------------------------------- | ------------------------------- |
| change | triggers when the selected value changes, the param is current selected value | **Function**`(val: any) => void` |

### Slots

| Name    | Description     | Type                        |
| ------- | --------------- | --------------------------- |
| default | option renderer | **object**`{ item: Option }` |

## Type Declarations

<details>
  <summary>Show declarations</summary>

```ts
type Option = Record<string, any> | string | number | boolean
```

</details>
