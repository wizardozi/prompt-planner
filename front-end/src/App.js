import React, { useEffect, useState } from 'react';

import ProjectsList from './components/ProjectsList';
import Sidebar from './components/Sidebar';
import Kanban from './components/Kanban';
import './output.css';
import './App.css';

function App() {
  const [selectedProject, setSelectedProject] = useState(null);
  console.log(selectedProject);

  return (
    <div className="flex h-screen overflow-hidden">
      {/* Sidebar - fixed height, sticky left */}
      <div className="shrink-0 h-full sticky top-0 left-0 z-10">
        <Sidebar onSelectProject={setSelectedProject} />
      </div>

      {/* Main content area that can scroll horizontally */}
      <div className="flex-1 h-full overflow-x-auto overflow-y-hidden">
        <div className="flex h-full min-w-max">
          <Kanban project={selectedProject} />
        </div>
      </div>
    </div>
  );
}

export default App;
