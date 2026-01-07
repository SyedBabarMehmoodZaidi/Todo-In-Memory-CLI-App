# Quickstart Guide: Todo Full-Stack Web Application

## Prerequisites
- Node.js 18+ and npm/yarn
- Python 3.11+
- PostgreSQL (or access to Neon Serverless PostgreSQL)
- Git

## Environment Setup

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install fastapi uvicorn sqlmodel python-multipart python-jose[cryptography] passlib[bcrypt] better-exceptions
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your database connection string and JWT secret
   ```

5. Run database migrations:
   ```bash
   # This will be implemented in the backend setup
   ```

6. Start the backend server:
   ```bash
   uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your backend API URL
   ```

4. Start the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login and get JWT token
- `POST /api/auth/logout` - Logout (client-side token removal)
- `GET /api/auth/me` - Get current user info (requires JWT)

### Todo Management
- `GET /api/todos` - Get user's todos (requires JWT)
- `POST /api/todos` - Create a new todo (requires JWT)
- `GET /api/todos/{id}` - Get a specific todo (requires JWT)
- `PUT /api/todos/{id}` - Update a specific todo (requires JWT)
- `DELETE /api/todos/{id}` - Delete a specific todo (requires JWT)
- `PATCH /api/todos/{id}/toggle` - Toggle completion status (requires JWT)

## Development Workflow

1. **Backend Development**: Run the backend server with `--reload` flag for hot reloading
2. **Frontend Development**: Use Next.js development server for hot reloading
3. **Database Changes**: Update SQLModel models and run migrations
4. **Testing**: Run backend tests with pytest and frontend tests with Jest

## Testing

### Backend Tests
```bash
cd backend
python -m pytest tests/
```

### Frontend Tests
```bash
cd frontend
npm test
# or
yarn test
```