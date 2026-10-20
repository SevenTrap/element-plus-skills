# slider API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/slider.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                        | Description                                                                                                                                          | Type                                                                                                                                                                        | Default |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| model-value / v-model       | binding value                                                                                                                                        | **number** / **array**`number[]`                                                                                                                                              | 0       |
| min                         | minimum value                                                                                                                                        | **number**                                                                                                                                                                   | 0       |
| max                         | maximum value                                                                                                                                        | **number**                                                                                                                                                                   | 100     |
| disabled                    | whether Slider is disabled                                                                                                                           | **boolean**                                                                                                                                                                  | false   |
| step                        | step size, can be a number or `'mark'` (since 2.13.6) to restrict values to marks. When set to `'mark'`, the `marks` attribute must be set                | **number** / **string**`'mark'`                                                                                                                                               | 1       |
| show-input                  | whether to display an input box, works when `range` is false and `step` is not `'mark'`                                                              | **boolean**                                                                                                                                                                  | false   |
| show-input-controls         | whether to display control buttons when `show-input` is true                                                                                         | **boolean**                                                                                                                                                                  | true    |
| size                        | size of the slider wrapper, will not work in vertical mode                                                                                           | **enum**`'' \| 'large' \| 'default' \| 'small'`                                                                                                                              | default |
| input-size                  | size of the input box, when set `size`, the default is the value of `size`                                                                           | **enum**`'' \| 'large' \| 'default' \| 'small'`                                                                                                                              | default |
| show-stops                  | whether to display breakpoints                                                                                                                       | **boolean**                                                                                                                                                                  | false   |
| show-tooltip                | whether to display tooltip value                                                                                                                     | **boolean**                                                                                                                                                                  | true    |
| format-tooltip              | format to display tooltip value                                                                                                                      | **Function**`(value: number) => number \| string`                                                                                                                            | —       |
| range                       | whether to select a range                                                                                                                            | **boolean**                                                                                                                                                                  | false   |
| vertical                    | vertical mode                                                                                                                                        | **boolean**                                                                                                                                                                  | false   |
| height                      | slider height, required in vertical mode                                                                                                             | **string**                                                                                                                                                                   | —       |
| aria-label (a11y) (since 2.7.2) | native `aria-label` attribute                                                                                                                        | **string**                                                                                                                                                                   | —       |
| range-start-label           | when `range` is true, screen reader label for the start of the range                                                                                 | **string**                                                                                                                                                                   | —       |
| range-end-label             | when `range` is true, screen reader label for the end of the range                                                                                   | **string**                                                                                                                                                                   | —       |
| format-value-text           | format to display the `aria-valuenow` attribute for screen readers                                                                                   | **Function**`(value: number) => string`                                                                                                                                      | —       |
| tooltip-class               | custom class name for the tooltip                                                                                                                    | **string**                                                                                                                                                                   | —       |
| placement                   | position of Tooltip                                                                                                                                  | **enum**`'top' \| 'top-start' \| 'top-end' \| 'bottom' \| 'bottom-start' \| 'bottom-end' \| 'left' \| 'left-start' \| 'left-end' \| 'right' \| 'right-start' \| 'right-end'` | top     |
| marks                       | marks, type of key must be `number` and must in closed interval `[min, max]`, each mark can custom style                                             | **object**`SliderMarks`                                                                                                                                                      | —       |
| validate-event              | whether to trigger form validation                                                                                                                   | **boolean**                                                                                                                                                                  | true    |
| persistent (since 2.9.5)         | when slider tooltip inactive and `persistent` is `false` , tooltip will be destroyed. `persistent` always be `false` when `show-tooltip ` is `false` | **boolean**                                                                                                                                                                  | true    |

### Events

| Name   | Description                                                                                                       | Type                                            |
| ------ | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| change | triggers when the value changes (if the mouse is being dragged, this event only fires when the mouse is released) | **Function**`(value: Arrayable<number>) => void` |
| input  | triggers when the data changes (It'll be emitted in real time during sliding)                                     | **Function**`(value: Arrayable<number>) => void` |

## Type Declarations

<details>
  <summary>Show declarations</summary>

```ts
type SliderMarks = Record<number, string | { style: CSSProperties; label: any }>
type Arrayable<T> = T | T[]
```

</details>
