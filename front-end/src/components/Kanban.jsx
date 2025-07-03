import React, { useEffect, useState } from 'react';
import TaskModal from './TaskModal';
import KanbanColumn from './KanbanColumn';

const columns = [
  { id: 'to-do', title: 'To Do' },
  { id: 'in-progress', title: 'In Progress' },
  { id: 'done', title: 'Done' },
  { id: 'incomplete', title: 'Incomplete' },
];

export default function Kanban({ project }) {
  const [selectedTask, setSelectedTask] = useState(null);

  return (
    <div>
      <h1 className="text-xl font-bold">
        {project?.name || 'No Project Selected'}
      </h1>
      <div className="flex gap-4 p-4 overflow-x-auto h-full bg-gray-100">
        {columns.map((col) => (
          <KanbanColumn
            key={col.id}
            title={col.title}
            tasks={(project?.tasks || []).filter(
              (task) => task.status && task.status.toLowerCase() === col.id
            )}
            onSelectTask={setSelectedTask} // ✅ Pass the function to the column
          />
        ))}
      </div>

      {/* ✅ Conditionally show TaskModal */}
      {selectedTask && (
        <TaskModal task={selectedTask} onClose={() => setSelectedTask(null)} />
      )}
    </div>
  );
}
