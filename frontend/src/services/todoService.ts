import axios from 'axios';

// Get base API URL from environment
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

// Create axios instance with defaults
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add request interceptor to include auth token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Add response interceptor to handle errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token might be expired, redirect to login
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

interface TodoCreateData {
  title: string;
  description?: string;
  priority?: number;
}

interface TodoUpdateData {
  title?: string;
  description?: string;
  is_completed?: boolean;
  priority?: number;
}

export interface Todo {
  id: string;
  title: string;
  description?: string;
  is_completed: boolean;
  priority: number;
  created_at: string;
  updated_at: string;
  user_id: string;
}

export const todoService = {
  // Get all todos for the authenticated user
  getTodos: async (completed?: boolean): Promise<Todo[]> => {
    const params = completed !== undefined ? { completed } : {};
    const response = await api.get('/api/todos', { params });
    return response.data;
  },

  // Create a new todo
  createTodo: async (todoData: TodoCreateData): Promise<Todo> => {
    const response = await api.post('/api/todos', todoData);
    return response.data;
  },

  // Get a specific todo by ID
  getTodo: async (id: string): Promise<Todo> => {
    const response = await api.get(`/api/todos/${id}`);
    return response.data;
  },

  // Update a todo
  updateTodo: async (id: string, todoData: TodoUpdateData): Promise<Todo> => {
    const response = await api.put(`/api/todos/${id}`, todoData);
    return response.data;
  },

  // Toggle todo completion status
  toggleTodo: async (id: string): Promise<Todo> => {
    const response = await api.patch(`/api/todos/${id}/toggle`);
    return response.data;
  },

  // Delete a todo
  deleteTodo: async (id: string): Promise<void> => {
    await api.delete(`/api/todos/${id}`);
  },
};