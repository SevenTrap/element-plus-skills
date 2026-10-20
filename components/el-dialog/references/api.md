# dialog API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/dialog.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                       | Description                                                                                                                    | Type                                   | Default     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------- | ----------- |
| model-value / v-model      | visibility of Dialog                                                                                                           | **boolean**                             | false       |
| title                      | title of Dialog. Can also be passed with a named slot (see the following table)                                                | **string**                              | ''          |
| width                      | width of Dialog, default is 50%                                                                                                | **string** / **number**                  | ''          |
| fullscreen                 | whether the Dialog takes up full screen                                                                                        | **boolean**                             | false       |
| top                        | value for `margin-top` of Dialog CSS, default is 15vh                                                                          | **string**                              | ''          |
| modal                      | whether a mask is displayed                                                                                                    | **boolean**                             | true        |
| modal-penetrable (since 2.10.5) | whether the mask is penetrable. The modal attribute must be `false`.                                                           | **boolean**                             | false       |
| modal-class                | custom class names for mask                                                                                                    | **string**                              | —           |
| header-class (since 2.9.3)      | custom class names for header wrapper                                                                                          | **string**                              | —           |
| body-class (since 2.9.3)        | custom class names for body wrapper                                                                                            | **string**                              | —           |
| footer-class (since 2.9.3)      | custom class names for footer wrapper                                                                                          | **string**                              | —           |
| append-to-body             | whether to append Dialog itself to body. A nested Dialog should have this attribute set to `true`                              | **boolean**                             | false       |
| append-to (since 2.4.3)         | which element the Dialog appends to. Will override `append-to-body`                                                            | **CSSSelector** / **HTMLElement**        | body        |
| lock-scroll                | whether scroll of body is disabled while Dialog is displayed                                                                   | **boolean**                             | true        |
| open-delay                 | the Time(milliseconds) before open                                                                                             | **number**                              | 0           |
| close-delay                | the Time(milliseconds) before close                                                                                            | **number**                              | 0           |
| close-on-click-modal       | whether the Dialog can be closed by clicking the mask                                                                          | **boolean**                             | true        |
| close-on-press-escape      | whether the Dialog can be closed by pressing ESC                                                                               | **boolean**                             | true        |
| show-close                 | whether to show a close button                                                                                                 | **boolean**                             | true        |
| before-close               | callback before Dialog closes, and it will prevent Dialog from closing, use done to close the dialog                           | **Function**`(done: DoneFn) => void`    | —           |
| draggable                  | enable dragging feature for Dialog                                                                                             | **boolean**                             | false       |
| overflow (since 2.5.4)          | draggable Dialog can overflow the viewport                                                                                     | **boolean**                             | false       |
| center                     | whether to align the header and footer in center                                                                               | **boolean**                             | false       |
| align-center (since 2.2.16)     | whether to align the dialog both horizontally and vertically                                                                   | **boolean**                             | false       |
| destroy-on-close           | destroy elements in Dialog when closed                                                                                         | **boolean**                             | false       |
| close-icon                 | custom close icon, default is Close                                                                                            | **string** / **Component**               | —           |
| z-index                    | same as z-index in native CSS, z-order of dialog                                                                               | **number**                              | —           |
| header-aria-level (a11y)  | header's `aria-level` attribute                                                                                                | **string**                              | 2           |
| transition (since 2.10.5)       | custom transition configuration for dialog animation. Can be a string (transition name) or an object with Vue transition props | **string** / **object**`TransitionProps` | dialog-fade |

> **Warning** 



### Slots

| Name                | Description                                                                                           |
| ------------------- | ----------------------------------------------------------------------------------------------------- |
| default             | default content of Dialog                                                                             |
| header              | content of the Dialog header; Replacing this removes the title, but does not remove the close button. |
| footer              | content of the Dialog footer                                                                          |
| title (deprecated) | works the same as the header slot. Use that instead.                                                  |

> **Warning** 

`title` has been **deprecated**, and **will be** removed in (3.0.0), please use `header`.


### Events

| Name             | Description                                      | Type                    |
| ---------------- | ------------------------------------------------ | ----------------------- |
| open             | triggers when the Dialog opens                   | **Function**`() => void` |
| opened           | triggers when the Dialog opening animation ends  | **Function**`() => void` |
| close            | triggers when the Dialog closes                  | **Function**`() => void` |
| closed           | triggers when the Dialog closing animation ends  | **Function**`() => void` |
| open-auto-focus  | triggers after Dialog opens and content focused  | **Function**`() => void` |
| close-auto-focus | triggers after Dialog closed and content focused | **Function**`() => void` |

### Exposes

| Name                   | Description    | Type                    |
| ---------------------- | -------------- | ----------------------- |
| resetPosition (since 2.8.1) | reset position | **Function**`() => void` |
| handleClose (since 2.9.8)   | close dialog   | **Function**`() => void` |

## FAQ

#### Using dialog in SFC, the scope style does not take effect

Typical issue: [#10515](https://github.com/element-plus/element-plus/issues/10515)

PS: Since the dialog is rendered using `Teleport`, the style of the root node is recommended to be written globally.

#### When the dialog is displayed and hidden, there is a situation where the page elements are displaced back and forth

Typical issue: [#10481](https://github.com/element-plus/element-plus/issues/10481)

PS: It is recommended to place the scroll area inside a vue mounted node, e.g. `<div id="app" />`, and use the `overflow: hidden` style for the body.
