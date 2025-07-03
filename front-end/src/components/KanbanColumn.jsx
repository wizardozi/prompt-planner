import React from 'react';
import KanbanCard from './KanbanCard';
export default function KanbanColumn({ title, tasks, onSelectTask }) {
  return (
    <div className="w-[300px] flex-shrink-0 p-4 flex flex-col">
      <h2 className="text-lg font-semibold mb-4">{title}</h2>
      <div className="flex flex-col w-[300px] max-h-[calc(100vh-100px)] overflow-y-auto overflow-x-hidden">
        {tasks.map((task) => (
          <div key={task.id} onClick={() => onSelectTask(task)}>
            <KanbanCard task={task} />
          </div>
        ))}
      </div>
    </div>
  );
}
