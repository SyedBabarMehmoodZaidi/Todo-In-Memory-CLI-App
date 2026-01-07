# API Contract: Todo Full-Stack Web Application

## Authentication Endpoints

### Register User
- **Endpoint**: `POST /api/auth/register`
- **Request Body**:
  ```json
  {
    "email": "string (required, valid email format)",
    "password": "string (required, min 8 chars)"
  }
  ```
- **Response**:
  - `201 Created`: User successfully registered
    ```json
    {
      "id": "uuid",
      "email": "string",
      "created_at": "datetime"
    }
    ```
  - `400 Bad Request`: Invalid input or email already exists
  - `422 Unprocessable Entity`: Validation errors

### Login User
- **Endpoint**: `POST /api/auth/login`
- **Request Body**:
  ```json
  {
    "email": "string (required)",
    "password": "string (required)"
  }
  ```
- **Response**:
  - `200 OK`: Login successful
    ```json
    {
      "access_token": "string (JWT)",
      "token_type": "string (bearer)",
      "user": {
        "id": "uuid",
        "email": "string"
      }
    }
    ```
  - `401 Unauthorized`: Invalid credentials

### Get Current User
- **Endpoint**: `GET /api/auth/me`
- **Headers**: `Authorization: Bearer {token}`
- **Response**:
  - `200 OK`: User data retrieved
    ```json
    {
      "id": "uuid",
      "email": "string",
      "created_at": "datetime"
    }
    ```
  - `401 Unauthorized`: Invalid or expired token

## Todo Management Endpoints

### Get User's Todos
- **Endpoint**: `GET /api/todos`
- **Headers**: `Authorization: Bearer {token}`
- **Query Parameters**:
  - `limit`: number (optional, default: 50)
  - `offset`: number (optional, default: 0)
  - `completed`: boolean (optional, filter by completion status)
- **Response**:
  - `200 OK`: List of todos retrieved
    ```json
    {
      "todos": [
        {
          "id": "uuid",
          "title": "string",
          "description": "string (optional)",
          "is_completed": "boolean",
          "priority": "integer (1-3)",
          "created_at": "datetime",
          "updated_at": "datetime",
          "user_id": "uuid"
        }
      ],
      "total": "integer"
    }
    ```

### Create Todo
- **Endpoint**: `POST /api/todos`
- **Headers**: `Authorization: Bearer {token}`
- **Request Body**:
  ```json
  {
    "title": "string (required)",
    "description": "string (optional)",
    "priority": "integer (optional, default: 2, range: 1-3)"
  }
  ```
- **Response**:
  - `201 Created`: Todo created successfully
    ```json
    {
      "id": "uuid",
      "title": "string",
      "description": "string (optional)",
      "is_completed": "boolean (default: false)",
      "priority": "integer (1-3)",
      "created_at": "datetime",
      "updated_at": "datetime",
      "user_id": "uuid"
    }
    ```
  - `400 Bad Request`: Invalid input data

### Get Specific Todo
- **Endpoint**: `GET /api/todos/{id}`
- **Headers**: `Authorization: Bearer {token}`
- **Response**:
  - `200 OK`: Todo retrieved
    ```json
    {
      "id": "uuid",
      "title": "string",
      "description": "string (optional)",
      "is_completed": "boolean",
      "priority": "integer (1-3)",
      "created_at": "datetime",
      "updated_at": "datetime",
      "user_id": "uuid"
    }
    ```
  - `404 Not Found`: Todo not found or doesn't belong to user

### Update Todo
- **Endpoint**: `PUT /api/todos/{id}`
- **Headers**: `Authorization: Bearer {token}`
- **Request Body**:
  ```json
  {
    "title": "string (optional)",
    "description": "string (optional)",
    "is_completed": "boolean (optional)",
    "priority": "integer (optional, range: 1-3)"
  }
  ```
- **Response**:
  - `200 OK`: Todo updated successfully
    ```json
    {
      "id": "uuid",
      "title": "string",
      "description": "string (optional)",
      "is_completed": "boolean",
      "priority": "integer (1-3)",
      "created_at": "datetime",
      "updated_at": "datetime",
      "user_id": "uuid"
    }
    ```

### Toggle Todo Completion
- **Endpoint**: `PATCH /api/todos/{id}/toggle`
- **Headers**: `Authorization: Bearer {token}`
- **Response**:
  - `200 OK`: Todo completion status updated
    ```json
    {
      "id": "uuid",
      "is_completed": "boolean",
      "updated_at": "datetime"
    }
    ```

### Delete Todo
- **Endpoint**: `DELETE /api/todos/{id}`
- **Headers**: `Authorization: Bearer {token}`
- **Response**:
  - `204 No Content`: Todo deleted successfully
  - `404 Not Found`: Todo not found or doesn't belong to user

## Error Response Format
All error responses follow this format:
```json
{
  "detail": "string (error message)"
}
```

## Authentication Requirements
- All `/api/todos/*` endpoints require a valid JWT token in the Authorization header
- The token must be valid and not expired
- Users can only access/modify their own todos