# tree-v2 API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/tree-v2.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## TreeV2 API

### TreeV2 Attributes

| Name                          | Description                                                                                                                                  | Type                                                                        | Default |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------- |
| data                          | tree data                                                                                                                                    | **array**`Array<{[key: string]: any}>`                                       | —       |
| empty-text                    | text displayed when data is void                                                                                                             | **string**                                                                   | —       |
| [props](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/tree-v2.md#props)               | configuration options, see the following table                                                                                               | **object**                                                                   | —       |
| highlight-current             | whether current node is highlighted                                                                                                          | **boolean**                                                                  | false   |
| expand-on-click-node          | whether to expand or collapse node when clicking on the node, if false, then expand or collapse node only when clicking on the arrow icon.   | **boolean**                                                                  | true    |
| check-on-click-node           | whether to check or uncheck node when clicking on the node, if false, the node can only be checked or unchecked by clicking on the checkbox. | **boolean**                                                                  | false   |
| check-on-click-leaf (since 2.9.6)  | whether to check or uncheck node when clicking on leaf node (last children).                                                                 | **boolean**                                                                  | true    |
| default-expanded-keys         | array of keys of initially expanded nodes                                                                                                    | **array**`Array<string \| number>`                                           | —       |
| show-checkbox                 | whether node is selectable                                                                                                                   | **boolean**                                                                  | false   |
| check-strictly                | whether checked state of a node not affects its father and child nodes when `show-checkbox` is `true`                                        | **boolean**                                                                  | false   |
| default-checked-keys          | array of keys of initially checked nodes                                                                                                     | **array**`Array<string \| number>`                                           | —       |
| current-node-key              | key of initially selected node                                                                                                               | **string** / **number**                                                       | —       |
| filter-method                 | this function will be executed on each node when use filter method. if return `false`, tree node will be hidden.                             | **Function**`(query: string, data: TreeNodeData, node: TreeNode) => boolean` | —       |
| indent                        | horizontal indentation of nodes in adjacent levels in pixels                                                                                 | **number**                                                                   | 16      |
| icon                          | custom tree node icon component                                                                                                              | **string** / **Component**                                                    | —       |
| item-size (since 2.2.33)           | custom tree node height                                                                                                                      | **number**                                                                   | 26      |
| scrollbar-always-on (since 2.10.4) | always show scrollbar                                                                                                                        | **boolean**                                                                  | false   |
| height                        | height of the tree                                                                                                                           | **number**                                                                   | 200     |

### props

| Attribute      | Description                                                                          | Type                                                                                                | Default  |
| -------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- | -------- |
| value          | unique identity key name for nodes, its value should be unique across the whole tree | **string**                                                                                           | id       |
| label          | specify which key of node object is used as the node's label                         | **string**                                                                                           | label    |
| children       | specify which node object is used as the node's subtree                              | **string**                                                                                           | children |
| disabled       | specify which key of node object represents if node's checkbox is disabled           | **string**                                                                                           | disabled |
| class (since 2.9.0) | custom node class name                                                               | **string** / **Function**`(data: TreeNodeData, node: TreeNode) => string \| {[key: string]: boolean}` | —        |

### TreeV2 Exposes

`Tree` has the following method, which returns the currently selected array of nodes.

| Method                | Description                                                                                                                       | Parameters                                                           |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| filter                | filter all tree nodes, filtered nodes will be hidden                                                                              | `(query: string)`                                                    |
| getCheckedNodes       | If the node can be selected (`show-checkbox` is `true`), it returns the currently selected array of nodes                         | `(leafOnly: boolean)`                                                |
| getCheckedKeys        | If the node can be selected (`show-checkbox` is `true`), it returns the currently selected array of node's keys                   | `(leafOnly: boolean)`                                                |
| setCheckedKeys        | set certain nodes to be checked                                                                                                   | `(keys: TreeKey[])`                                                  |
| setChecked            | set node to be checked or not, `deep` (added in (since 2.14.0)) indicates whether child nodes should be recursively checked/unchecked. | `(key: TreeKey, checked: boolean, deep?: boolean)`                   |
| setExpandedKeys       | set certain nodes to be expanded                                                                                                  | `(keys: TreeKey[])`                                                  |
| getHalfCheckedNodes   | If the node can be selected (`show-checkbox` is `true`), it returns the currently half selected array of nodes                    | —                                                                    |
| getHalfCheckedKeys    | If the node can be selected (`show-checkbox` is `true`), it returns the currently half selected array of node's keys              | —                                                                    |
| getCurrentKey         | return the highlight node's key (undefined if no node is highlighted)                                                             | —                                                                    |
| getCurrentNode        | return the highlight node's data (undefined if no node is highlighted)                                                            | —                                                                    |
| setCurrentKey         | set highlighted node by key                                                                                                       | `(key: TreeKey)`                                                     |
| getNode               | get node by key or data                                                                                                           | `(data: TreeKey \| TreeNodeData)`                                    |
| expandNode            | expand specified node                                                                                                             | `(node: TreeNode)`                                                   |
| collapseNode          | collapse specified node                                                                                                           | `(node: TreeNode)`                                                   |
| setData               | When the data is very large, using reactive data will cause the poor performance, so we provide a way to avoid this situation     | `(data: TreeData)`                                                   |
| scrollTo (since 2.8.0)     | scroll to a given position                                                                                                        | `(offset: number)`                                                   |
| scrollToNode (since 2.8.0) | scroll to a given tree key with specified scroll strategy                                                                         | `(key: TreeKey, strategy?: auto \| smart \| center \| start \| end)` |

### TreeV2 Events

| Name               | Description                                          | Parameters                                                                                                                              |
| ------------------ | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| node-click         | triggers when a node is clicked                      | `(data: TreeNodeData, node: TreeNode, e: MouseEvent)`                                                                                   |
| node-drop (since 2.8.3) | triggers when drag something and drop on a node      | `(data: TreeNodeData, node: TreeNode, e: DragEvent)`                                                                                    |
| node-contextmenu   | triggers when a node is clicked by right button      | `(e: Event, data: TreeNodeData, node: TreeNode)`                                                                                        |
| check-change       | triggers when the selected state of the node changes | `(data: TreeNodeData, checked: boolean)`                                                                                                |
| check              | triggers after clicking the checkbox of a node       | `(data: TreeNodeData, info: { checkedKeys: TreeKey[],checkedNodes: TreeData, halfCheckedKeys: TreeKey[], halfCheckedNodes: TreeData,})` |
| current-change     | triggers when current node changes                   | `(data: TreeNodeData, node: TreeNode)`                                                                                                  |
| node-expand        | triggers when current node open                      | `(data: TreeNodeData, node: TreeNode)`                                                                                                  |
| node-collapse      | triggers when current node close                     | `(data: TreeNodeData, node: TreeNode)`                                                                                                  |

### TreeV2 Slots

| Name           | Description                       | Type                                              |
| -------------- | --------------------------------- | ------------------------------------------------- |
| default        | custom content for tree nodes     | **object**`{ node: TreeNode, data: TreeNodeData }` |
| empty (since 2.9.0) | custom content when data is empty | —                                                 |

## Type Declarations

<details>
  <summary>Show declarations</summary>

```ts
type TreeNodeData = Record<string, any>
type TreeKey = string | number
type TreeData = TreeNodeData[]

interface TreeNode {
  key: TreeKey
  level: number
  parent?: TreeNode
  children?: TreeNode[]
  data: TreeNodeData
  disabled?: boolean
  label?: string
  isLeaf?: boolean
  expanded?: boolean
  isEffectivelyChecked?: boolean
}
```

</details>
