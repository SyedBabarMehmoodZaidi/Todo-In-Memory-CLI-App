# Tasks: In-Memory Python Console Todo App (Phase I)

**Input**: Design documents from `/specs/001-todo-cli-phase1/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Initialize UV project with `uv init`
- [x] T002 Configure project structure (src/app/models, src/app/services, src/app/ui, tests/unit)
- [x] T003 [P] Add `pytest` as a development dependency using `uv add --dev pytest`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [x] T004 Create `Task` dataclass in `src/app/models/task.py` per data-model.md
- [x] T005 Create `TodoManager` base class and in-memory store (dict) in `src/app/services/todo_manager.py`
- [x] T006 [P] Setup `tests/unit/test_todo_manager.py` with basic fixtures

---

## Phase 3: User Story 1 - Add and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Allow users to add tasks and list them in the console

**Independent Test**: Add a task via `add_task` and verify it appears in `list_tasks` output.

### Implementation for User Story 1

- [x] T007 [P] [US1] Implement `add_task` in `src/app/services/todo_manager.py` with validation
- [x] T008 [P] [US1] Implement `list_tasks` in `src/app/services/todo_manager.py`
- [x] T009 [US1] Add unit tests for `add_task` and `list_tasks` in `tests/unit/test_todo_manager.py`
- [x] T010 [US1] Implement basic list and add commands in `src/app/ui/console_ui.py`
- [x] T011 [US1] Create main CLI loop in `main.py` with routing for 'add' and 'list'

**Checkpoint**: User Story 1 (MVP) is fully functional. Users can record and see tasks.

---

## Phase 4: User Story 2 - Complete and Update Tasks (Priority: P2)

**Goal**: Allow users to mark tasks as done and edit titles

**Independent Test**: Use IDs from User Story 1 to toggle status and edit descriptions, then verify via 'list'.

### Implementation for User Story 2

- [x] T012 [P] [US2] Implement `toggle_task` in `src/app/services/todo_manager.py`
- [x] T013 [P] [US2] Implement `update_task` in `src/app/services/todo_manager.py`
- [x] T014 [US2] Add unit tests for update/toggle in `tests/unit/test_todo_manager.py`
- [x] T015 [US2] Add 'complete' and 'update' commands to `src/app/ui/console_ui.py`
- [x] T016 [US2] Integrate new commands into the CLI loop in `main.py`

**Checkpoint**: Users can now manage the lifecycle of their tasks.

---

## Phase 5: User Story 3 - Delete Tasks (Priority: P3)

**Goal**: Allow users to remove tasks

**Independent Test**: Delete a task by ID and verify it is gone from the list.

### Implementation for User Story 3

- [x] T017 [P] [US3] Implement `delete_task` in `src/app/services/todo_manager.py`
- [x] T018 [US3] Add unit tests for deletion in `tests/unit/test_todo_manager.py`
- [x] T019 [US3] Add 'delete' command to `src/app/ui/console_ui.py`
- [x] T020 [US3] Integrate delete command into the CLI loop in `main.py`

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final cleanup and robust input handling

- [x] T021 [P] Ensure all numeric inputs in `src/app/ui/console_ui.py` handle non-integer input gracefully
- [x] T022 [P] Implement common help menu and welcome message in `src/app/ui/console_ui.py`
- [x] T023 Final manual walkthrough of all User Stories via `main.py`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Phase 1 structure.
- **US1 (Phase 3)**: Depends on Foundational. **MVP Target**.
- **US2/US3 (Phase 4/5)**: Depend on US1 (requires list functionality to verify).

### Parallel Opportunities

- T007 and T008 (US1 logic) can be implemented together.
- T012 and T013 (US2 logic) can be implemented together.
- T021 and T022 (Polish) can be done in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Setup and Foundational.
2. Complete Phase 3 (US1).
3. **Validate**: Run CLI, add "Task A", run "list", see "1. [Pending] Task A".
4. Proceed to US2/US3 once US1 is stable.
