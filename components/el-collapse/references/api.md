# collapse API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/collapse.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Collapse API

### Collapse Attributes

| Name                           | Description                                                                                                                                          | Type                                           | Default |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ------- |
| model-value / v-model          | currently active panel, the type is `string` in accordion mode, otherwise it is `array`                                                              | **string** / **array**                           | []      |
| accordion                      | whether to activate accordion mode                                                                                                                   | **boolean**                                     | false   |
| expand-icon-position (since 2.9.10) | set expand icon position                                                                                                                             | **enum**`'left' \| 'right' `                    | right   |
| before-collapse (since 2.9.11)      | before-collapse hook before the collapse state changes. If `false` is returned or a `Promise` is returned and then is rejected, will stop collapsing | **Function**`() => Promise<boolean> \| boolean` | —       |

### Collapse Events

| Name   | Description                                                                                                   | Type                                                |
| ------ | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| change | triggers when active panels change, the parameter type is `string` in accordion mode, otherwise it is `array` | **Function**`(activeNames: array \| string) => void` |

### Collapse Slots

| Name    | Description               | Subtags       |
| ------- | ------------------------- | ------------- |
| default | customize default content | Collapse Item |

### Collapse Exposes

| Name           | Description                  | Type                                                     |
| -------------- | ---------------------------- | -------------------------------------------------------- |
| activeNames    | currently active panel names | **object**`ComputedRef<(string \| number)[]>`             |
| setActiveNames | set active panel names       | **Function**`(activeNames: (string \| number)[]) => void` |

## Collapse Item API

### Collapse Item Attributes

| Name          | Description                        | Type                     | Default    |
| ------------- | ---------------------------------- | ------------------------ | ---------- |
| name          | unique identification of the panel | **string** / **number**    | —          |
| title         | title of the panel                 | **string**                | ''         |
| icon (since 2.8.3) | icon of the collapse item          | **string** / **Component** | ArrowRight |
| disabled      | disable the collapse item          | **boolean**               | false      |

### Collapse Item Slot

| Name          | Description                    | Type                             |
| ------------- | ------------------------------ | -------------------------------- |
| default       | content of Collapse Item       | —                                |
| title         | content of Collapse Item title | **object**`{ isActive: boolean }` |
| icon (since 2.8.3) | content of Collapse Item icon  | **object**`{ isActive: boolean }` |

### Collapse Item Exposes

| Name     | Description                                 | Type                                         |
| -------- | ------------------------------------------- | -------------------------------------------- |
| isActive | whether the current collapse item is active | **object**`ComputedRef<boolean \| undefined>` |
