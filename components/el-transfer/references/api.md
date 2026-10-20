# transfer API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/transfer.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Transfer API

### Transfer Attributes

| Name                        | Description                                                                                                                                                                                                                                                                        | Type                                                               | Default  |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | -------- |
| model-value / v-model       | binding value                                                                                                                                                                                                                                                                      | **array**`Array<string \| number>`                                  | []       |
| data                        | data source                                                                                                                                                                                                                                                                        | **array**`Record<string, any>[]`                                    | []       |
| filterable                  | whether Transfer is filterable                                                                                                                                                                                                                                                     | **boolean**                                                         | false    |
| filter-placeholder          | placeholder for the filter input                                                                                                                                                                                                                                                   | **string**                                                          | —        |
| filter-method               | custom filter method                                                                                                                                                                                                                                                               | **Function**`(query: string, item: Record<string, any>) => boolean` | —        |
| target-order                | order strategy for elements in the target list. If set to `original`, the elements will keep the same order as the data source. If set to `push`, the newly added elements will be pushed to the bottom. If set to `unshift`, the newly added elements will be inserted on the top | **enum**`'original' \| 'push' \| 'unshift'`                         | original |
| titles                      | custom list titles                                                                                                                                                                                                                                                                 | **array**`[string, string]`                                         | []       |
| button-texts                | custom button texts                                                                                                                                                                                                                                                                | **array**`[string, string]`                                         | []       |
| render-content              | custom render function for data items                                                                                                                                                                                                                                              | **object**`renderContent`                                           | —        |
| format                      | texts for checking status in list header                                                                                                                                                                                                                                           | **object**`TransferFormat`                                          | {}       |
| [props](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/transfer.md#type-declarations) | prop aliases for data source                                                                                                                                                                                                                                                       | **object**`TransferPropsAlias`                                      | —        |
| left-default-checked        | key array of initially checked data items of the left list                                                                                                                                                                                                                         | **array**`Array<string \| number>`                                  | []       |
| right-default-checked       | key array of initially checked data items of the right list                                                                                                                                                                                                                        | **array**`Array<string \| number>`                                  | []       |
| validate-event              | whether to trigger form validation                                                                                                                                                                                                                                                 | **boolean**                                                         | true     |
| virtual-scroll (since 2.14.3)    | whether to enable virtual scrolling                                                                                                                                                                                                                                                | **boolean**                                                         | false    |
| item-size (since 2.14.3)         | item height for virtual scrolling                                                                                                                                                                                                                                                  | **number**                                                          | 30       |

### Transfer Events

| Name               | Description                                                                         | Type                                                                                                |
| ------------------ | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| change             | triggers when data items change in the right list                                   | **Function**`(value: TransferKey[], direction: TransferDirection, movedKeys: TransferKey[]) => void` |
| left-check-change  | triggers when end user changes the checked state of any data item in the left list  | **Function**`(value: TransferKey[], movedKeys?: TransferKey[]) => void`                              |
| right-check-change | triggers when end user changes the checked state of any data item in the right list | **Function**`(value: TransferKey[], movedKeys?: TransferKey[]) => void`                              |

### Transfer Slots

| Name                 | Description                                                          | Type                                    |
| -------------------- | -------------------------------------------------------------------- | --------------------------------------- |
| default              | Custom content for data items.                                       | **object**`{ option: TransferDataItem }` |
| left-footer          | content of left list footer                                          | —                                       |
| right-footer         | content of right list footer                                         | —                                       |
| left-empty (since 2.9.0)  | content when left panel is empty or when no data matches the filter  | —                                       |
| right-empty (since 2.9.0) | content when right panel is empty or when no data matches the filter | —                                       |

### Transfer Exposes

| Name       | Description                                 | Type                                            |
| ---------- | ------------------------------------------- | ----------------------------------------------- |
| clearQuery | clear the filter keyword of a certain panel | **Function**`(which: TransferDirection) => void` |
| leftPanel  | left panel ref                              | **object**`Ref<TransferPanelInstance>`           |
| rightPanel | right panel ref                             | **object**`Ref<TransferPanelInstance>`           |

## Transfer Panel API

### Transfer Panel Exposes

| Name  | Description    | Type      |
| ----- | -------------- | --------- |
| query | filter keyword | **string** |

## Type Declarations

<details>
  <summary>Show declarations</summary>

```ts
import type { h as H, VNode } from 'vue'

type TransferKey = string | number

type TransferDirection = 'left' | 'right'

type TransferDataItem = Record<string, any>

type renderContent<T extends TransferDataItem = TransferDataItem> = (
  h: typeof H,
  option: T
) => VNode | VNode[]

interface TransferFormat {
  noChecked?: string
  hasChecked?: string
}

interface TransferPropsAlias {
  label?: string
  key?: string
  disabled?: string
}
```

</details>
