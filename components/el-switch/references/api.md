# switch API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/switch.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                          | Description                                                                                                                                     | Type                                           | Default |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ------- |
| model-value / v-model         | binding value, it should be equivalent to either `active-value` or `inactive-value`, by default it's `boolean` type                             | **boolean** / **string** / **number**             | false   |
| disabled                      | whether Switch is disabled                                                                                                                      | **boolean**                                     | false   |
| loading                       | whether Switch is in loading state                                                                                                              | **boolean**                                     | false   |
| size                          | size of Switch                                                                                                                                  | **enum**`'' \| 'large' \| 'default' \| 'small'` | ''      |
| width                         | width of Switch                                                                                                                                 | **number** / **string**                          | ''      |
| inline-prompt                 | whether icon or text is displayed inside dot, only the first character will be rendered for text                                                | **boolean**                                     | false   |
| active-icon                   | component of the icon displayed when in `on` state, overrides `active-text`                                                                     | **string** / **Component**                       | —       |
| inactive-icon                 | component of the icon displayed when in `off` state, overrides `inactive-text`                                                                  | **string** / **Component**                       | —       |
| active-action-icon (since 2.3.9)   | component of the icon displayed in action when in `on` state                                                                                    | **string** / **Component**                       | —       |
| inactive-action-icon (since 2.3.9) | component of the icon displayed in action when in `off` state                                                                                   | **string** / **Component**                       | —       |
| active-text                   | text displayed when in `on` state                                                                                                               | **string**                                      | ''      |
| inactive-text                 | text displayed when in `off` state                                                                                                              | **string**                                      | ''      |
| active-value                  | switch value when in `on` state                                                                                                                 | **boolean** / **string** / **number**             | true    |
| inactive-value                | switch value when in `off` state                                                                                                                | **boolean** / **string** / **number**             | false   |
| name                          | input name of Switch                                                                                                                            | **string**                                      | ''      |
| validate-event                | whether to trigger form validation                                                                                                              | **boolean**                                     | true    |
| before-change                 | before-change hook before the switch state changes. If `false` is returned or a `Promise` is returned and then is rejected, will stop switching | **Function**`() => Promise<boolean> \| boolean` | —       |
| id                            | id for input                                                                                                                                    | **string**                                      | —       |
| tabindex                      | tabindex for input                                                                                                                              | **string** / **number**                          | —       |
| aria-label (a11y) (since 2.7.2)   | same as `aria-label` in native input                                                                                                            | **string**                                      | —       |

### Events

| Name   | Description                 | Type                                                    |
| ------ | --------------------------- | ------------------------------------------------------- |
| change | triggers when value changes | **Function**`(val: boolean \| string \| number) => void` |

### Switch Slots

| Name                     | Description                |
| ------------------------ | -------------------------- |
| active-action (since 2.4.4)   | customize active action    |
| inactive-action (since 2.4.4) | customize inactive action  |
| active (since 2.13.0)         | customize active content   |
| inactive (since 2.13.0)       | customize inactive content |

### Exposes

| Method | Description                          | Type                    |
| ------ | ------------------------------------ | ----------------------- |
| focus  | manual focus to the switch component | **Function**`() => void` |

Removed legacy color props: use CSS variables `--el-switch-on-color`, `--el-switch-off-color`, and `--el-switch-border-color` instead; these props are absent from the 2.14.6 implementation.
