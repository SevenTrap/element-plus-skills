# page-header API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/page-header.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name    | Description                                                   | Type                     | Default |
| ------- | ------------------------------------------------------------- | ------------------------ | ------- |
| icon    | icon component of page header                                 | **string** / **Component** | Back    |
| title   | main title of page header, default is Back that built-in a11y | **string**                | ''      |
| content | content of page header                                        | **string**                | ''      |

### Events

| Name | Description                         | Type                    |
| ---- | ----------------------------------- | ----------------------- |
| back | triggers when right side is clicked | **Function**`() => void` |

### Slots

| Name       | Description           |
| ---------- | --------------------- |
| icon       | content as icon       |
| title      | content as title      |
| content    | content               |
| extra      | extra                 |
| breadcrumb | content as breadcrumb |
| default    | main content          |
