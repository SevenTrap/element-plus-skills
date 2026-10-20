---
name: element-plus-components
description: Choose Element Plus 2.14.6 components and locate their individual skills, including virtualized alternatives, panels, services, and directives.
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Component selection — Element Plus 2.14.6

This index covers **78 component skills**. Categories follow the target release's documentation sidebar. Companion components such as FormItem, TableColumn, ImageViewer, Countdown, and AutoResizer are documented with their parent family. Grid Row/Col is in the [layout design skill](../element-plus-design-layout/SKILL.md).

## Choose by behavior

- Use Select V2, Tree V2, or Table V2 for virtualization. Their APIs differ from Select, Tree, and Table; do not interchange props or claim ordinary Select virtualizes its options.
- DateTimePicker is `ElDatePicker` with `type="datetime"` or `type="datetimerange"`; there is no exported `ElDatetimePicker` component.
- DatePickerPanel, ColorPickerPanel, InputOtp, and Table V2 carry beta labels in the 2.14.6 docs. Tree V2 is also documented as beta.
- Loading is a directive/service; Message, MessageBox, and Notification provide programmatic APIs. Follow each skill's imports and cleanup behavior.
- InfiniteScroll remains available but deprecated. Prefer Scrollbar's `end-reached` event with application loading and exhaustion guards.
- The standalone panel components do not automatically inherit every picker-wrapper prop. Use the specific panel API.
- For full plugin registration, styles, and automatic imports, read [quickstart](../element-plus-quickstart/SKILL.md).

## Basic (8)

| Component | Skill |
| --- | --- |
| Button | [el-button](../components/el-button/SKILL.md) |
| Layout Container | [el-container](../components/el-container/SKILL.md) |
| Icon | [el-icon](../components/el-icon/SKILL.md) |
| Link | [el-link](../components/el-link/SKILL.md) |
| Text | [el-text](../components/el-text/SKILL.md) |
| Scrollbar | [el-scrollbar](../components/el-scrollbar/SKILL.md) |
| Space | [el-space](../components/el-space/SKILL.md) |
| Splitter | [el-splitter](../components/el-splitter/SKILL.md) |

## Configuration (1)

| Component | Skill |
| --- | --- |
| Config Provider | [el-config-provider](../components/el-config-provider/SKILL.md) |

## Form (25)

| Component | Skill |
| --- | --- |
| Autocomplete | [el-autocomplete](../components/el-autocomplete/SKILL.md) |
| Cascader | [el-cascader](../components/el-cascader/SKILL.md) |
| Checkbox | [el-checkbox](../components/el-checkbox/SKILL.md) |
| Color Picker Panel | [el-color-picker-panel](../components/el-color-picker-panel/SKILL.md) |
| Color Picker | [el-color-picker](../components/el-color-picker/SKILL.md) |
| Date Picker Panel | [el-date-picker-panel](../components/el-date-picker-panel/SKILL.md) |
| Date Picker | [el-date-picker](../components/el-date-picker/SKILL.md) |
| DateTime Picker | [el-datetime-picker](../components/el-datetime-picker/SKILL.md) |
| Form | [el-form](../components/el-form/SKILL.md) |
| Input | [el-input](../components/el-input/SKILL.md) |
| Input Number | [el-input-number](../components/el-input-number/SKILL.md) |
| Input Tag | [el-input-tag](../components/el-input-tag/SKILL.md) |
| Input OTP | [el-input-otp](../components/el-input-otp/SKILL.md) |
| Mention | [el-mention](../components/el-mention/SKILL.md) |
| Radio | [el-radio](../components/el-radio/SKILL.md) |
| Rate | [el-rate](../components/el-rate/SKILL.md) |
| Select | [el-select](../components/el-select/SKILL.md) |
| Virtualized Select | [el-select-v2](../components/el-select-v2/SKILL.md) |
| Slider | [el-slider](../components/el-slider/SKILL.md) |
| Switch | [el-switch](../components/el-switch/SKILL.md) |
| Time Picker | [el-time-picker](../components/el-time-picker/SKILL.md) |
| Time Select | [el-time-select](../components/el-time-select/SKILL.md) |
| Transfer | [el-transfer](../components/el-transfer/SKILL.md) |
| TreeSelect | [el-tree-select](../components/el-tree-select/SKILL.md) |
| Upload | [el-upload](../components/el-upload/SKILL.md) |

