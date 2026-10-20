# dropdown API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/dropdown.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Dropdown API

### Dropdown Attributes

| Name                         | Description                                                                                                           | Type                                                                                                         | Default                                                                    |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| type                         | menu button type, refer to `Button` Component, only works when `split-button` is true                                 | **enum**`'' \| 'default' \| 'primary' \| 'success' \| 'warning' \| 'info' \| 'danger' \| 'text' (deprecated)` | ''                                                                         |
| size                         | menu size, also works on the split button                                                                             | **enum**`'' \| 'large' \| 'default' \| 'small'`                                                               | ''                                                                         |
| button-props                 | props for the button component, refer to [Button Attributes](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/button.md#button-attributes)                         | **object**                                                                                                    | —                                                                          |
| max-height                   | the max height of menu                                                                                                | **string** / **number**                                                                                        | ''                                                                         |
| split-button                 | whether a button group is displayed                                                                                   | **boolean**                                                                                                   | false                                                                      |
| disabled                     | whether to disable                                                                                                    | **boolean**                                                                                                   | false                                                                      |
| placement                    | placement of pop menu                                                                                                 | **enum**`'top' \| 'top-start' \| 'top-end' \| 'bottom' \| 'bottom-start' \| 'bottom-end'`                     | bottom                                                                     |
| effect                       | Tooltip theme, built-in theme: `dark` / `light`                                                                       | **enum**`'dark' \| 'light'` / **string**                                                                       | light                                                                      |
| trigger                      | how to trigger                                                                                                        | **enum**`'click' \| 'hover' \| 'contextmenu'` / **array**`Array<'click' \| 'hover' \| 'contextmenu'>`          | hover                                                                      |
| trigger-keys (since 2.9.1)        | specify which keys on the keyboard can trigger when pressed                                                           | **array**`string[]`                                                                                           | `['Enter', 'Space', 'ArrowDown', 'NumpadEnter']`                           |
| virtual-triggering (since 2.11.3) | indicates whether virtual triggering is enabled                                                                       | **boolean**                                                                                                   | —                                                                          |
| virtual-ref (since 2.11.3)        | indicates the reference element to which the dropdown is attached                                                     | **HTMLElement**                                                                                               | —                                                                          |
| hide-on-click                | whether to hide menu after clicking menu-item                                                                         | **boolean**                                                                                                   | true                                                                       |
| show-arrow (since 2.11.3)         | whether the tooltip content has an arrow                                                                              | **boolean**                                                                                                   | true                                                                       |
| show-timeout                 | delay time before show a dropdown (only works when trigger is `hover`)                                                | **number**                                                                                                    | 150                                                                        |
| hide-timeout                 | delay time before hide a dropdown (only works when trigger is `hover`)                                                | **number**                                                                                                    | 150                                                                        |
| role                         | the ARIA role attribute for the dropdown menu. Depending on the use case, you may want to change this to 'navigation' | **enum**`'dialog' \| 'grid' \| 'group' \| 'listbox' \| 'menu' \| 'navigation' \| 'tooltip' \| 'tree'`         | menu                                                                       |
| tabindex                     | [tabindex](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex) of Dropdown                  | **number** / **string**                                                                                        | 0                                                                          |
| popper-class                 | custom class name for Dropdown's dropdown                                                                             | **string** / **object**                                                                                        | ''                                                                         |
| popper-style (since 2.11.5)       | custom style for Dropdown's dropdown                                                                                  | **string** / **object**                                                                                        | —                                                                          |
| popper-options               | [popper.js](https://popper.js.org/docs/v2/) parameters                                                                | **object**                                                                                                    | `{modifiers: [{name: 'computeStyles',options: {gpuAcceleration: false}}]}` |
| teleported (since 2.2.20)         | whether the dropdown popup is teleported to the body                                                                  | **boolean**                                                                                                   | true                                                                       |
| append-to (since 2.13.0)          | which element the dropdown CONTENT appends to                                                                         | **CSSSelector** / **HTMLElement**                                                                              | —                                                                          |
| persistent (since 2.9.5)          | when dropdown inactive and `persistent` is `false` , dropdown menu will be destroyed                                  | **boolean**                                                                                                   | true                                                                       |

### Dropdown Slots

| Name     | Description                                                                                                                                   | Subtags       |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| default  | content of Dropdown. Notice: Must be a valid html dom element (ex. `<span>, <button> etc.`) or `el-component`, to attach the trigger listener | —             |
| dropdown | content of the Dropdown Menu, usually a `<el-dropdown-menu>` element                                                                          | Dropdown-Menu |

### Dropdown Events

| Name           | Description                                                                                               | Type                                  |
| -------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| click          | if `split-button` is `true`, triggers when left button is clicked                                         | **Function**`(e: MouseEvent) => void`  |
| command        | triggers when a dropdown item is clicked, the parameters is the command dispatched from the dropdown item | **Function**`(...args: any[]) => void` |
| visible-change | triggers when the dropdown appears/disappears, the param is true when it appears, and false otherwise     | **Function**`(val: boolean) => void`   |

### Dropdown Exposes

| Method      | Description             | Type                    |
| ----------- | ----------------------- | ----------------------- |
| handleOpen  | open the dropdown menu  | **Function**`() => void` |
| handleClose | close the dropdown menu | **Function**`() => void` |

## Dropdown-Menu API

### Dropdown-Menu Slots

| Name    | Description              | Subtags       |
| ------- | ------------------------ | ------------- |
| default | content of Dropdown Menu | Dropdown-Item |

## Dropdown-Item API

### Dropdown-Item Attributes

| Name     | Description                                                 | Type                              | Default |
| -------- | ----------------------------------------------------------- | --------------------------------- | ------- |
| command  | a command to be dispatched to Dropdown's `command` callback | **string** / **number** / **object** | —       |
| disabled | whether the item is disabled                                | **boolean**                        | false   |
| divided  | whether a divider is displayed                              | **boolean**                        | false   |
| icon     | custom icon                                                 | **string** / **Component**          | —       |

### Dropdown-Item Slots

| Name           | Description                                 |
| -------------- | ------------------------------------------- |
| default        | customize of Dropdown Item                  |
| icon (since 2.13.1) | custom icon, it will override the icon prop |
