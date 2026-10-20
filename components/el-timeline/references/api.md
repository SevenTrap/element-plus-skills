# timeline API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/timeline.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Timeline API

### Timeline Attributes

| Name              | Description                               | Type                                                            | Default |
| ----------------- | ----------------------------------------- | --------------------------------------------------------------- | ------- |
| reverse (since 2.11.9) | whether reverse order                     | **boolean**                                                      | false   |
| mode (since 2.13.1)    | relative position of timeline and content | **enum**`'start' \| 'alternate' \| 'alternate-reverse' \| 'end'` | start   |

### Timeline Slots

| Name    | Description                            | Subtags       |
| ------- | -------------------------------------- | ------------- |
| default | customize default content for timeline | Timeline-Item |

## Timeline-Item API

### Timeline-Item Attributes

| Name           | Description                 | Type                                                               | Default |
| -------------- | --------------------------- | ------------------------------------------------------------------ | ------- |
| timestamp      | timestamp content           | **string**                                                          | ''      |
| hide-timestamp | whether to show timestamp   | **boolean**                                                         | false   |
| center         | whether vertically centered | **boolean**                                                         | false   |
| placement      | position of timestamp       | **enum**`'top' \| 'bottom'`                                         | bottom  |
| type           | node type                   | **enum**`'primary' \| 'success' \| 'warning' \| 'danger' \| 'info'` | ''      |
| color          | background color of node    | **string**                                                          | ''      |
| size           | node size                   | **enum**`'normal' \| 'large'`                                       | normal  |
| icon           | icon component              | **string** / **Component**                                           | —       |
| hollow         | icon is hollow              | **boolean**                                                         | false   |

### Timeline-Item Slots

| Name    | Description                                 |
| ------- | ------------------------------------------- |
| default | customize default content for timeline item |
| dot     | customize defined node for timeline item    |
