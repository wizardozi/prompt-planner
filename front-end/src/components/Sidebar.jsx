import React, { useEffect, useState } from 'react';
function taskCount(tasks) {
  let count = 0;
  for (let i = 0; i < tasks.length; i++) {
    count++;
  }
  return count;
}
function ProjectsList() {
  const [projects, setProjects] = useState([]);
  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/projects')
      .then((res) => res.json())
      .then((data) => setProjects(data))
      .catch((err) => console.error('Error loading projects:', err));
  }, []);

  return (
    <div>
      <h2>Projects</h2>
      {projects.length === 0 ? (
        <p>No projects found.</p>
      ) : (
        <div>
          {projects.map((project) => (
            <div key={project.id} style={{ marginBottom: '8px' }}>
              <strong>{project.name}</strong>
              <p>Tasks: {taskCount(project.tasks)}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default ProjectsList;
