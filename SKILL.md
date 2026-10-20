---
name: element-plus-skills
description: Use Element Plus 2.14.6 in Vue applications; route component, installation, theming, localization, SSR, and design requests to the corresponding skills.
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Element Plus skills — 2.14.6

This library targets **Element Plus 2.14.6** with Vue `^3.3.7`. It contains **89 topic skills** (78 component, 6 foundation, 5 design), plus this routing skill: **90 SKILL.md files** total.

## Route the request

| Need | Read |
| --- | --- |
| Select a component or find its API | [Component index](element-plus-components/SKILL.md) |
| Install, register, import styles or configure TypeScript | [Quickstart](element-plus-quickstart/SKILL.md) |
| Customize CSS variables or Sass | [Theming](element-plus-theming/SKILL.md) |
| Localize components and date formatting | [Internationalization](element-plus-i18n/SKILL.md) |
| Activate or customize dark mode | [Dark mode](element-plus-dark-mode/SKILL.md) |
| SSR IDs, z-index and teleport hydration | [SSR](element-plus-ssr/SKILL.md) |
| Interaction and visual conventions | [Design overview](element-plus-design-overview/SKILL.md) |
| Color tokens | [Color](element-plus-design-color/SKILL.md) |
| Borders, radii and shadows | [Border](element-plus-design-border/SKILL.md) |
| Grid and responsive breakpoints | [Layout](element-plus-design-layout/SKILL.md) |
| Fonts and text hierarchy | [Typography](element-plus-design-typography/SKILL.md) |

For a named component, open `components/el-{name}/SKILL.md`. Read only the relevant skill, then its linked `references/api.md` when exact props, events, slots, types or exposes are needed. Examples assume the stylesheet setup described in quickstart.

## Version rules

- Use the fixed 2.14.6 API and implementation. `dev` is a comparison source and may contain unreleased or later-version changes.
- DateTimePicker uses `el-date-picker`; services and directives are not ordinary component tags. Follow the selected skill's actual registration and import instructions.
- Keep deprecated APIs distinct from removed ones. A future 3.0 removal notice does not mean the API has already been removed in 2.14.6.
- Version labels on API rows state the introduction version. They do not permit adopting a row introduced after 2.14.6.
- The [version baseline](references/version-baseline.md) records the exact tag/dev commits and known documentation corrections. The [source manifest](references/source-manifest.json) records each component reference's provenance.
