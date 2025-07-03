import React from 'react';

export default function KanbanCard({ task }) {
  const calculateTaskEstimate = (task) => {
    let total = 0;
    if (task.subtasks) {
      task.subtasks.forEach((subtask) => {
        total += parseFloat(subtask.estimate || 0);
      });
    }
    return total.toFixed(2);
  };

  const getPriorityStyle = (priority) => {
    switch (priority) {
      case 'high':
        return 'bg-red-100 text-red-700';
      case 'medium':
        return 'bg-yellow-100 text-yellow-700';
      case 'low':
        return 'bg-green-100 text-green-700';
      default:
        return 'bg-gray-100 text-gray-700';
    }
  };

  const getDaysLeft = (dueDate) => {
    if (!dueDate) return null;
    const now = new Date();
    const due = new Date(dueDate);
    const diffTime = due - now;
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    return diffDays;
  };

  return (
    <div className="bg-white border border-gray-200 rounded-md p-4 shadow-sm mb-4">
      <h3 className="text-sm font-semibold text-gray-800">{task.name}</h3>

      {task.description && (
        <p className="text-xs text-gray-500 mt-1 line-clamp-3">
          {task.description}
        </p>
      )}

      <div className="mt-3 flex flex-wrap gap-2 text-xs">
        {task.priority && (
          <span
            className={`px-2 py-1 rounded ${getPriorityStyle(task.priority)}`}
          >
            {task.priority}
          </span>
        )}

        <span className="bg-blue-100 text-blue-700 px-2 py-1 rounded">
          {calculateTaskEstimate(task)} hrs
        </span>

        {task.due_by && (
          <span className="bg-gray-100 text-gray-500 px-2 py-1 rounded inline-flex items-center gap-1">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="currentColor"
              class="size-4"
            >
              <path
                fill-rule="evenodd"
                d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25ZM12.75 6a.75.75 0 0 0-1.5 0v6c0 .414.336.75.75.75h4.5a.75.75 0 0 0 0-1.5h-3.75V6Z"
                clip-rule="evenodd"
              />
            </svg>
            {getDaysLeft(task.due_by)} days left
          </span>
        )}
      </div>
    </div>
  );
}
