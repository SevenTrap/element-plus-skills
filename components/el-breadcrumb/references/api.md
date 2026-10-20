# breadcrumb API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/breadcrumb.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Breadcrumb API

### Breadcrumb Attributes

| Name           | Description                      | Type                     | Default |
| -------------- | -------------------------------- | ------------------------ | ------- |
| separator      | separator character              | **string**                | /       |
| separator-icon | icon component of icon separator | **string** / **Component** | —       |

### Breadcrumb Slots

| Name    | Description               | Subtags         |
| ------- | ------------------------- | --------------- |
| default | customize default content | Breadcrumb Item |

## BreadcrumbItem API

### BreadcrumbItem Attributes

| Name    | Description                                               | Type                                    | Default |
| ------- | --------------------------------------------------------- | --------------------------------------- | ------- |
| to      | target route of the link, same as `to` of `vue-router`    | **string** / **object**`RouteLocationRaw` | ''      |
| replace | if `true`, the navigation will not leave a history record | **boolean**                              | false   |

### BreadcrumbItem Slots

| Name    | Description               |
| ------- | ------------------------- |
| default | customize default content |
