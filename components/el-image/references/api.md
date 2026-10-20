# image API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/image.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Image API

### Image Attributes

| Name                   | Description                                                                                                                                       | Type                                                                    | Default |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------- |
| src                    | image source, same as native.                                                                                                                     | **string**                                                               | ''      |
| fit                    | indicate how the image should be resized to fit its container, same as [object-fit](https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit). | **enum**`'' \| 'fill' \| 'contain' \| 'cover' \| 'none' \| 'scale-down'` | ''      |
| hide-on-click-modal    | when enabling preview, use this flag to control whether clicking on backdrop can exit preview mode.                                               | **boolean**                                                              | false   |
| loading (since 2.2.3)       | Indicates how the browser should load the image, same as [native](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-loading).    | **enum**`'eager' \| 'lazy'`                                              | —       |
| lazy                   | whether to use lazy load.                                                                                                                         | **boolean**                                                              | false   |
| scroll-container       | the container to add scroll listener when using lazy load. By default, the container to add scroll listener when using lazy load.                 | **string** / **object**`HTMLElement`                                      | —       |
| alt                    | native attribute `alt`.                                                                                                                           | **string**                                                               | —       |
| referrerpolicy         | native attribute [referrerPolicy](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/referrerPolicy).                              | **string**                                                               | —       |
| crossorigin            | native attribute [crossorigin](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin).                                         | **enum**`'' \| 'anonymous' \| 'use-credentials'`                         | —       |
| preview-src-list       | allow big image preview.                                                                                                                          | **array**`string[]`                                                      | []      |
| z-index                | set image preview z-index.                                                                                                                        | **number**                                                               | —       |
| initial-index          | initial preview image index, less than the length of `url-list`.                                                                                  | **number**                                                               | 0       |
| close-on-press-escape  | whether the image-viewer can be closed by pressing ESC.                                                                                           | **boolean**                                                              | true    |
| preview-teleported     | whether to append image-viewer to body. A nested parent element attribute transform should have this attribute set to `true`.                     | **boolean**                                                              | false   |
| infinite               | whether the viewer preview is infinite.                                                                                                           | **boolean**                                                              | true    |
| zoom-rate              | the zoom rate of the image viewer zoom event.                                                                                                     | **number**                                                               | 1.2     |
| scale (since 2.11.3)        | the preview image scale.                                                                                                                          | **number**                                                               | 1       |
| min-scale (since 2.4.0)     | the min scale of the image viewer zoom event.                                                                                                     | **number**                                                               | 0.2     |
| max-scale (since 2.4.0)     | the max scale of the image viewer zoom event.                                                                                                     | **number**                                                               | 7       |
| show-progress (since 2.9.4) | whether to display the preview image progress content.                                                                                            | **boolean**                                                              | false   |

### Image Events

| Name   | Description                                                                                       | Type                                 |
| ------ | ------------------------------------------------------------------------------------------------- | ------------------------------------ |
| load   | same as native load.                                                                              | **Function**`(e: Event) => void`      |
| error  | same as native error.                                                                             | **Function**`(e: Event) => void`      |
| switch | trigger when switching images.                                                                    | **Function**`(index: number) => void` |
| close  | trigger when clicking on close button or when `hide-on-click-modal` enabled clicking on backdrop. | **Function**`() => void`              |
| show   | trigger when the viewer displays                                                                  | **Function**`() => void`              |

### Image Slots

| Name                                      | Description                                                           | Type |
| ----------------------------------------- | --------------------------------------------------------------------- | ---- |
| placeholder                               | custom placeholder content when image hasn't loaded yet.              | -    |
| error                                     | custom image load failed content.                                     | -    |
| [image viewer slots](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/image.md#image-viewer-slots) | when you allow big image preview, image viewer slots all can be used. | -    |

### Image Exposes

| Name                 | Description                     | Type                    |
| -------------------- | ------------------------------- | ----------------------- |
| showPreview (since 2.9.4) | manually open preview big image | **Function**`() => void` |

## Image Viewer API

### Image Viewer Attributes

| Name                   | Description                                                                                                                   | Type                  | Default |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------- | ------- |
| url-list               | preview link list.                                                                                                            | **array**`string[]`    | []      |
| z-index                | preview backdrop z-index.                                                                                                     | **number** / **string** | —       |
| initial-index          | the initial preview image index, less than or equal to the length of `url-list`.                                              | **number**             | 0       |
| infinite               | whether preview is infinite.                                                                                                  | **boolean**            | true    |
| hide-on-click-modal    | whether user can emit close event when clicking backdrop.                                                                     | **boolean**            | false   |
| teleported             | whether to append image itself to body. A nested parent element attribute transform should have this attribute set to `true`. | **boolean**            | false   |
| zoom-rate (since 2.2.27)    | the zoom rate of the image viewer zoom event.                                                                                 | **number**             | 1.2     |
| scale (since 2.11.3)        | the preview image scale.                                                                                                      | **number**             | 1       |
| min-scale (since 2.4.0)     | the min scale of the image viewer zoom event.                                                                                 | **number**             | 0.2     |
| max-scale (since 2.4.0)     | the max scale of the image viewer zoom event.                                                                                 | **number**             | 7       |
| close-on-press-escape  | whether the image-viewer can be closed by pressing ESC.                                                                       | **boolean**            | true    |
| show-progress (since 2.9.4) | whether to display the preview image progress content                                                                         | **boolean**            | false   |

### Image Viewer Events

| Name             | Description                                                                                       | Type                                 |
| ---------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------ |
| close            | trigger when clicking on close button or when `hide-on-click-modal` enabled clicking on backdrop. | **Function**`() => void`              |
| error (since 2.11.3)  | same as native error.                                                                             | **Function**`(e: Event) => void`      |
| switch           | trigger when switching images.                                                                    | **Function**`(index: number) => void` |
| rotate (since 2.3.13) | trigger when rotating images.                                                                     | **Function**`(deg: number) => void`   |

### Image Viewer Slots

| Name                   | Description                                                            | Type                                                                                                                                                                                                                |
| ---------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| viewer                 | custom content                                                         | -                                                                                                                                                                                                                   |
| progress (since 2.9.4)      | custom progress content (Priority is higher than `show-progress` prop) | **object**`{ activeIndex: number, total: number }`                                                                                                                                                                   |
| toolbar (since 2.9.4)       | custom toolbar content                                                 | **object**`{ actions: (action: ImageViewerAction, options?: ImageViewerActionOptions) => void, prev: () => void, next: () => void, reset: () => void, activeIndex: number, setActiveItem: (index: number) => void }` |
| viewer-error (since 2.11.3) | custom image load failed content.                                      | **object**`{ activeIndex: number, src: string }`                                                                                                                                                                     |

### Image Viewer Exposes

| Name          | Description           | Type                                 |
| ------------- | --------------------- | ------------------------------------ |
| setActiveItem | manually switch image | **Function**`(index: number) => void` |

## Type Declarations

<details>
  <summary>Show declarations</summary>

```ts
type ImageViewerAction = 'zoomIn' | 'zoomOut' | 'clockwise' | 'anticlockwise'
type ImageViewerActionOptions = {
  enableTransition?: boolean
  zoomRate?: number
  rotateDeg?: number
}
```

</details>
