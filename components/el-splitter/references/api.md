# splitter API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/splitter.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Splitter API

### Splitter Attributes

| Name           | Description                      | Type                                | Default    |
| -------------- | -------------------------------- | ----------------------------------- | ---------- |
| layout         | Layout direction of the splitter | **enum**`'horizontal' \| 'vertical'` | horizontal |
| lazy (since 2.11.0) | Whether to enable lazy mode      | **boolean**                          | false      |

### Splitter Events

| Name               | Description                                                              | type                                                                          |
| ------------------ | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| resize-start       | Triggered when starting to resize a panel, `index` is the drag bar index | **Function**`(index: number, sizes: number[]) => void`                         |
| resize             | Triggered while resizing a panel, `index` is the drag bar index          | **Function**`(index: number, sizes: number[]) => void`                         |
| resize-end         | Triggered when panel resizing ends, `index` is the drag bar index        | **Function**`(index: number, sizes: number[]) => void`                         |
| collapse (since 2.10.3) | Triggered when a panel is collapsed, `index` is the drag bar index       | **Function**`(index: number, type: 'start' \| 'end', sizes: number[]) => void` |

## SplitterPanel API

### SplitterPanel Attributes

| Name                | Description                                         | Type                  | Default |
| ------------------- | --------------------------------------------------- | --------------------- | ------- |
| size / v-model:size | Size of the panel (in pixels or percentage)         | **string** / **number** | -       |
| min                 | Minimum size of the panel (in pixels or percentage) | **string** / **number** | -       |
| max                 | Maximum size of the panel (in pixels or percentage) | **string** / **number** | -       |
| resizable           | Whether the panel can be resized                    | **boolean**            | true    |
| collapsible         | Whether the panel can be collapsed                  | **boolean**            | false   |

### SplitterPanel Events

| Name        | Description                       | type                                |
| ----------- | --------------------------------- | ----------------------------------- |
| update:size | Triggered when panel size changes | **Function**`(size: number) => void` |

### SplitterPanel Slots

| Name              | Description                                     |
| ----------------- | ----------------------------------------------- |
| default           | Default content of the panel                    |
| start-collapsible | Custom content for the start collapsible button |
| end-collapsible   | Custom content for the end collapsible button   |

### SplitterPanel Exposes

| Name                       | Description                | Type                           |
| -------------------------- | -------------------------- | ------------------------------ |
| splitterPanelRef (since 2.11.9) | SplitterPanel html element | **object**`Ref<HTMLDivElement>` |
