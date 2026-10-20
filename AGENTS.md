# Element Plus skills maintenance

This directory is a versioned skill library for **Element Plus 2.14.6**. Start at [SKILL.md](SKILL.md) and route to the relevant topic; do not load the entire library for a single component question.

## Layout and ownership

- `components/el-*/SKILL.md`: component-family decisions, pitfalls and examples.
- `components/el-*/references/api.md`: exact target-version API contracts, read on demand.
- `element-plus-*/SKILL.md`: foundation and design topics; [component index](element-plus-components/SKILL.md) enumerates all component skills.
- [Version baseline](references/version-baseline.md): tag/dev commits, compatibility boundaries and source corrections.
- [Source manifest](references/source-manifest.json): component reference provenance and hashes.
- `scripts/`: local validation and its tests.

There are 78 component skills, 6 foundation skills, 5 design skills and the root router: 90 skill files. These are topic counts, not exported-component counts.

## Version maintenance

1. Use the official target tag's docs, examples and `packages/components` implementation. Compare `dev` separately and record its commit. Do not add later APIs merely because current online documentation shows them.
2. Check defaults and exposed methods against source when docs disagree. Preserve deprecated-but-supported behavior accurately and distinguish a future removal notice from an already removed API.
3. Keep skill metadata `element-plus-version: "2.14.6"` and application install examples pinned. Skill metadata `version` describes the skill revision separately.
4. Keep entrypoints concise; exact API tables belong in the linked reference. Do not duplicate parameter catalogs across README, AGENTS and SKILL files.
5. Keep example imports and reactive state complete. Component examples require registration and styles described in [quickstart](element-plus-quickstart/SKILL.md); source monorepo aliases are not public import paths.
6. Update manifest hashes after correcting reference contents and retain the [upstream license](references/upstream-LICENSE).

## Checks

```sh
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/validate_skills.py
```

Also check a changed example in an appropriate Vue/TypeScript application when possible. Structural validation alone cannot prove runtime or accessibility behavior. Avoid changing unrelated projects, user configuration or external resources while maintaining this directory.
