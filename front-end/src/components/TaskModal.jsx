// src/components/TaskModal.jsx

import React from 'react';

const TaskModal = ({ task, onClose }) => {
  if (!task) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg shadow-lg w-full max-w-lg p-6 relative">
        <button
          onClick={onClose}
          className="absolute top-2 right-2 text-gray-500 hover:text-gray-700 text-xl font-bold"
        >
          &times;
        </button>
        <h2 className="text-2xl font-semibold mb-2">{task.name}</h2>
        <p className="text-sm text-gray-600 mb-4">{task.description}</p>
        <div className="mb-4">
          <strong>Status:</strong> {task.status} <br />
          <strong>Estimate:</strong> {task.estimate} hours <br />
          <strong>Due by:</strong> {task.due_by}
        </div>
        <div>
          <h3 className="font-medium mb-2">Subtasks</h3>
          <ul className="list-disc list-inside space-y-1">
            {task.subtasks &&
              task.subtasks.map((subtask) => (
                <div key={subtask.id}>
                  <p>
                    {subtask.name} — {subtask.estimate ?? '?'}h
                  </p>
                  <li>{subtask.description}</li>
                </div>
              ))}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default TaskModal;
