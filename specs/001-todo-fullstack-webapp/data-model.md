# Data Model: Todo Full-Stack Web Application

## Entity: User
**Description**: Represents a registered user of the application

**Fields**:
- `id`: UUID (Primary Key) - Unique identifier for the user
- `email`: String (Unique, Indexed) - User's email address for login
- `hashed_password`: String - Securely hashed password
- `created_at`: DateTime - Timestamp of account creation
- `updated_at`: DateTime - Timestamp of last update
- `is_active`: Boolean - Account status flag

**Relationships**:
- One-to-Many: User has many Todo items (via user_id foreign key)

**Validation Rules**:
- Email must be valid email format
- Email must be unique across all users
- Password must meet security requirements (minimum length, complexity)

## Entity: Todo
**Description**: Represents a user's task/todo item

**Fields**:
- `id`: UUID (Primary Key) - Unique identifier for the todo
- `title`: String (Required) - Title of the todo item
- `description`: String (Optional) - Detailed description of the todo
- `is_completed`: Boolean - Completion status (default: false)
- `priority`: Integer (Enum: 1-3, default: 2) - Priority level (1: low, 2: medium, 3: high)
- `created_at`: DateTime - Timestamp of creation
- `updated_at`: DateTime - Timestamp of last update
- `user_id`: UUID (Foreign Key) - Reference to the owning user

**Relationships**:
- Many-to-One: Todo belongs to one User (via user_id foreign key)

**Validation Rules**:
- Title must not be empty
- Priority must be between 1 and 3
- User_id must reference an existing active user
- Only the owner can modify/delete the todo

## State Transitions

### Todo State Transitions:
- **Created**: When a new todo is added by a user
- **Updated**: When any field except completion status is modified
- **Completed**: When the is_completed field is set to true
- **Reopened**: When the is_completed field is set to false
- **Deleted**: When the todo is permanently removed

### User State Transitions:
- **Registered**: When a new user account is created
- **Activated**: When email is verified (if verification required)
- **Deactivated**: When account is disabled
- **Deleted**: When account is permanently removed

## Indexes
- User.email: Unique index for fast login lookups
- Todo.user_id: Index for efficient user-specific queries
- Todo.created_at: Index for chronological sorting
- Todo.is_completed: Index for filtering by completion status