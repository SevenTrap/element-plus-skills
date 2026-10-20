# menu API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/menu.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Menu API

### Menu Attributes

| Name                            | Description                                                                                                                                                           | Type                                   | Default  |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | -------- |
| mode                            | menu display mode                                                                                                                                                     | **enum**`'horizontal' \| 'vertical'`    | vertical |
| collapse                        | whether the menu is collapsed (available only in vertical mode)                                                                                                       | **boolean**                             | false    |
| ellipsis                        | whether the menu is ellipsis (available only in horizontal mode)                                                                                                      | **boolean**                             | true     |
| ellipsis-icon (since 2.4.4)          | custom ellipsis icon (available only in horizontal mode and ellipsis is true)                                                                                         | **string** / **Component**               | —        |
| popper-offset (since 2.4.4)          | offset of the popper (effective for all submenus)                                                                                                                     | **number**                              | 6        |
| default-active                  | index of active menu on page load                                                                                                                                     | **string**                              | ''       |
| default-openeds                 | array that contains indexes of currently active sub-menus                                                                                                             | **array**`string[]`                     | []       |
| unique-opened                   | whether only one sub-menu can be active                                                                                                                               | **boolean**                             | false    |
| menu-trigger                    | how sub-menus are triggered, only works when `mode` is 'horizontal'                                                                                                   | **enum**`'hover' \| 'click'`            | hover    |
| router                          | whether `vue-router` mode is activated. If true, index will be used as 'path' to activate the route action. Use with `default-active` to set the active item on load. | **boolean**                             | false    |
| collapse-transition             | whether to enable the collapse transition                                                                                                                             | **boolean**                             | true     |
| popper-effect (since 2.2.26)         | Tooltip theme, built-in theme: `dark` / `light` when menu is collapsed                                                                                                | **enum**`'dark' \| 'light'` / **string** | dark     |
| close-on-click-outside (since 2.4.4) | optional, whether menu is collapsed when clicking outside                                                                                                             | **boolean**                             | false    |
| popper-class (since 2.5.0)           | custom class name for all popup menus and titles' tooltips                                                                                                            | **string**                              | —        |
| popper-style (since 2.11.5)          | custom style for all popup menus and titles' tooltips                                                                                                                 | **string** / **object**                  | —        |
| show-timeout (since 2.5.0)           | control timeout for all menus before showing                                                                                                                          | **number**                              | 300      |
| hide-timeout (since 2.5.0)           | control timeout for all menus before hiding                                                                                                                           | **number**                              | 300      |
| background-color (deprecated)  | background color of Menu (hex format) (use `--el-menu-bg-color` in a style class instead)                                                                             | **string**                              | #ffffff  |
| text-color (deprecated)        | text color of Menu (hex format) ( use `--el-menu-text-color` in a style class instead)                                                                                | **string**                              | #303133  |
| active-text-color (deprecated) | text color of currently active menu item (hex format) ( use `--el-menu-active-color` in a style class instead)                                                        | **string**                              | #409eff  |
| persistent (since 2.9.5)             | when menu inactive and `persistent` is `false` , dropdown menu will be destroyed                                                                                      | **boolean**                             | true     |

### Menu Events

| Name   | Description                               | Type                         |
| ------ | ----------------------------------------- | ---------------------------- |
| select | callback function when menu is activated  | **Function**`MenuSelectEvent` |
| open   | callback function when sub-menu expands   | **Function**`MenuOpenEvent`   |
| close  | callback function when sub-menu collapses | **Function**`MenuCloseEvent`  |

### Menu Slots

| Name    | Description               | Subtags                               |
| ------- | ------------------------- | ------------------------------------- |
| default | customize default content | SubMenu / Menu-Item / Menu-Item-Group |

### Menu Exposes

| Name                       | Description                                                            | Type                                 |
| -------------------------- | ---------------------------------------------------------------------- | ------------------------------------ |
| open                       | open a specific sub-menu, the param is index of the sub-menu to open   | **Function**`(index: string) => void` |
| close                      | close a specific sub-menu, the param is index of the sub-menu to close | **Function**`(index: string) => void` |
| handleResize               | manually trigger menu width recalculation                              | **Function**`() => void`              |
| updateActiveIndex (since 2.9.8) | set index of active menu                                               | **Function**`(index: string) => void` |

