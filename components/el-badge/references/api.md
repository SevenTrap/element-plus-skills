# badge API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/badge.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                 | Description                                                                   | Type                                                               | Default |
| -------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------- |
| value                | display value.                                                                | **string** / **number**                                              | ''      |
| max                  | maximum value, shows `{max}+` when exceeded. Only works if value is a number. | **number**                                                          | 99      |
| is-dot               | if a little dot is displayed.                                                 | **boolean**                                                         | false   |
| hidden               | hidden badge.                                                                 | **boolean**                                                         | false   |
| type                 | badge type.                                                                   | **enum**`'primary' \| 'success' \| 'warning' \| 'danger' \| 'info'` | danger  |
| show-zero (since 2.6.0)   | Whether to show badge when value is zero.                                     | **boolean**                                                         | true    |
| color (since 2.6.3)       | background color of the dot                                                   | **string**                                                          |         |
| offset (since 2.7.0)      | offset of badge                                                               | **array**`[number, number]`                                         | [0, 0]  |
| badge-style (since 2.7.1) | custom style of badge                                                         | **object**`CSSProperties`                                           | —       |
| badge-class (since 2.7.1) | custom class of badge                                                         | **string**                                                          | —       |

### Slots

| Name             | Description               | Type                         |
| ---------------- | ------------------------- | ---------------------------- |
| default          | customize default content | -                            |
| content (since 2.9.1) | customize badge content   | **object**`{ value: string }` |
