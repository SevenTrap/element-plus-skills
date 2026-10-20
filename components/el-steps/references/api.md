# steps API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/steps.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Steps API

### Steps Attributes

| Name           | Description                                                                   | Type                                                             | Default    |
| -------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------- | ---------- |
| space          | the spacing of each step, will be responsive if omitted. Supports percentage. | **number** / **string**                                            | ''         |
| direction      | display direction                                                             | **enum**`'vertical' \| 'horizontal'`                              | horizontal |
| active         | current activation step                                                       | **number**                                                        | 0          |
| process-status | status of current step                                                        | **enum**`'wait' \| 'process' \| 'finish' \| 'error' \| 'success'` | process    |
| finish-status  | status of end step                                                            | **enum**`'wait' \| 'process' \| 'finish' \| 'error' \| 'success'` | finish     |
| align-center   | center title and description                                                  | **boolean**                                                       | —          |
| simple         | whether to apply simple theme                                                 | **boolean**                                                       | —          |

### Steps Events

| Name   | Description                           | Parameters                                            |
| ------ | ------------------------------------- | ----------------------------------------------------- |
| change | triggers when the active step changes | **Function**`(newVal: number, oldVal: number) => void` |

### Steps Slots

| Name    | Description               | Subtags |
| ------- | ------------------------- | ------- |
| default | customize default content | Step    |

## Step API

### Step Attributes

| Name        | Description                                                              | Type                                                                   | Default |
| ----------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------- | ------- |
| title       | step title                                                               | **string**                                                              | ''      |
| description | step description                                                         | **string**                                                              | ''      |
| icon        | step custom icon. Icons can be passed via named slot as well             | **string** / **Component**                                               | —       |
| status      | current status. It will be automatically set by Steps if not configured. | **enum**`'' \| 'wait' \| 'process' \| 'finish' \| 'error' \| 'success'` | ''      |

### Step Slots

| Name        | Description      |
| ----------- | ---------------- |
| icon        | custom icon      |
| title       | step title       |
| description | step description |
