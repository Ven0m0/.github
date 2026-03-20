---
name: migrate-component
description: Migrate a component from one framework or library to another while preserving all behavior, props, tests, and accessibility. Use when asked to convert between React/Vue/Svelte/Angular or between component libraries (MUI to shadcn, etc).
allowed-tools: "Bash, Read, Write, Edit, Glob, Grep"
---

# Migrate Component

Migrate the `$0` component from `$1` to `$2`, preserving all existing behavior and tests.

<instructions>

## Workflow

Think step-by-step through the migration:

1. **Audit the source component**:
   - Read the component file and all its imports
   - Catalog: props/inputs, state, lifecycle hooks, event handlers, slots/children
   - Identify: styling approach, accessibility attributes, test coverage
   - Map dependencies to target framework equivalents

2. **Create a migration plan**:
   - List every prop, event, and behavior that must be preserved
   - Identify framework-specific patterns that need translation:

   | Source Pattern | Target Equivalent |
   |---------------|-------------------|
   | React `useState` | Vue `ref()` / Svelte `$state` |
   | React `useEffect` | Vue `onMounted` / Svelte `$effect` |
   | React `children` | Vue `<slot>` / Svelte `<slot>` |
   | Vue `v-model` | React controlled input / Svelte `bind:` |
   | Angular `@Input` | React props / Vue `defineProps` |

3. **Implement the migration**:
   - Write the new component following target framework idioms
   - Preserve all ARIA attributes, roles, and keyboard navigation
   - Maintain the same public API (prop names, events) where possible
   - Document any unavoidable API differences

4. **Migrate tests**:
   - Translate test assertions to target testing library
   - Ensure identical behavior coverage
   - Add any new edge case tests

5. **Update consumers**:
   - Find all files importing the old component
   - Update import paths and usage syntax
   - Verify no TypeScript/lint errors

6. **Verify**:
   - All tests pass
   - Visual behavior unchanged (if possible, side-by-side comparison)
   - No accessibility regressions
   - No console errors or warnings

</instructions>

<constraints>
- Never drop functionality during migration
- Preserve all accessibility attributes
- If the target framework cannot support a feature, document it and propose alternatives
- Keep the same file/directory structure conventions as the target project
</constraints>

<examples>

### React to Vue 3
```
Input: migrate-component UserCard React Vue3
Steps:
  1. Read UserCard.tsx: props (name, avatar, role), useState for expanded, onClick handler
  2. Plan: useState -> ref(), useEffect -> onMounted(), JSX -> template
  3. Write UserCard.vue with <script setup>, defineProps, ref()
  4. Migrate UserCard.test.tsx -> UserCard.test.ts using @vue/test-utils
  5. Update imports in pages/Profile.vue
```

### MUI to shadcn/ui
```
Input: migrate-component DataTable MUI shadcn
Steps:
  1. Read DataTable.tsx: MUI DataGrid props, custom renderers, sorting
  2. Plan: DataGrid -> shadcn Table + tanstack-table, theme tokens -> CSS variables
  3. Write DataTable.tsx with shadcn primitives, preserve column config API
  4. Update tests, verify sorting/filtering/pagination behavior
```

</examples>
