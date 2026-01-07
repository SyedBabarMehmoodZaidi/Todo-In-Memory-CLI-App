import React, { useEffect } from 'react';
import { useTodo } from '../contexts/TodoContext';
import TodoList from '../components/TodoList';
import TodoForm from '../components/TodoForm';

const DashboardPage: React.FC = () => {
  const { state, fetchTodos } = useTodo();

  useEffect(() => {
    fetchTodos();
  }, []);

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="text-center mb-8">
          <h1 className="text-2xl sm:text-3xl font-bold text-gray-900">Todo Dashboard</h1>
          <p className="mt-2 text-gray-600">Manage your tasks efficiently</p>
        </div>

        <div className="bg-white shadow rounded-lg p-4 sm:p-6">
          <TodoForm />
          <TodoList todos={state.todos} loading={state.loading} />
        </div>
      </div>
    </div>
  );
};

export default DashboardPage;