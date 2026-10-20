# infinite-scroll API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/infinite-scroll.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Directives

| Name                      | Description                                                                                                      | Type        | Default |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------- | ----------- | ------- |
| v-infinite-scroll         | Load more data while reach bottom of the page                                                                    | **Function** | —       |
| infinite-scroll-disabled  | is disabled                                                                                                      | **boolean**  | false   |
| infinite-scroll-delay     | throttle delay (ms)                                                                                              | **number**   | 200     |
| infinite-scroll-distance  | trigger distance (px)                                                                                            | **number**   | 0       |
| infinite-scroll-immediate | Whether to execute the loading method immediately, in case the content cannot be filled up in the initial state. | **boolean**  | true    |
