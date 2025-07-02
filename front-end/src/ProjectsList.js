import React, { useEffect, useState } from 'react';

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
        <ul>
          {projects.map((project) => (
            <li key={project.id}>
              <strong>{project.name}</strong>
              <p>{project.description}</p>
              <p>{project.category}</p>
              {project.tasks && (
                <ul>
                  {project.tasks.map((task) => (
                    <li key={task.id}>
                      <strong>{task.name}</strong>
                      <p>{task.description}</p>
                      <p>Due: {task.due_by}</p>
                      <p>Priority: {task.priority}</p>
                      <p>Status: {task.status}</p>
                      {task.subtasks && (
                        <ul>
                          {task.subtasks?.map((subtask, index) => (
                            <li key={index}>
                              <strong>{subtask.name}</strong>
                              <p>{subtask.description}</p>
                              <p>Estimate: {subtask.estimate} hrs</p>
                              <p>Status: {subtask.status}</p>
                            </li>
                          ))}
                        </ul>
                      )}
                    </li>
                  ))}
                </ul>
              )}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default ProjectsList;