## SubMenu API

### SubMenu Attributes

| Name                   | Description                                                                                                                                   | Type                     | Default   |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | --------- |
| index (required)      | unique identification                                                                                                                         | **string**                | —         |
| popper-class           | custom class name for the popup menu                                                                                                          | **string**                | —         |
| popper-style (since 2.11.5) | custom style for the popup menu                                                                                                               | **string** / **object**    | —         |
| show-timeout           | timeout before showing a sub-menu(inherit `show-timeout` of the menu by default.)                                                             | **number**                | —         |
| hide-timeout           | timeout before hiding a sub-menu(inherit `hide-timeout` of the menu by default.)                                                              | **number**                | —         |
| disabled               | whether the sub-menu is disabled                                                                                                              | **boolean**               | false     |
| teleported             | whether popup menu is teleported to the body, the default is true for the level one SubMenu, false for other SubMenus                         | **boolean**               | undefined |
| popper-offset          | offset of the popper (overrides the `popper` of menu)                                                                                         | **number**                | —         |
| expand-close-icon      | Icon when menu are expanded and submenu are closed, `expand-close-icon` and `expand-open-icon` need to be passed together to take effect      | **string** / **Component** | —         |
| expand-open-icon       | Icon when menu are expanded and submenu are opened, `expand-open-icon` and `expand-close-icon` need to be passed together to take effect      | **string** / **Component** | —         |
| collapse-close-icon    | Icon when menu are collapsed and submenu are closed, `collapse-close-icon` and `collapse-open-icon` need to be passed together to take effect | **string** / **Component** | —         |
| collapse-open-icon     | Icon when menu are collapsed and submenu are opened, `collapse-open-icon` and `collapse-close-icon` need to be passed together to take effect | **string** / **Component** | —         |

### SubMenu Slots

| Name    | Description               | Subtags                               |
| ------- | ------------------------- | ------------------------------------- |
| default | customize default content | SubMenu / Menu-Item / Menu-Item-Group |
| title   | customize title content   | —                                     |

## Menu-Item API

### Menu-Item Attributes

| Name              | Description                          | Type                  | Default |
| ----------------- | ------------------------------------ | --------------------- | ------- |
| index (required) | unique identification                | **string**             | —       |
| route             | Vue Router Route Location Parameters | **string** / **object** | —       |
| disabled          | whether disabled                     | **boolean**            | false   |

### Menu-Item Events

| Name  | Description                                                                  | Type                                            |
| ----- | ---------------------------------------------------------------------------- | ----------------------------------------------- |
| click | callback function when menu-item is clicked, the param is menu-item instance | **Function**`(item: MenuItemRegistered) => void` |

### Menu-Item Slots

| Name    | Description               |
| ------- | ------------------------- |
| default | customize default content |
| title   | customize title content   |

## Menu-Item-Group API

### Menu-Item-Group Attributes

| Name  | Description | Type      | Default |
| ----- | ----------- | --------- | ------- |
| title | group title | **string** | —       |

### Menu-Item-Group Slots

| Name    | Description               | Subtags   |
| ------- | ------------------------- | --------- |
| default | customize default content | Menu-Item |
| title   | customize group title     | —         |

## Type Declarations

<details>
  <summary>Show declarations</summary>

```ts
/**
 * @param index index of activated menu
 * @param indexPath index path of activated menu
 * @param item the selected menu item
 * @param routerResult result returned by `vue-router` if `router` is enabled
 */
type MenuSelectEvent = (
  index: string,
  indexPath: string[],
  item: MenuItemClicked,
  routerResult?: Promise<void | NavigationFailure>
) => void

/**
 * @param index index of expanded sub-menu
 * @param indexPath index path of expanded sub-menu
 */
type MenuOpenEvent = (index: string, indexPath: string[]) => void

/**
 * @param index index of collapsed sub-menu
 * @param indexPath index path of collapsed sub-menu
 */
type MenuCloseEvent = (index: string, indexPath: string[]) => void

interface MenuItemRegistered {
  index: string
  indexPath: string[]
  active: boolean
}

interface MenuItemClicked {
  index: string
  indexPath: string[]
  route?: RouteLocationRaw
}
```

</details>
