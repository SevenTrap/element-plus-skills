# result API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/result.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name      | Description         | Type                                                                       | Default |
| --------- | ------------------- | -------------------------------------------------------------------------- | ------- |
| title     | title of result     | **string**                                                                  | ''      |
| sub-title | sub title of result | **string**                                                                  | ''      |
| icon      | icon type of result | **enum**`'primary' (2.9.11) \| 'success' \| 'warning' \| 'info' \| 'error'` | info    |

### Slots

| Name      | Description                  |
| --------- | ---------------------------- |
| icon      | content as result icon       |
| title     | content as result title      |
| sub-title | content as result sub title  |
| extra     | content as result extra area |