## Data (23)

| Component | Skill |
| --- | --- |
| Avatar | [el-avatar](../components/el-avatar/SKILL.md) |
| Badge | [el-badge](../components/el-badge/SKILL.md) |
| Calendar | [el-calendar](../components/el-calendar/SKILL.md) |
| Card | [el-card](../components/el-card/SKILL.md) |
| Carousel | [el-carousel](../components/el-carousel/SKILL.md) |
| Collapse | [el-collapse](../components/el-collapse/SKILL.md) |
| Descriptions | [el-descriptions](../components/el-descriptions/SKILL.md) |
| Empty | [el-empty](../components/el-empty/SKILL.md) |
| Image | [el-image](../components/el-image/SKILL.md) |
| Infinite Scroll | [el-infinite-scroll](../components/el-infinite-scroll/SKILL.md) |
| Pagination | [el-pagination](../components/el-pagination/SKILL.md) |
| Progress | [el-progress](../components/el-progress/SKILL.md) |
| Result | [el-result](../components/el-result/SKILL.md) |
| Skeleton | [el-skeleton](../components/el-skeleton/SKILL.md) |
| Table | [el-table](../components/el-table/SKILL.md) |
| Virtualized Table | [el-table-v2](../components/el-table-v2/SKILL.md) |
| Tag | [el-tag](../components/el-tag/SKILL.md) |
| Timeline | [el-timeline](../components/el-timeline/SKILL.md) |
| Tour | [el-tour](../components/el-tour/SKILL.md) |
| Tree | [el-tree](../components/el-tree/SKILL.md) |
| Virtualized Tree | [el-tree-v2](../components/el-tree-v2/SKILL.md) |
| Statistic | [el-statistic](../components/el-statistic/SKILL.md) |
| Segmented | [el-segmented](../components/el-segmented/SKILL.md) |

## Navigation (9)

| Component | Skill |
| --- | --- |
| Affix | [el-affix](../components/el-affix/SKILL.md) |
| Anchor | [el-anchor](../components/el-anchor/SKILL.md) |
| Backtop | [el-backtop](../components/el-backtop/SKILL.md) |
| Breadcrumb | [el-breadcrumb](../components/el-breadcrumb/SKILL.md) |
| Dropdown | [el-dropdown](../components/el-dropdown/SKILL.md) |
| Menu | [el-menu](../components/el-menu/SKILL.md) |
| Page Header | [el-page-header](../components/el-page-header/SKILL.md) |
| Steps | [el-steps](../components/el-steps/SKILL.md) |
| Tabs | [el-tabs](../components/el-tabs/SKILL.md) |

## Feedback (10)

| Component | Skill |
| --- | --- |
| Alert | [el-alert](../components/el-alert/SKILL.md) |
| Dialog | [el-dialog](../components/el-dialog/SKILL.md) |
| Drawer | [el-drawer](../components/el-drawer/SKILL.md) |
| Loading | [el-loading](../components/el-loading/SKILL.md) |
| Message | [el-message](../components/el-message/SKILL.md) |
| Message Box | [el-message-box](../components/el-message-box/SKILL.md) |
| Notification | [el-notification](../components/el-notification/SKILL.md) |
| Popconfirm | [el-popconfirm](../components/el-popconfirm/SKILL.md) |
| Popover | [el-popover](../components/el-popover/SKILL.md) |
| Tooltip | [el-tooltip](../components/el-tooltip/SKILL.md) |

## Others (2)

| Component | Skill |
| --- | --- |
| Divider | [el-divider](../components/el-divider/SKILL.md) |
| Watermark | [el-watermark](../components/el-watermark/SKILL.md) |

Source: [2.14.6 documentation categories](https://github.com/element-plus/element-plus/blob/2.14.6/docs/.vitepress/crowdin/en-US/pages/component.json). Read each component's linked `references/api.md` only when its full contract is needed.
