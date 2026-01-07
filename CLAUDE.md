# Todo-In-Memory-CLI-App Development Guidelines

Phase II: Todo Full-Stack Web Application. Last updated: 2026-01-07

## Project Phases

### Phase I (Completed)
- Console-based Todo application with in-memory storage
- Basic CRUD operations for tasks
- Local persistent storage (JSON/SQLite)

### Phase II (Active)
- Multi-user web application with persistent storage
- RESTful API backend
- Responsive frontend interface
- JWT-based authentication

## Active Technologies

### Frontend Layer
- **Framework**: Next.js 16+ (App Router)
- **Language**: TypeScript 5+
- **Styling**: Tailwind CSS / CSS Modules
- **State Management**: React Context / Custom hooks
- **Validation**: Client-side form validation

### Backend Layer
- **Framework**: FastAPI (Python 3.11+)
- **Language**: Python 3.11+
- **ORM**: SQLModel (SQLAlchemy + Pydantic)
- **Package Manager**: UV
- **Testing**: Pytest

### Database Layer
- **Database**: Neon Serverless PostgreSQL
- **Connection Pooling**: Neon built-in pooling
- **Migrations**: Alembic

### Authentication & Security
- **Auth Provider**: Better Auth
- **Token Type**: JWT (JSON Web Tokens)
- **Token Storage**: Secure HTTP-only cookies (frontend)
- **Authorization**: Bearer token in Authorization header
- **Token Verification**: Shared secret key between frontend and backend

## Development Approach

**Agentic Development Stack Workflow**:
1. **Specify**: Write feature specifications using Spec-Kit Plus
2. **Plan**: Generate implementation plans using Claude Code
3. **Break into Tasks**: Decompose plans into actionable tasks
4. **Implement**: Execute tasks via Claude Code agents (no manual coding)

## Project Structure

```text
backend/
├── src/
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth/           # Authentication endpoints
│   │   │   ├── tasks/          # Task CRUD endpoints
│   │   │   └── users/          # User endpoints
│   │   ├── models/             # SQLModel database models
│   │   ├── schemas/            # Pydantic request/response schemas
│   │   ├── services/           # Business logic
│   │   ├── middleware/         # JWT verification middleware
│   │   ├── database.py         # Database configuration
│   │   └── main.py             # FastAPI app initialization
│   └── config.py               # Configuration settings
├── tests/
│   ├── unit/                   # Unit tests
│   ├── integration/            # Integration tests
│   └── conftest.py             # Pytest fixtures
├── requirements.txt            # Python dependencies
└── pyproject.toml              # Project metadata

frontend/
├── src/
│   ├── app/
│   │   ├── (auth)/             # Authentication pages
│   │   │   ├── signup/page.tsx
│   │   │   ├── signin/page.tsx
│   │   │   └── layout.tsx
│   │   ├── (dashboard)/        # Dashboard pages
│   │   │   ├── tasks/page.tsx
│   │   │   ├── layout.tsx
│   │   │   └── error.tsx
│   │   └── layout.tsx          # Root layout
│   ├── components/
│   │   ├── auth/               # Auth components
│   │   ├── tasks/              # Task components
│   │   └── common/             # Shared components
│   ├── lib/
│   │   ├── api-client.ts       # API client with Bearer token
│   │   ├── auth.ts             # Better Auth integration
│   │   └── utils.ts            # Utility functions
│   └── styles/                 # Global styles
├── .env.local                  # Environment variables
└── package.json                # Dependencies
```

## Commands

### Backend
- `uv run main.py`: Start FastAPI development server
- `uv run pytest`: Run unit tests
- `uv add [dependency]`: Add new dependencies
- `alembic upgrade head`: Run database migrations

### Frontend
- `npm run dev`: Start Next.js development server
- `npm test`: Run frontend tests
- `npm run build`: Build for production

## Code Style

### Backend (Python)
- Follow PEP 8 guidelines
- Use type hints for all function signatures and variable declarations
- Use SQLModel for database models (combines SQLAlchemy + Pydantic)
- Implement robust input validation (Pydantic schemas)
- Use dependency injection for services and database connections
- Implement proper error handling with FastAPI exceptions

### Frontend (TypeScript)
- Use TypeScript for type safety
- Follow React hooks and functional component patterns
- Use Server Components where appropriate (Next.js App Router)
- Implement proper error boundaries and error handling
- Use semantic HTML and ARIA labels for accessibility
- Implement proper loading and error states

## Authentication Flow

1. **User Registration**: Frontend sends email/password → Better Auth creates user → Issues JWT
2. **User Login**: Frontend sends credentials → Better Auth validates → Issues JWT token
3. **API Requests**: Frontend includes token in `Authorization: Bearer <token>` header
4. **Token Verification**: FastAPI middleware extracts and verifies token
5. **User Isolation**: Backend filters data by decoded user ID from token
6. **Token Refresh**: Better Auth handles automatic token refresh

## Agentic Roles

| Role | Responsibility | Agent Type |
|------|-----------------|-----------|
| **Auth Agent** | Implement signup/signin, JWT handling, Better Auth integration | auth-implementation-reviewer |
| **Backend Agent** | Create FastAPI routes, database queries, business logic | fastapi-backend-architect |
| **Database Agent** | Design schemas, migrations, PostgreSQL optimization | db-neon-manager |
| **Frontend Agent** | Build Next.js components, layouts, responsive UI | nextjs-todo-frontend |

## Recent Changes
- **001-todo-fullstack-webapp** (Phase II): Defined full-stack architecture with FastAPI backend, Next.js frontend, Neon PostgreSQL, Better Auth JWT authentication, and agentic development workflow
- **001-todo-cli-phase1** (Phase I): Initial console app with in-memory storage and layered design

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
