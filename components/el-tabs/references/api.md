# tabs API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/tabs.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Tabs API

### Tabs Attributes

| Name                    | Description                                                                                                                             | Type                                                                                             | Default    |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ---------- |
| model-value / v-model   | binding value, name of the selected tab, the default value is the name of first tab                                                     | **string** / **number**                                                                            | —          |
| default-value (since 2.11.9) | The value of the tab that should be active when initially rendered. (avoid initial transition)                                          | **string** / **number**                                                                            | —          |
| type                    | type of Tab                                                                                                                             | **enum**`'' \| 'card' \| 'border-card'`                                                           | ''         |
| closable                | whether Tab is closable                                                                                                                 | **boolean**                                                                                       | false      |
| addable                 | whether Tab is addable                                                                                                                  | **boolean**                                                                                       | false      |
| editable                | whether Tab is addable and closable                                                                                                     | **boolean**                                                                                       | false      |
| tab-position            | position of tabs                                                                                                                        | **enum**`'top' \| 'right' \| 'bottom' \| 'left'`                                                  | top        |
| stretch                 | whether width of tab automatically fits its container                                                                                   | **boolean**                                                                                       | false      |
| before-leave            | hook function before switching tab. If `false` is returned or a `Promise` is returned and then is rejected, switching will be prevented | **Function**`(activeName: TabPaneName, oldActiveName: TabPaneName) => Awaitable<void \| boolean>` | () => true |
| tabindex (since 2.11.7)      | tabs tabindex                                                                                                                           | **string** / **number**                                                                            | 0          |

### Tabs Events

| Name       | Description                                           | Parameters                                                                           |
| ---------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------ |
| tab-click  | triggers when a tab is clicked                        | **Function**`(pane: TabsPaneContext, ev: Event) => void`                              |
| tab-change | triggers when `activeName` is changed                 | **Function**`(name: TabPaneName) => void`                                             |
| tab-remove | triggers when tab-remove button is clicked            | **Function**`(name: TabPaneName) => void`                                             |
| tab-add    | triggers when tab-add button is clicked               | **Function**`() => void`                                                              |
| edit       | triggers when tab-add button or tab-remove is clicked | **Function**`(paneName: TabPaneName \| undefined, action: 'remove' \| 'add') => void` |

### Tabs Slots

| Name                           | Description               | Subtags  |
| ------------------------------ | ------------------------- | -------- |
| default                        | customize default content | Tab-pane |
| add-icon (since 2.5.4)              | customize add button icon | —        |

### Tabs Exposes

| Name                | Description                | Type                                        |
| ------------------- | -------------------------- | ------------------------------------------- |
| currentName         | current active pane name   | **object**`Ref<TabPaneName>`                 |
| tabNavRef (since 2.9.10) | tab-nav component instance | **object**`Ref<TabNavInstance \| undefined>` |

## Tab-nav API

### Tab-nav Exposes

| Name                 | Description                 | Type                                        |
| -------------------- | --------------------------- | ------------------------------------------- |
| scrollToActiveTab    | scroll to the active tab    | **Function**`() => Promise<void>`            |
| removeFocus          | remove focus status         | **Function**`() => boolean`                  |
| tabListRef (since 2.9.10) | el_tabs\_\_nav html element | **object**`Ref<HTMLDivElement \| undefined>` |
| tabBarRef (since 2.9.10)  | el_tabs\_\_nav bar instance | **object**`Ref<TabBarInstance \| undefined>` |

## Tab-bar API

### Tab-bar Exposes

| Name             | Description                                                       | Type                                        |
| ---------------- | ----------------------------------------------------------------- | ------------------------------------------- |
| ref (since 2.9.10)    | tab root html element                                             | **object**`Ref<HTMLDivElement \| undefined>` |
| update (since 2.9.10) | method to manually update tab bar style, return the updated style | **Function**`() => CSSProperties`            |

## Tab-pane API

### Tab-pane Attributes

| Name     | Description                                                                                                                                                                         | Type                  | Default |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ------- |
| label    | title of the tab                                                                                                                                                                    | **string**             | ''      |
| disabled | whether Tab is disabled                                                                                                                                                             | **boolean**            | false   |
| name     | identifier corresponding to the name of Tabs, representing the alias of the tab-pane, the default is ordinal number of the tab-pane in the sequence, e.g. the first tab-pane is '0' | **string** / **number** | —       |
| closable | whether Tab is closable                                                                                                                                                             | **boolean**            | false   |
| lazy     | whether Tab is lazily rendered                                                                                                                                                      | **boolean**            | false   |

### Tab-pane Slots

| Name    | Description        |
| ------- | ------------------ |
| default | Tab-pane's content |
| label   | Tab-pane's label   |

## FAQ

#### How to use sortable/draggable tabs ?

We exposed the necessary information to implement it yourself.
You can use a native way to do it, [demo](https://tinyurl.com/2jkyw82j).
Or using [SortableJs](https://github.com/SortableJS/Sortable), [demo](https://tinyurl.com/2r8js24y).
