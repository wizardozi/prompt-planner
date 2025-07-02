import ProjectsList from './components/ProjectsList';
import Sidebar from './components/Sidebar';
import TestProjectGenerator from './TestProjectGenerator';

function App() {
  return (
    <div>
      <h1>Prompt Planner UI</h1>
      <Sidebar />
      <ProjectsList />
      {/* <TestProjectGenerator /> */}
    </div>
  );
}

export default App;
