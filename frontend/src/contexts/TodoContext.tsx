import React, { createContext, useContext, useReducer, ReactNode } from 'react';

interface Todo {
  id: string;
  title: string;
  description?: string;
  is_completed: boolean;
  priority: number; // 1: low, 2: medium, 3: high
  created_at: string;
  updated_at: string;
  user_id: string;
}

interface TodoState {
  todos: Todo[];
  loading: boolean;
  error: string | null;
}

interface TodoAction {
  type: string;
  payload?: any;
}

interface TodoContextType {
  state: TodoState;
  addTodo: (todo: Omit<Todo, 'id' | 'created_at' | 'updated_at' | 'user_id' | 'is_completed'>) => void;
  updateTodo: (id: string, updates: Partial<Todo>) => void;
  deleteTodo: (id: string) => void;
  toggleTodo: (id: string) => void;
  fetchTodos: () => void;
}

const initialState: TodoState = {
  todos: [],
  loading: false,
  error: null,
};

const TodoContext = createContext<TodoContextType | undefined>(undefined);

const todoReducer = (state: TodoState, action: TodoAction): TodoState => {
  switch (action.type) {
    case 'SET_LOADING':
      return { ...state, loading: action.payload };
    case 'SET_ERROR':
      return { ...state, error: action.payload };
    case 'SET_TODOS':
      return { ...state, todos: action.payload, loading: false };
    case 'ADD_TODO':
      return { ...state, todos: [action.payload, ...state.todos] };
    case 'UPDATE_TODO':
      return {
        ...state,
        todos: state.todos.map(todo =>
          todo.id === action.payload.id ? { ...todo, ...action.payload.updates } : todo
        ),
      };
    case 'DELETE_TODO':
      return {
        ...state,
        todos: state.todos.filter(todo => todo.id !== action.payload),
      };
    case 'TOGGLE_TODO':
      return {
        ...state,
        todos: state.todos.map(todo =>
          todo.id === action.payload.id
            ? { ...todo, is_completed: !todo.is_completed }
            : todo
        ),
      };
    default:
      return state;
  }
};

export const TodoProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [state, dispatch] = useReducer(todoReducer, initialState);

  const addTodo = (todoData: Omit<Todo, 'id' | 'created_at' | 'updated_at' | 'user_id' | 'is_completed'>) => {
    // Mock implementation for now
    const newTodo: Todo = {
      id: Math.random().toString(36).substr(2, 9),
      ...todoData,
      is_completed: false,
      created_at: new Date().toISOString(),
      updated_at: new Date().toISOString(),
      user_id: 'current-user-id', // This would come from auth context
    };
    dispatch({ type: 'ADD_TODO', payload: newTodo });
  };

  const updateTodo = (id: string, updates: Partial<Todo>) => {
    dispatch({ type: 'UPDATE_TODO', payload: { id, updates } });
  };

  const deleteTodo = (id: string) => {
    dispatch({ type: 'DELETE_TODO', payload: id });
  };

  const toggleTodo = (id: string) => {
    dispatch({ type: 'TOGGLE_TODO', payload: { id } });
  };

  const fetchTodos = () => {
    // Mock implementation for now
    dispatch({ type: 'SET_LOADING', payload: true });
    dispatch({ type: 'SET_ERROR', payload: null });
    setTimeout(() => {
      dispatch({
        type: 'SET_TODOS',
        payload: [
          {
            id: '1',
            title: 'Sample Todo',
            description: 'This is a sample todo item',
            is_completed: false,
            priority: 2,
            created_at: new Date().toISOString(),
            updated_at: new Date().toISOString(),
            user_id: 'current-user-id',
          }
        ]
      });
    }, 500);
  };

  return (
    <TodoContext.Provider
      value={{
        state,
        addTodo,
        updateTodo,
        deleteTodo,
        toggleTodo,
        fetchTodos,
      }}
    >
      {children}
    </TodoContext.Provider>
  );
};

export const useTodo = () => {
  const context = useContext(TodoContext);
  if (!context) {
    throw new Error('useTodo must be used within a TodoProvider');
  }
  return context;
};