# tooltip API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/tooltip.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                      | Description                                                                                                                                                                           | Type                                                                                                                                                                        | Default           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| append-to                 | Which element the tooltip CONTENT appends to                                                                                                                                          | **CSSSelector** / **HTMLElement**                                                                                                                                             | —                 |
| effect                    | Tooltip theme, built-in theme: `dark` / `light`                                                                                                                                       | **enum**`'dark' \| 'light'`                                                                                                                                                  | dark              |
| content                   | Display content, can be overridden by `slot#content`                                                                                                                                  | **string**                                                                                                                                                                   | ''                |
| raw-content               | Whether `content` is treated as HTML string                                                                                                                                           | **boolean**                                                                                                                                                                  | false             |
| placement                 | Position of Tooltip                                                                                                                                                                   | **enum**`'top' \| 'top-start' \| 'top-end' \| 'bottom' \| 'bottom-start' \| 'bottom-end' \| 'left' \| 'left-start' \| 'left-end' \| 'right' \| 'right-start' \| 'right-end'` | bottom            |
| fallback-placements       | List of possible positions for Tooltip [popper.js](https://popper.js.org/docs/v2/modifiers/flip/#fallbackplacements)                                                                  | **array**`Placement[]`                                                                                                                                                       | —                 |
| visible / v-model:visible | Visibility of Tooltip                                                                                                                                                                 | **boolean**                                                                                                                                                                  | —                 |
| disabled                  | Whether Tooltip is disabled                                                                                                                                                           | **boolean**                                                                                                                                                                  | —                 |
| offset                    | Offset of the Tooltip                                                                                                                                                                 | **number**                                                                                                                                                                   | 12                |
| transition                | Animation name                                                                                                                                                                        | **string**                                                                                                                                                                   | —                 |
| popper-options            | [popper.js](https://popper.js.org/docs/v2/) parameters                                                                                                                                | **object**refer to [popper.js](https://popper.js.org/docs/v2/) doc                                                                                                           | {}                |
| arrow-offset (since 2.9.10)    | Controls the offset (padding) of the tooltip’s arrow relative to the popper.                                                                                                          | **number**                                                                                                                                                                   | 5                 |
| show-after                | Delay of appearance, in millisecond, not valid in controlled mode                                                                                                                     | **number**                                                                                                                                                                   | 0                 |
| show-arrow                | Whether the tooltip content has an arrow                                                                                                                                              | **boolean**                                                                                                                                                                  | true              |
| hide-after                | Delay of disappear, in millisecond, not valid in controlled mode                                                                                                                      | **number**                                                                                                                                                                   | 200               |
| auto-close                | Timeout in milliseconds to hide tooltip, not valid in controlled mode                                                                                                                 | **number**                                                                                                                                                                   | 0                 |
| popper-class              | Custom class name for Tooltip's popper                                                                                                                                                | **string**                                                                                                                                                                   | —                 |
| popper-style              | Custom style for Tooltip's popper                                                                                                                                                     | **string** / **object**                                                                                                                                                       | —                 |
| enterable                 | Whether the mouse can enter the tooltip                                                                                                                                               | **boolean**                                                                                                                                                                  | true              |
| teleported                | Whether tooltip content is teleported, if `true` it will be teleported to where `append-to` sets                                                                                      | **boolean**                                                                                                                                                                  | true              |
| trigger                   | How should the tooltip be triggered (to show), not valid in controlled mode                                                                                                           | **enum**`'hover' \| 'click' \| 'focus' \| 'contextmenu'` / **array**`Array<'click' \| 'focus' \| 'hover' \| 'contextmenu'>`                                                   | hover             |
| virtual-triggering        | Indicates whether virtual triggering is enabled                                                                                                                                       | **boolean**                                                                                                                                                                  | —                 |
| virtual-ref               | Indicates the reference element to which the tooltip is attached                                                                                                                      | **HTMLElement**                                                                                                                                                              | —                 |
| trigger-keys              | When you click the mouse to focus on the trigger element, you can define a set of keyboard codes to control the display of tooltip through the keyboard, not valid in controlled mode | **Array**                                                                                                                                                                    | ['Enter','Space'] |
| persistent                | When tooltip inactive and `persistent` is `false` , tooltip will be destroyed                                                                                                         | **boolean**                                                                                                                                                                  | —                 |
| aria-label (a11y)        | Same as `aria-label`                                                                                                                                                                  | **string**                                                                                                                                                                   | —                 |
| focus-on-target (since 2.11.2) | When triggering tooltips through hover, whether to focus the trigger element, which improves accessibility                                                                            | **boolean**                                                                                                                                                                  | false             |

### Events

| Name        | Description                                                           | Type                                 |
| ----------- | --------------------------------------------------------------------- | ------------------------------------ |
| before-show | Triggers before tooltip is shown. Passes trigger reason as argument.  | **Function**`(event?: Event) => void` |
| show        | Triggers when tooltip is shown. Passes trigger reason as argument.    | **Function**`(event?: Event) => void` |
| before-hide | Triggers before tooltip is hidden. Passes trigger reason as argument. | **Function**`(event?: Event) => void` |
| hide        | Triggers when tooltip is hidden. Passes trigger reason as argument.   | **Function**`(event?: Event) => void` |

### Slots

| Name    | Description                                                                    |
| ------- | ------------------------------------------------------------------------------ |
| default | Tooltip triggering & reference element, only a single root element is accepted |
| content | Customize content                                                              |

### Exposes

| Name                 | Description                                                       | Type                                                |
| -------------------- | ----------------------------------------------------------------- | --------------------------------------------------- |
| popperRef            | el-popper component instance                                      | **object**`Ref<PopperInstance \| undefined>`         |
| contentRef           | el-tooltip-content component instance                             | **object**`Ref<TooltipContentInstance \| undefined>` |
| isFocusInsideContent | Validate current focus event is trigger inside el-tooltip-content | **Function**`() => boolean \| undefined`             |
| updatePopper         | Update el-popper component instance                               | **Function**`() => void`                             |
| onOpen               | Expose onOpen function to manage el-tooltip open state            | **Function**`(event?: Event \| undefined) => void`   |
| onClose              | Expose onClose function to manage el-tooltip open state           | **Function**`(event?: Event \| undefined) => void`   |
| hide                 | Expose hide function                                              | **Function**`(event?: Event \| undefined) => void`   |

## FAQ

#### How to allow spaces in the input box when tooltip is nested?

Typical issue: [#20907](https://github.com/element-plus/element-plus/issues/20907)

```vue
<template>
  <el-tooltip content="tooltip content" placement="top" :trigger-keys="[]">
    <el-input v-model="value" placeholder="" />
  </el-tooltip>
</template>
```
