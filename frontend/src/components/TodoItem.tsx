import React from 'react';
import { Todo } from '../services/todoService';
import { useTodo } from '../contexts/TodoContext';

interface TodoItemProps {
  todo: Todo;
}

const TodoItem: React.FC<TodoItemProps> = ({ todo }) => {
  const { toggleTodo, deleteTodo } = useTodo();

  const handleToggle = () => {
    toggleTodo(todo.id);
  };

  const handleDelete = () => {
    deleteTodo(todo.id);
  };

  // Priority badge styling
  const getPriorityClass = (priority: number) => {
    switch (priority) {
      case 3:
        return 'bg-red-100 text-red-800';
      case 1:
        return 'bg-green-100 text-green-800';
      case 2:
      default:
        return 'bg-yellow-100 text-yellow-800';
    }
  };

  return (
    <div className="py-4 flex items-start">
      <div className="flex items-center h-5">
        <input
          id={`todo-${todo.id}`}
          type="checkbox"
          checked={todo.is_completed}
          onChange={handleToggle}
          className="h-4 w-4 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500"
        />
      </div>
      <div className="ml-3 flex-1">
        <label htmlFor={`todo-${todo.id}`} className="font-medium text-gray-700">
          <span className={todo.is_completed ? 'line-through text-gray-400' : ''}>
            {todo.title}
          </span>
        </label>
        {todo.description && (
          <p className={`mt-1 text-sm ${todo.is_completed ? 'text-gray-400' : 'text-gray-500'}`}>
            {todo.description}
          </p>
        )}
        <div className="mt-2 flex items-center">
          <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${getPriorityClass(todo.priority)}`}>
            {todo.priority === 1 ? 'Low' : todo.priority === 2 ? 'Medium' : 'High'} Priority
          </span>
          <span className="ml-2 text-xs text-gray-500">
            {new Date(todo.created_at).toLocaleDateString()}
          </span>
        </div>
      </div>
      <div className="ml-4 flex-shrink-0">
        <button
          onClick={handleDelete}
          className="inline-flex items-center px-3 py-1 border border-transparent text-sm leading-4 font-medium rounded-md text-red-700 bg-red-100 hover:bg-red-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
        >
          Delete
        </button>
      </div>
    </div>
  );
};

export default TodoItem;