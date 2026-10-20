# container API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/container.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Container API

### Container Attributes

| Name      | Description                         | Type                                | Default                                                                    |
| --------- | ----------------------------------- | ----------------------------------- | -------------------------------------------------------------------------- |
| direction | layout direction for child elements | **enum**`'horizontal' \| 'vertical'` | vertical when nested with `el-header` or `el-footer`; horizontal otherwise |

### Container Slots

| Name    | Description               | Subtags                                    |
| ------- | ------------------------- | ------------------------------------------ |
| default | customize default content | Container / Header / Aside / Main / Footer |

## Header API

### Header Attributes

| Name   | Description          | Type      | Default |
| ------ | -------------------- | --------- | ------- |
| height | height of the header | **string** | 60px    |

### Header Slots

| Name    | Description               |
| ------- | ------------------------- |
| default | customize default content |

## Aside API

### Aside Attributes

| Name  | Description               | Type      | Default |
| ----- | ------------------------- | --------- | ------- |
| width | width of the side section | **string** | 300px   |

### Aside Slots

| Name    | Description               |
| ------- | ------------------------- |
| default | customize default content |

## Main API

### Main Slots

| Name    | Description               |
| ------- | ------------------------- |
| default | customize default content |

## Footer API

### Footer Attributes

| Name   | Description          | Type      | Default |
| ------ | -------------------- | --------- | ------- |
| height | height of the footer | **string** | 60px    |

### Footer Slots

| Name    | Description               |
| ------- | ------------------------- |
| default | customize default content |
