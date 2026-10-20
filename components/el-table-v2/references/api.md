# table-v2 API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## TableV2 API

### TableV2 Attributes

| Name                      | Description                                                                                                                | Type                                                   | Default   |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | --------- |
| cache                     | Number of rows rendered in advance to boost the performance                                                                | `number`                                               | 2         |
| estimated-row-height      | The estimated row height for rendering dynamic height rows                                                                 | `number`                                               | —         |
| header-class              | Customized class name passed to header wrapper                                                                             | `string` / Function<[HeaderClassGetter](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)>     | —         |
| header-props              | Customized props name passed to header component                                                                           | `object` / Function<[HeaderPropsGetter](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)>     | —         |
| header-cell-props         | Customized props name passed to header cell component                                                                      | `object` / Function<[HeaderCellPropsGetter](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)> | —         |
| header-height             | The height of the header is set by `height`. If given an array, it renders header rows equal to its length                 | `number`/ `number[]`                                   | 50        |
| footer-height             | The height of the footer element, when provided, will be part to the calculation of the table's height.                    | `number`                                               | 0         |
| row-class                 | Customized class name passed to row wrapper                                                                                | `string` / Function<[RowClassGetter](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)>        | —         |
| row-key                   | The key of each row, if not provided, will be the index of the row                                                         | `string` / `Symbol` / `number`                         | id        |
| row-props                 | Customized props name passed to row component                                                                              | `object` / Function<[RowPropsGetter](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)>        | —         |
| row-height                | The height of each row, used for calculating the total height of the table                                                 | `number`                                               | 50        |
| row-event-handlers        | A collection of handlers attached to each row                                                                              | `object`\<[RowEventHandlers](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)\>               | —         |
| cell-props                | extra props passed to each cell (except header cells)                                                                      | `object` / Function<[CellPropsGetter](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)>       | —         |
| columns                   | An array of column definitions.                                                                                            | [Column[]](#column-attribute)                          | —         |
| data                      | An array of data to be rendered in the table.                                                                              | [Data[]](#typings)                                     | []        |
| data-getter               | A method to customize data fetch from the data source.                                                                     | Function<[DataGetter\<T\>](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)>                  | —         |
| fixed-data                | Data for rendering rows above the main content and below the header                                                        | `object`\<[Data](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)\>                           | —         |
| expand-column-key         | The column key indicates which row is expandable                                                                           | `string`                                               | —         |
| expanded-row-keys         | An array of keys for expanded rows, can be used with `v-model`                                                             | [KeyType[]](#typings)                                  | —         |
| default-expanded-row-keys | An array of keys for default expanded rows, **NON REACTIVE**                                                               | [KeyType[]](#typings)                                  | —         |
| class                     | Class name for the virtual table, will be applied to all three tables (left, right, main)                                  | `string` / `array` / `object`                          | —         |
| fixed                     | Flag indicates the table column's width to be fixed or flexible.                                                           | `boolean`                                              | false     |
| width (required)         | Width of the table                                                                                                         | `number`                                               | —         |
| height (required)        | Height of the table                                                                                                        | `number`                                               | —         |
| max-height                | Maximum height of the table                                                                                                | `number`                                               | —         |
| indent-size               | horizontal indentation of tree table                                                                                       | `number`                                               | 12        |
| h-scrollbar-size          | Indicates the horizontal scrollbar's size for the table, used to prevent the horizontal and vertical scrollbar to collapse | `number`                                               | 6         |
| v-scrollbar-size          | Indicates the vertical scrollbar's size for the table, used to prevent the horizontal and vertical scrollbar to collapse   | `number`                                               | 6         |
| scrollbar-always-on       | If true, the scrollbar will always be shown instead of when mouse is placed above the table                                | `boolean`                                              | false     |
| sort-by                   | Sort indicator                                                                                                             | `object`\<[SortBy](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)\>                         | {}        |
| sort-state                | Multiple sort indicator                                                                                                    | `object`\<[SortState](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)\>                      | undefined |

### TableV2 Slots

| Name        | Type                                        |
| ----------- | ------------------------------------------- |
| cell        | `object`\<[CellSlotProps](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)\>       |
| header      | `object`\<[HeaderSlotProps](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)\>     |
| header-cell | `object`\<[HeaderCellSlotProps](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)\> |
| row         | `object`\<[RowSlotProps](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)\>        |
| footer      | —                                           |
| empty       | —                                           |
| overlay     | —                                           |

### TableV2 Events

| Name                 | Description                                                                                                                     | Parameters                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| column-sort          | Invoked when column sorted                                                                                                      | `object`\<[ColumnSortParam](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)\>       |
| expanded-rows-change | Invoked when expanded rows changed                                                                                              | [KeyType[]](#typings)                         |
| end-reached          | Invoked when the end of the table is reached. The callback contain the remain distance, it is the usually the scrollbar height. | **Function**`(remainDistance: number) => void` |
| scroll               | Invoked after scrolling                                                                                                         | `object`\<[ScrollParams](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)\>          |
| rows-rendered        | Invoked when rows are rendered                                                                                                  | `object`\<[RowsRenderedParams](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)\>    |
| row-expand           | Invoked when expand/collapse the tree node by clicking the arrow icon                                                           | `object`\<[RowExpandParams](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)\>       |

### TableV2 Exposes

| Method       | Description                                          | Parameters                                                                             |
| ------------ | ---------------------------------------------------- | -------------------------------------------------------------------------------------- |
| scrollTo     | Scroll to a given position                           | **Function**`(param: {scrollLeft?: number, scrollTop?: number}) => void`                |
| scrollToLeft | Scroll to a given horizontal position                | **Function**`(scrollLeft: number) => void`                                              |
| scrollToTop  | Scroll to a given vertical position                  | **Function**`(scrollTop: number) => void`                                               |
| scrollToRow  | scroll to a given row with specified scroll strategy | **Function**`(row: number, strategy?: 'center' \| 'end' \| 'start' \| 'smart') => void` |

> **Tip** 

Note that these are `JavaScript` Objects, so you **CANNOT USE** kebab-case for these attributes


### Column Attribute

| Name               | Description                                                           | Type                                                                                                                                                                 | Default |
| ------------------ | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| align              | Alignment of the table cell content                                   | [Alignment](https://github.com/element-plus/element-plus/blob/b92b22932758f0ddea98810ae248f6ca62f77e25/packages/components/table-v2/src/constants.ts#L6)             | left    |
| class              | Class name for the column                                             | `string`                                                                                                                                                             | —       |
| key                | Unique identification                                                 | [KeyType](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)                                                                                                                                                  | —       |
| dataKey            | Unique identification of data                                         | [KeyType](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)                                                                                                                                                  | —       |
| fixed              | Fixed direction of the column                                         | `boolean` / [FixedDir](https://github.com/element-plus/element-plus/blob/b92b22932758f0ddea98810ae248f6ca62f77e25/packages/components/table-v2/src/constants.ts#L11) | false   |
| flexGrow           | CSSProperties flex grow, Only useful when this is not a fixed table   | `number`                                                                                                                                                             | 0       |
| flexShrink         | CSSProperties flex shrink, Only useful when this is not a fixed table | `number`                                                                                                                                                             | 1       |
| headerClass        | Used for customizing header column class                              | `string`                                                                                                                                                             | —       |
| hidden             | Whether the column is invisible                                       | `boolean`                                                                                                                                                            | —       |
| style              | Customized style for column cell, will be merged with grid cell       | **object**`CSSProperties`                                                                                                                                             | —       |
| sortable           | Indicates whether the column is sortable                              | `boolean`                                                                                                                                                            | —       |
| title              | The default text rendered in header cell                              | `string`                                                                                                                                                             | —       |
| maxWidth           | Maximum width for the column                                          | `number`                                                                                                                                                             | —       |
| minWidth           | Minimum width for the column                                          | `number`                                                                                                                                                             | —       |
| width (required)  | Width for the column                                                  | `number`                                                                                                                                                             | —       |
| cellRenderer       | Customized Cell renderer                                              | `VueComponent` / (props: [CellRenderProps](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)) => VNode                                                                                                       | —       |
| headerCellRenderer | Customized Header renderer                                            | `VueComponent` / (props: [HeaderRenderProps](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#typings)) => VNode                                                                                                     | —       |

## Typings{#typings}

<details>
<summary>Show Type Declarations</summary>

```ts
type HeaderClassGetter = (param: {
  columns: Column<any>[]
  headerIndex: number
}) => string

type HeaderPropsGetter = (param: {
  columns: Column<any>[]
  headerIndex: number
}) => Record<string, any>

type HeaderCellPropsGetter = (param: {
  columns: Column<any>[]
  column: Column<any>
  columnIndex: number
  headerIndex: number
  style: CSSProperties
}) => Record<string, any>

type RowClassGetter = (param: {
  columns: Column<any>[]
  rowData: any
  rowIndex: number
}) => string

type RowPropsGetter = (param: {
  columns: Column<any>[]
  rowData: any
  rowIndex: number
}) => Record<string, any>

type CellPropsGetter = (param: {
  column: Column<any>
  columns: Column<any>[]
  columnIndex: number
  cellData: any
  rowData: any
  rowIndex: number
}) => void

type DataGetterParams<T> = {
  columns: Column<T>[]
  column: Column<T>
  columnIndex: number
} & RowCommonParams

type DataGetter<T> = (params: DataGetterParams<T>) => T

type CellRenderProps<T> = {
  cellData: T
  column: Column<T>
  columns: Column<T>[]
  columnIndex: number
  rowData: any
  rowIndex: number
}

type HeaderRenderProps<T> = {
  column: Column<T>
  columns: Column<T>[]
  columnIndex: number
  headerIndex: number
}

type ScrollParams = {
  xAxisScrollDir: 'forward' | 'backward'
  scrollLeft: number
  yAxisScrollDir: 'forward' | 'backward'
  scrollTop: number
}

type CellSlotProps<T> = {
  column: Column<T>
  columns: Column<T>[]
  columnIndex: number
  depth: number
  style: CSSProperties
  rowData: any
  rowIndex: number
  isScrolling: boolean
  expandIconProps?:
    | {
        rowData: any
        rowIndex: number
        onExpand: (expand: boolean) => void
      }
    | undefined
}

type HeaderSlotProps = {
  cells: VNode[]
  columns: Column<any>[]
  headerIndex: number
}

type HeaderCellSlotProps = {
  class: string
  columns: Column<any>[]
  column: Column<any>
  columnIndex: number
  headerIndex: number
  style: CSSProperties
  headerCellProps?: any
  sortBy: SortBy
  sortState?: SortState | undefined
  onColumnSorted: (e: MouseEvent) => void
}

type RowCommonParams = {
  rowData: any
  rowIndex: number
}

type RowEventHandlerParams = {
  rowKey: KeyType
  event: Event
} & RowCommonParams

type RowEventHandler = (params: RowEventHandlerParams) => void
type RowEventHandlers = {
  onClick?: RowEventHandler
  onContextmenu?: RowEventHandler
  onDblclick?: RowEventHandler
  onMouseenter?: RowEventHandler
  onMouseleave?: RowEventHandler
}

type RowsRenderedParams = {
  rowCacheStart: number
  rowCacheEnd: number
  rowVisibleStart: number
  rowVisibleEnd: number
}

type RowSlotProps = {
  columns: Column<any>[]
  rowData: any
  columnIndex: number
  rowIndex: number
  data: any
  key: number | string
  isScrolling?: boolean
  style: CSSProperties
}

type RowExpandParams = {
  expanded: boolean
  rowKey: KeyType
} & RowCommonParams

type Data = {
  [key: KeyType]: any
  children?: Array<any>
}

type FixedData = Data

type KeyType = string | number | symbol

type ColumnSortParam<T> = { column: Column<T>; key: KeyType; order: SortOrder }

enum SortOrder {
  ASC = 'asc',
  DESC = 'desc',
}

enum Alignment {
  LEFT = 'left',
  CENTER = 'center',
  RIGHT = 'right',
}

type SortBy = { key: KeyType; Order: SortOrder }
type SortState = Record<KeyType, SortOrder>
```

</details>

## FAQs

#### How do I render a list with a checkbox in the first column?

Since you are allowed to define your own cell renderer, you can do what the example
[Customize Cell Renderer](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table-v2.md#customize-cell-renderer) did to render `checkbox` yourself, and maintain the
state by yourself.

#### Why does virtualized table provide less features than [TableV1](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/table.md)

For virtualized table, we intend to provide less feature and let our users implement their own features as needed.
Integrating too many features makes the code hard to maintain and for most users the basic features are enough. Some key
features were not developed yet. We would love to hear from you. Join [Discord](https://discord.com/invite/gXK9XNzW3X) to stay tuned.
