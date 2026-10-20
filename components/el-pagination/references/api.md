# pagination API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/pagination.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## API

### Attributes

| Name                                | Description                                                                                                                     | Type                                                                              | Default                              |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------ |
| size (since 2.7.6)                       | pagination size                                                                                                                 | **enum**`'large' \| 'default' \| 'small'`                                          | 'default'                            |
| background                          | whether the buttons have a background color                                                                                     | **boolean**                                                                        | false                                |
| page-size / v-model:page-size       | item count of each page                                                                                                         | **number**                                                                         | —                                    |
| default-page-size                   | default initial value of page size, not setting is the same as setting 10                                                       | **number**                                                                         | —                                    |
| total                               | total item count                                                                                                                | **number**                                                                         | —                                    |
| page-count                          | total page count. Set either `total` or `page-count` and pages will be displayed; if you need `page-sizes`, `total` is required | **number**                                                                         | —                                    |
| pager-count                         | number of pagers. Pagination collapses when the total page count exceeds this value                                             | **number**`5 \| 7 \| 9 \| 11 \| 13 \| 15 \| 17 \| 19 \| 21`                        | 7                                    |
| current-page / v-model:current-page | current page number                                                                                                             | **number**                                                                         | —                                    |
| default-current-page                | default initial value of current-page, not setting is the same as setting 1                                                     | **number**                                                                         | —                                    |
| layout                              | layout of Pagination, elements separated with a comma                                                                           | **string**`string (consists of sizes, prev, pager, next, jumper, ->, total, slot)` | prev, pager, next, jumper, ->, total |
| page-sizes                          | options of item count per page                                                                                                  | **array**`number[]`                                                                | [10, 20, 30, 40, 50, 100]            |
| append-size-to (since 2.8.4)             | which element the size dropdown appends to                                                                                      | **string**                                                                         | —                                    |
| popper-class                        | custom class name for the page size Select's dropdown                                                                           | **string**                                                                         | ''                                   |
| popper-style (since 2.11.5)              | custom style for the page size Select's dropdown                                                                                | **string** / **object**                                                             | —                                    |
| prev-text                           | text for the prev button                                                                                                        | **string**                                                                         | ''                                   |
| prev-icon                           | icon for the prev button, has a lower priority than `prev-text`                                                                 | **string** / **Component**                                                          | ArrowLeft                            |
| next-text                           | text for the next button                                                                                                        | **string**                                                                         | ''                                   |
| next-icon                           | icon for the next button, has a lower priority than `next-text`                                                                 | **string** / **Component**                                                          | ArrowRight                           |
| disabled                            | whether Pagination is disabled                                                                                                  | **boolean**                                                                        | false                                |
| teleported (since 2.3.13)                | whether Pagination select dropdown is teleported to the body                                                                    | **boolean**                                                                        | true                                 |
| hide-on-single-page                 | whether to hide when there's only one page                                                                                      | **boolean**                                                                        | false                                |
| small (deprecated)                 | whether to use small pagination                                                                                                 | **boolean**                                                                        | false                                |

> **Warning** 

We'll detect some deprecated usages, if your pagination don't appeared or worked as expected, please check rules below:

- You have to define one of `total` and `page-count`, otherwise we can't determine count of total pages.When both defined, `page-count` taken as priority.
- If `current-page` is defined, you have to listen `current-page` change, by also define `@update:current-page`, otherwise pagination didn't work.
- If `page-size` is defined while page size selector displayed(`sizes` included in `layout`), you have to listen `page-size` change as well, by define `@update:page-size`, otherwise change of page size didn't work.


### Events

| Name            | Description                                                       | Type                                                         |
| --------------- | ----------------------------------------------------------------- | ------------------------------------------------------------ |
| size-change     | triggers when `page-size` changes                                 | **Function**`(value: number) => void`                         |
| current-change  | triggers when `current-page` changes                              | **Function**`(value: number) => void`                         |
| change (since 2.4.4) | triggers when `current-page` or `page-size` changes               | **Function**`(currentPage: number, pageSize: number) => void` |
| prev-click      | triggers when the prev button is clicked and current page changes | **Function**`(value: number) => void`                         |
| next-click      | triggers when the next button is clicked and current page changes | **Function**`(value: number) => void`                         |

> **Warning** 

Events above are not recommended(but are still supported for compatible reason), better choice is to use the two-way data binding by `v-model`.


### Slots

| Name    | Description                                                         |
| ------- | ------------------------------------------------------------------- |
| default | custom content. To use this, you need to declare `slot` in `layout` |
