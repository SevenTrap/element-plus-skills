# Element Plus Skills 技能库

适用于 **Element Plus 2.14.6**，Vue peer dependency 为 `^3.3.7`。

[English](README.md) · [技能入口](SKILL.md) · [组件索引](element-plus-components/SKILL.md) · [版本核对依据](references/version-baseline.md)

## 技能范围

包含 **89 个主题技能，加上根路由技能，共 90 个 SKILL.md**。

| 类别 | 数量 | 内容 |
| --- | --- | --- |
| 组件 | 78 | `components/el-*/SKILL.md`，包含 InputOtp |
| 基础 | 6 | 快速开始、主题、国际化、暗色模式、SSR、组件索引 |
| 设计 | 5 | 概览、边框、颜色、字体、栅格布局 |

组件技能说明选型、关键行为、废弃项和示例；完整属性、事件、插槽及暴露方法放在各自的 `references/api.md`，需要时再读取。子组件按组件家族组织，例如 ImageViewer 归入 Image、Countdown 归入 Statistic、FormItem 归入 Form、TableColumn 归入 Table、AutoResizer 归入 Table V2。布局技能覆盖 Row 和 Col。

## 使用方法

从 [SKILL.md](SKILL.md) 选择主题，再读取具体技能。应用中固定安装目标版本：

```sh
npm install --save-exact element-plus@2.14.6
```

按照[快速开始](element-plus-quickstart/SKILL.md)配置组件注册、样式、图标、自动导入和 TypeScript。单独导入组件不会自动引入全局样式。

日期时间选择使用 `el-date-picker` 的 `datetime` 或 `datetimerange` 类型；不存在独立导出的 `el-datetime-picker`。普通 Select、Tree、Table 与各自的虚拟化版本具有不同 API，不能直接互换。

## 版本依据

以官方 `2.14.6` 标签的文档、类型和实现为准，对照已固定提交的 `dev` 分支检查差异。不能将当前在线文档里的新功能直接当成 2.14.6 的能力，例如后续的 Drawer 对象形式 `resizable`、Scrollbar `mask` 和 Image `viewer-placeholder`。

[版本基线](references/version-baseline.md)记录两个提交、排除项和官方文档错误的源码修正；[来源清单](references/source-manifest.json)记录组件参考文件及原文的 SHA-256。

## 维护与验证

修改技能时，同步核对 API、示例、版本声明及引用。对文档疑点，以同一标签的源码为准。修正 API 参考文件后更新来源清单中的内容哈希，并保留上游版权信息。

```sh
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/validate_skills.py
```

验证脚本需要 Python 3 和 PyYAML，检查元数据、本地链接、代码围栏及版本边界。应用仍需执行自己的 Vue/TypeScript 检查和交互测试。维护约定见 [AGENTS.md](AGENTS.md)。

## 许可证

本库使用 [MIT 许可证](LICENSE)。改编的 Element Plus 文档保留[上游 MIT 声明](references/upstream-LICENSE)。
