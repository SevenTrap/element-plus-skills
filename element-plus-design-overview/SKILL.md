---
name: element-plus-design-overview
description: Apply Element Plus design disciplines of consistency, feedback, efficiency, and controllability; locate the matching token and layout skills.
metadata:
  author: jiaiyan
  version: "2.0.0"
  element-plus-version: "2.14.6"
---

# Design overview — Element Plus 2.14.6

Use this skill when choosing interaction and visual conventions for an Element Plus interface. For component discovery, use the [component index](../element-plus-components/SKILL.md).

## Apply the four design disciplines

- **Consistency:** use familiar language and consistent icon meanings, text, alignment, and component states. Use the same component pattern for the same task.
- **Feedback:** make actions and current state perceptible. Bind loading and disabled states to application state, display validation results, and provide success or failure feedback when it helps the user proceed.
- **Efficiency:** simplify the task sequence, make choices clear, and keep relevant actions discoverable without requiring users to memorize them.
- **Controllability:** preserve deliberate user choices. Provide cancel or exit actions and describe consequential operations clearly.

## Load the needed design reference

| Decision | Skill |
| --- | --- |
| Semantic colors, text colors, fills and backgrounds | [Color](../element-plus-design-color/SKILL.md) |
| Borders, corner radii, shadows | [Border](../element-plus-design-border/SKILL.md) |
| Font families, sizes and hierarchy | [Typography](../element-plus-design-typography/SKILL.md) |
| 24-column grid, gutters and responsive breakpoints | [Layout](../element-plus-design-layout/SKILL.md) |
| Runtime or Sass theme customization | [Theming](../element-plus-theming/SKILL.md) |
| Dark theme tokens and root activation | [Dark mode](../element-plus-dark-mode/SKILL.md) |

Use component props and published CSS variables before overriding internal DOM selectors. Apply semantic tokens rather than copying light-theme hex values into all contexts.

Source: [2.14.6 design guide](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/guide/design.md). The conventions describe the target release; they do not imply that a component validates business rules or authorizes an action.
