# button API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/button.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Button API

### Button Attributes

| Name              | Description                                                                                                                                          | Type                                                                                                         | Default |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------- |
| size              | button size                                                                                                                                          | **enum**`'large' \| 'default' \| 'small'`                                                                     | —       |
| type              | button type, when setting `color`, the latter prevails                                                                                               | **enum**`'default' \| 'primary' \| 'success' \| 'warning' \| 'danger' \| 'info' \| '' \| 'text' (deprecated)` | —       |
| plain             | determine whether it's a plain button                                                                                                                | **boolean**                                                                                                   | false   |
| text (since 2.2.0)     | determine whether it's a text button                                                                                                                 | **boolean**                                                                                                   | false   |
| bg (since 2.2.0)       | determine whether the text button background color is always on                                                                                      | **boolean**                                                                                                   | false   |
| link (since 2.2.1)     | determine whether it's a link button                                                                                                                 | **boolean**                                                                                                   | false   |
| round             | determine whether it's a round button                                                                                                                | **boolean**                                                                                                   | false   |
| circle            | determine whether it's a circle button                                                                                                               | **boolean**                                                                                                   | false   |
| dashed (since 2.13.3)  | determine whether it's a dashed button                                                                                                               | **boolean**                                                                                                   | false   |
| loading           | determine whether it's loading                                                                                                                       | **boolean**                                                                                                   | false   |
| loading-icon      | customize loading icon component                                                                                                                     | **string** / **Component**                                                                                     | Loading |
| disabled          | disable the button                                                                                                                                   | **boolean**                                                                                                   | false   |
| icon              | icon component                                                                                                                                       | **string** / **Component**                                                                                     | —       |
| autofocus         | same as native button's `autofocus`                                                                                                                  | **boolean**                                                                                                   | false   |
| native-type       | same as native button's `type`                                                                                                                       | **enum**`'button' \| 'submit' \| 'reset'`                                                                     | button  |
| auto-insert-space | automatically insert a space between two chinese characters(this will only take effect when the text length is 2 and all characters are in Chinese.) | **boolean**                                                                                                   | false   |
| color             | custom button color, automatically calculate `hover` and `active` color. Works with `link`/`text` buttons since (since 2.13.7)                            | **string**                                                                                                    | —       |
| dark              | dark mode, which automatically converts `color` to dark mode colors                                                                                  | **boolean**                                                                                                   | false   |
| tag (since 2.3.4)      | custom element tag                                                                                                                                   | **string** / **Component**                                                                                     | button  |

### Button Slots

| Name    | Description                 |
| ------- | --------------------------- |
| default | customize default content   |
| loading | customize loading component |
| icon    | customize icon component    |

### Button Exposes

| Name           | Description          | Type                                                                                                           |
| -------------- | -------------------- | -------------------------------------------------------------------------------------------------------------- |
| ref            | button html element  | **object**`Ref<HTMLButtonElement>`                                                                              |
| size           | button size          | **object**`ComputedRef<'' \| 'small' \| 'default' \| 'large'>`                                                  |
| type           | button type          | **object**`ComputedRef<'' \| 'default' \| 'primary' \| 'success' \| 'warning' \| 'info' \| 'danger' \| 'text'>` |
| disabled       | button disabled      | **object**`ComputedRef<boolean>`                                                                                |
| shouldAddSpace | whether adding space | **object**`ComputedRef<boolean>`                                                                                |

## ButtonGroup API

### ButtonGroup Attributes

| Name                | Description                                      | Type                                                               | Default    |
| ------------------- | ------------------------------------------------ | ------------------------------------------------------------------ | ---------- |
| size                | control the size of buttons in this button-group | **enum**`'large' \| 'default' \| 'small'`                           | —          |
| type                | control the type of buttons in this button-group | **enum**`'primary' \| 'success' \| 'warning' \| 'danger' \| 'info'` | —          |
| direction (since 2.11.9) | display direction                                | **enum**`'horizontal' \| 'vertical'`                                | horizontal |

### ButtonGroup Slots

| Name    | Description                    | Subtags |
| ------- | ------------------------------ | ------- |
| default | customize button group content | Button  |
