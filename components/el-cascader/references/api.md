# cascader API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/cascader.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Cascader API

### Cascader Attributes

| Name                                       | Description                                                                                                                                                                      | Type                                                                                                                                                                        | Default      |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| model-value / v-model                      | binding value                                                                                                                                                                    | **string** / **number** /**array**`string[] \| number[] \| any`                                                                                                                | —            |
| options                                    | data of the options, the key of `value` and `label` can be customize by `CascaderProps`.                                                                                         | **array**`CascaderOption[]`                                                                                                                                                  | —            |
| [props](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/cascader.md#cascaderprops)                    | configuration options, see the following `CascaderProps` table.                                                                                                                  | **object**`CascaderProps`                                                                                                                                                    | —            |
| size                                       | size of input                                                                                                                                                                    | **enum**`'large' \| 'default' \| 'small'`                                                                                                                                    | —            |
| placeholder                                | placeholder of input                                                                                                                                                             | **string**                                                                                                                                                                   | —            |
| disabled                                   | whether Cascader is disabled                                                                                                                                                     | **boolean**                                                                                                                                                                  | —            |
| clearable                                  | whether selected value can be cleared                                                                                                                                            | **boolean**                                                                                                                                                                  | —            |
| clear-icon (since 2.11.0)                       | custom clear icon component                                                                                                                                                      | **string** / **object**`Component`                                                                                                                                            | CircleClose  |
| show-all-levels                            | whether to display all levels of the selected value in the input                                                                                                                 | **boolean**                                                                                                                                                                  | true         |
| collapse-tags                              | whether to collapse tags in multiple selection mode                                                                                                                              | **boolean**                                                                                                                                                                  | —            |
| collapse-tags-tooltip                      | whether show all selected tags when mouse hover text of collapse-tags. To use this, `collapse-tags` must be true                                                                 | **boolean**                                                                                                                                                                  | false        |
| max-collapse-tags-tooltip-height (since 2.10.2) | max height of collapse-tags tooltip.                                                                                                                                             | **string** / **number**                                                                                                                                                       | —            |
| separator                                  | option label separator                                                                                                                                                           | **string**                                                                                                                                                                   | ' / '        |
| filterable                                 | whether the options can be searched                                                                                                                                              | **boolean**                                                                                                                                                                  | —            |
| filter-method                              | customize search logic, the first parameter is `node`, the second is `keyword`, and need return a boolean value indicating whether it hits.                                      | **Function**`(node: CascaderNode, keyword: string) => boolean`                                                                                                               | —            |
| debounce                                   | debounce delay when typing filter keyword, in milliseconds                                                                                                                       | **number**                                                                                                                                                                   | 300          |
| before-filter                              | hook function before filtering with the value to be filtered as its parameter. If `false` is returned or a `Promise` is returned and then is rejected, filtering will be aborted | **Function**`(value: string) => boolean`                                                                                                                                     | —            |
| popper-class                               | custom class name for Cascader's dropdown and tags' tooltip                                                                                                                      | **string**                                                                                                                                                                   | ''           |
| popper-style                               | custom style for Cascader's dropdown and tags' tooltip                                                                                                                           | **string** / **object**                                                                                                                                                       | —            |
| teleported                                 | whether cascader popup is teleported                                                                                                                                             | **boolean**                                                                                                                                                                  | true         |
| effect (since 2.10.5)                           | tooltip theme, built-in theme: `dark` / `light`                                                                                                                                  | **enum**`'dark' \| 'light'` / **string**                                                                                                                                      | light        |
| tag-type                                   | tag type                                                                                                                                                                         | **enum**`'success' \| 'info' \| 'warning' \| 'danger'`                                                                                                                       | info         |
| tag-effect (since 2.7.8)                        | tag effect                                                                                                                                                                       | **enum**`'light' \| 'dark' \| 'plain'`                                                                                                                                       | light        |
| validate-event                             | whether to trigger form validation                                                                                                                                               | **boolean**                                                                                                                                                                  | true         |
| max-collapse-tags (since 2.3.10)                | The max tags number to be shown. To use this, `collapse-tags` must be true                                                                                                       | **number**                                                                                                                                                                   | 1            |
| empty-values (since 2.7.0)                      | empty values of component, [see config-provider](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/config-provider.md#empty-values-configurations)                                                                               | **array**                                                                                                                                                                    | —            |
| value-on-clear (since 2.7.0)                    | clear return value, [see config-provider](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/config-provider.md#empty-values-configurations)                                                                                      | **string** / **number** / **boolean** / **Function**                                                                                                                            | —            |
| persistent (since 2.7.8)                        | when dropdown is inactive and `persistent` is `false`, dropdown will be destroyed                                                                                                | **boolean**                                                                                                                                                                  | true         |
| fallback-placements (since 2.8.1)               | list of possible positions for Tooltip [popper.js](https://popper.js.org/docs/v2/modifiers/flip/#fallbackplacements)                                                             | **array**`Placement[]`                                                                                                                                                       | —            |
| placement (since 2.8.1)                         | position of dropdown                                                                                                                                                             | **enum**`'top' \| 'top-start' \| 'top-end' \| 'bottom' \| 'bottom-start' \| 'bottom-end' \| 'left' \| 'left-start' \| 'left-end' \| 'right' \| 'right-start' \| 'right-end'` | bottom-start |
| show-checked-strategy (since 2.10.5)            | strategy for displaying checked nodes in multiple selection mode. Use `parent` when you want things tidy. Use `child` when every single item matters                             | **enum**`'parent' \| 'child'`                                                                                                                                                | child        |
| virtual-scroll (since 2.14.0)                   | whether to enable virtual scrolling for large data                                                                                                                               | **boolean**                                                                                                                                                                  | false        |
| fit-input-width (since 2.14.0)                  | whether the width of the suggestion panel is the same as the input, if the value is `number`, then the width is fixed                                                            | **boolean** / **number**                                                                                                                                                      | false        |
| item-size (since 2.14.0)                        | node height for virtual scrolling (px)                                                                                                                                           | **number**                                                                                                                                                                   | 34           |
| height (since 2.14.0)                           | menu height for virtual scrolling (px)                                                                                                                                           | **number**                                                                                                                                                                   | 204          |

### Cascader Events

| Name           | Description                                                   | Type                                                        |
| -------------- | ------------------------------------------------------------- | ----------------------------------------------------------- |
| change         | triggers when the binding value changes                       | **Function**`(value: CascaderValue) => void`                 |
| expand-change  | triggers when expand option changes                           | **Function**`(value: CascaderValue) => void`                 |
| blur           | triggers when Cascader blurs                                  | **Function**`(event: FocusEvent) => void`                    |
| focus          | triggers when Cascader focuses                                | **Function**`(event: FocusEvent) => void`                    |
| clear (since 2.7.7) | triggers when the clear icon is clicked in a clearable Select | **Function**`() => void`                                     |
| visible-change | triggers when the dropdown appears/disappears                 | **Function**`(value: boolean) => void`                       |
| remove-tag     | triggers when remove tag in multiple selection mode           | **Function**`(value: CascaderNode['valueByOption']) => void` |

### Cascader Slots

| Name                     | Description                                                                                    | Type                                                      |
| ------------------------ | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| default                  | the custom content of cascader node, which are current Node object and node data respectively. | **object**`{ node: any, data: any }`                       |
| empty                    | content when there is no matched options.                                                      | —                                                         |
| prefix (since 2.9.4)          | content as Input prefix                                                                        | —                                                         |
| suggestion-item (since 2.9.5) | custom content for suggestion item when searching                                              | **object**`{ item: CascaderNode }`                         |
| tag (since 2.10.3)            | custom tags style                                                                              | **object**`{ data: Tag[], deleteTag: (tag: Tag) => void }` |
| header (since 2.10.5)         | content at the top of the dropdown                                                             | —                                                         |
| footer (since 2.10.5)         | content at the bottom of the dropdown                                                          | —                                                         |

### Cascader Exposes

| Name                          | Description                                                                                                       | Type                                                            |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| getCheckedNodes               | get an array of currently selected node,(leafOnly) whether only return the leaf checked nodes, default is `false` | **Function**`(leafOnly: boolean) => CascaderNode[] \| undefined` |
| cascaderPanelRef              | cascader panel ref                                                                                                | **object**`ComputedRef<any>`                                     |
| togglePopperVisible (since 2.2.31) | toggle the visible type of popper                                                                                 | **Function**`(visible?: boolean) => void`                        |
| contentRef                    | cascader content ref                                                                                              | **object**`ComputedRef<any>`                                     |
| presentText (since 2.8.4)          | selected content text                                                                                             | **object**`ComputedRef<string>`                                  |
| focus (since 2.11.8)               | focus the input element                                                                                           | **Function**`() => void`                                         |
| blur (since 2.11.8)                | blur the input element                                                                                            | **Function**`() => void`                                         |

## CascaderPanel API

### CascaderPanel Attributes

| Name                     | Description                                                                              | Type                                                      | Default |
| ------------------------ | ---------------------------------------------------------------------------------------- | --------------------------------------------------------- | ------- |
| model-value / v-model    | binding value                                                                            | **string**/**number**/**array**`string[] \| number[] \| any` | —       |
| options                  | data of the options, the key of `value` and `label` can be customize by `CascaderProps`. | **array**`CascaderOption[]`                                | —       |
| [props](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/cascader.md#cascaderprops)  | configuration options, see the following `CascaderProps` table.                          | **object**`CascaderProps`                                  | —       |
| virtual-scroll (since 2.14.0) | whether to enable virtual scrolling for large data                                       | **boolean**                                                | false   |
| item-size (since 2.14.0)      | node height for virtual scrolling (px)                                                   | **number**                                                 | 34      |
| height (since 2.14.0)         | menu height for virtual scrolling (px)                                                   | **number**                                                 | 204     |

### CascaderPanel Events

| Name              | Description                                                             | Type                                                     |
| ----------------- | ----------------------------------------------------------------------- | -------------------------------------------------------- |
| change            | triggers when the binding value changes                                 | **Function**`(value: CascaderValue \| undefined) => void` |
| update:modelValue | triggers when the binding value changes                                 | **Function**`(value: CascaderValue \| undefined) => void` |
| expand-change     | triggers when expand option changes                                     | **Function**`(value: CascaderNodePathValue) => void`      |
| close             | close panel event, provided to Cascader to put away the panel judgment. | **Function**`() => void`                                  |

### CascaderPanel Slots

| Name           | Description                                                                                    | Type                                |
| -------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------- |
| default        | the custom content of cascader node, which are current Node object and node data respectively. | **object**`{ node: any, data: any }` |
| empty (since 2.8.3) | the content of the panel when there is no data.                                                | —                                   |

### CascaderPanel Exposes

| Name              | Description                                                                                                       | Type                                                            |
| ----------------- | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| getCheckedNodes   | get an array of currently selected node,(leafOnly) whether only return the leaf checked nodes, default is `false` | **Function**`(leafOnly: boolean) => CascaderNode[] \| undefined` |
| clearCheckedNodes | clear checked nodes                                                                                               | **Function**`() => void`                                         |

## CascaderProps

| Attribute                  | Description                                                                                                                     | Type                                                                    | Default  |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | -------- |
| expandTrigger              | trigger mode of expanding options                                                                                               | **enum**`'click' \| 'hover'`                                             | click    |
| multiple                   | whether multiple selection is enabled                                                                                           | **boolean**                                                              | false    |
| checkStrictly              | whether checked state of a node not affects its parent and child nodes                                                          | **boolean**                                                              | false    |
| emitPath                   | when checked nodes change, whether to emit an array of node's path, if false, only emit the value of node.                      | **boolean**                                                              | true     |
| lazy                       | whether to dynamic load child nodes, use with `lazyload` attribute                                                              | **boolean**                                                              | false    |
| lazyLoad                   | method for loading child nodes data, only works when `lazy` is true. The reject parameter is supported after version (since 2.11.5). | **Function**`(node: Node, resolve: Resolve, reject: () => void) => void` | —        |
| value                      | specify which key of node object is used as the node's value                                                                    | **string**                                                               | value    |
| label                      | specify which key of node object is used as the node's label                                                                    | **string**                                                               | label    |
| children                   | specify which key of node object is used as the node's children                                                                 | **string**                                                               | children |
| disabled                   | specify which key of node object is used as the node's disabled                                                                 | **string**                                                               | disabled |
| leaf                       | specify which key of node object is used as the node's leaf field                                                               | **string**                                                               | leaf     |
| hoverThreshold             | hover threshold of expanding options                                                                                            | **number**                                                               | 500      |
| checkOnClickNode (since 2.10.5) | whether to check or uncheck node when clicking on the node                                                                      | **boolean**                                                              | false    |
| checkOnClickLeaf (since 2.10.5) | whether to check or uncheck node when clicking on leaf node (last children).                                                    | **boolean**                                                              | true     |
| showPrefix (since 2.10.5)       | whether to show the radio or checkbox prefix                                                                                    | **boolean**                                                              | true     |

## Type Declarations

<details>
  <summary>Show declarations</summary>

```ts
type CascaderNodeValue = string | number
type CascaderNodePathValue = CascaderNodeValue[]
type CascaderValue =
  | CascaderNodeValue
  | CascaderNodePathValue
  | (CascaderNodeValue | CascaderNodePathValue)[]

type Resolve = (data: any) => void

type ExpandTrigger = 'click' | 'hover'

type LazyLoad = (node: Node, resolve: Resolve, reject: () => void) => void

type isDisabled = (data: CascaderOption, node: Node) => boolean

type isLeaf = (data: CascaderOption, node: Node) => boolean

interface CascaderOption extends Record<string, unknown> {
  label?: string
  value?: CascaderNodeValue
  children?: CascaderOption[]
  disabled?: boolean
  leaf?: boolean
}

interface CascaderProps {
  expandTrigger?: ExpandTrigger
  multiple?: boolean
  checkStrictly?: boolean
  emitPath?: boolean
  lazy?: boolean
  lazyLoad?: LazyLoad
  value?: string
  label?: string
  children?: string
  disabled?: string | isDisabled
  leaf?: string | isLeaf
  hoverThreshold?: number
}

class Node {
  readonly uid: number
  readonly level: number
  readonly value: CascaderNodeValue
  readonly label: string
  readonly pathNodes: Node[]
  readonly pathValues: CascaderNodePathValue
  readonly pathLabels: string[]

  childrenData: ChildrenData
  children: Node[]
  text: string
  loaded: boolean
  /**
   * Is it checked
   *
   * @default false
   */
  checked: boolean
  /**
   * Used to indicate the intermediate state of unchecked and fully checked child nodes
   *
   * @default false
   */
  indeterminate: boolean
  /**
   * Loading Status
   *
   * @default false
   */
  loading: boolean

  // getter
  isDisabled: boolean
  isLeaf: boolean
  valueByOption: CascaderNodeValue | CascaderNodePathValue

  // method
  appendChild(childData: CascaderOption): Node
  calcText(allLevels: boolean, separator: string): string
  broadcast(): void
  emit(): void
  onParentCheck(checked: boolean): void
  onChildCheck(): void
  setCheckState(checked: boolean): void
  doCheck(checked: boolean): void
}

Node as CascaderNode
```

</details>
