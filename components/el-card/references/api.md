# card API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/card.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                  | Description                                                    | Type                              | Default |
| --------------------- | -------------------------------------------------------------- | --------------------------------- | ------- |
| header                | title of the card. Also accepts a DOM passed by `slot#header`  | **string**                         | —       |
| footer (since 2.4.3)       | footer of the card. Also accepts a DOM passed by `slot#footer` | **string**                         | —       |
| body-style            | CSS style of card body                                         | **object**`CSSProperties`          | —       |
| header-class (since 2.9.8) | custom class name of card header                               | **string**                         | —       |
| body-class (since 2.3.10)  | custom class name of card body                                 | **string**                         | —       |
| footer-class (since 2.9.8) | custom class name of card footer                               | **string**                         | —       |
| shadow                | when to show card shadows                                      | **enum**`always \| never \| hover` | always  |

### Slots

| Name    | Description                |
| ------- | -------------------------- |
| default | customize default content  |
| header  | content of the Card header |
| footer  | content of the Card footer |
