import React, { createContext, useContext, useReducer, ReactNode } from 'react';

interface User {
  id: string;
  email: string;
  created_at: string;
}

interface AuthState {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  loading: boolean;
}

interface AuthAction {
  type: string;
  payload?: any;
}

interface AuthContextType {
  state: AuthState;
  login: (token: string, user: User) => void;
  logout: () => void;
  register: (email: string, password: string) => Promise<void>;
}

const initialState: AuthState = {
  user: null,
  token: null,
  isAuthenticated: false,
  loading: true,
};

const AuthContext = createContext<AuthContextType | undefined>(undefined);

const authReducer = (state: AuthState, action: AuthAction): AuthState => {
  switch (action.type) {
    case 'LOGIN':
      return {
        ...state,
        user: action.payload.user,
        token: action.payload.token,
        isAuthenticated: true,
        loading: false,
      };
    case 'LOGOUT':
      return {
        ...state,
        user: null,
        token: null,
        isAuthenticated: false,
        loading: false,
      };
    case 'SET_LOADING':
      return {
        ...state,
        loading: action.payload,
      };
    default:
      return state;
  }
};

export const AuthProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [state, dispatch] = useReducer(authReducer, initialState);

  const login = (token: string, user: User) => {
    // Store token in localStorage for persistence across sessions
    localStorage.setItem('token', token);
    dispatch({ type: 'LOGIN', payload: { token, user } });
  };

  const logout = () => {
    // Remove token from localStorage
    localStorage.removeItem('token');
    // Remove any other stored user data
    localStorage.removeItem('user');
    dispatch({ type: 'LOGOUT' });
  };

  // Function to check if token is expired
  const isTokenExpired = (token: string): boolean => {
    try {
      const payload = JSON.parse(atob(token.split('.')[1]));
      const currentTime = Math.floor(Date.now() / 1000);
      return payload.exp < currentTime;
    } catch (e) {
      return true; // If we can't parse the token, consider it expired
    }
  };

  // Function to get token with expiration check
  const getToken = (): string | null => {
    const token = localStorage.getItem('token');
    if (token && isTokenExpired(token)) {
      logout(); // Automatically logout if token is expired
      return null;
    }
    return token;
  };

  const register = async (email: string, password: string) => {
    // Implementation will be added later
    console.log('Register function called with:', { email, password });
  };

  return (
    <AuthContext.Provider value={{ state, login, logout, register }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};