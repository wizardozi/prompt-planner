import PingTest from './PingTest';
import ProjectsList from './ProjectsList';
import Sidebar from './Sidebar';

function App() {
  return (
    <div>
      <h1>Prompt Planner UI</h1>
      <Sidebar />
      <PingTest />
      <ProjectsList />
    </div>
  );
}

export default App;
