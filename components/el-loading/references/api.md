# loading API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/loading.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Options

| Name                 | Description                                                                                                                                                              | Type                                     | Default       |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------- | ------------- |
| target               | the DOM node Loading needs to cover. Accepts a DOM object or a string. If it's a string, it will be passed to `document.querySelector` to get the corresponding DOM node | **string** / **HTMLElement**               | document.body |
| body                 | same as the `body` modifier of `v-loading`                                                                                                                               | **boolean**                               | false         |
| fullscreen           | same as the `fullscreen` modifier of `v-loading`                                                                                                                         | **boolean**                               | true          |
| lock                 | same as the `lock` modifier of `v-loading`                                                                                                                               | **boolean**                               | false         |
| text                 | loading text that displays under the spinner                                                                                                                             | **string** / **VNode** / **array**`VNode[]` | —             |
| spinner              | class name of the custom spinner                                                                                                                                         | **string**                                | —             |
| background           | background color of the mask                                                                                                                                             | **string**                                | —             |
| customClass          | custom class name for loading                                                                                                                                            | **string**                                | —             |
| svg                  | custom SVG element to override the default loading spinner                                                                                                               | **string**                                | —             |
| svgViewBox           | sets the viewBox attribute for loading svg element                                                                                                                       | **string**                                | —             |
| beforeClose (since 2.7.8) | Function executed before loading attempts to close. If this function returns false, the closing process will be aborted. Otherwise, the loading will close.              | **Function**`() => boolean`               | —             |
| closed (since 2.7.8)      | Function triggered after loading has completely closed                                                                                                                   | **Function**`() => void`                  | —             |

### Directives

| Name                         | Description                                                  | Type                           |
| ---------------------------- | ------------------------------------------------------------ | ------------------------------ |
| v-loading                    | show animation while loading data                            | **boolean** / **LoadingOptions** |
| element-loading-text         | loading text that displays under the spinner                 | **string**                      |
| element-loading-spinner      | icon of the custom spinner                                   | **string**                      |
| element-loading-svg          | icon of the custom spinner (same as element-loading-spinner) | **string**                      |
| element-loading-svg-view-box | sets the viewBox attribute for loading svg element           | **string**                      |
| element-loading-background   | background color of the mask                                 | **string**                      |
| element-loading-custom-class | custom class name for loading                                | **string**                      |
