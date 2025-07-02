import React, { useEffect, useState } from 'react';

function ProjectsList() {
  const [projects, setProjects] = useState([]);

  const calculateProjectEstimate = (project) => {
    let total = 0;
    if (project.tasks) {
      project.tasks.forEach((task) => {
        if (task.subtasks) {
          task.subtasks.forEach((subtask) => {
            total += parseFloat(subtask.estimate || 0);
          });
        }
      });
    }
    return total.toFixed(2);
  };

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/projects')
      .then((res) => res.json())
      .then((data) => setProjects(data))
      .catch((err) => console.error('Error loading projects:', err));
  }, []);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h2 style={{ color: '#333' }}>Projects</h2>
      {projects.length === 0 ? (
        <p style={{ color: '#888' }}>No projects found.</p>
      ) : (
        <ul style={{ listStyleType: 'none', paddingLeft: 0 }}>
          {projects.map((project) => (
            <li key={project.id} style={{ marginBottom: '2rem' }}>
              <strong style={{ color: '#007acc' }}>{project.name}</strong>
              <p style={{ color: '#444' }}>{project.description}</p>
              <p style={{ color: '#5c5c5c', fontStyle: 'italic' }}>
                {project.category}
              </p>
              <p style={{ color: '#555' }}>
                <strong>Total Estimate:</strong>{' '}
                {calculateProjectEstimate(project)} hrs
              </p>

              {project.tasks && (
                <ul style={{ paddingLeft: '1rem' }}>
                  {project.tasks.map((task) => (
                    <li key={task.id} style={{ marginTop: '1rem' }}>
                      <strong style={{ color: '#d97706' }}>{task.name}</strong>
                      <p style={{ color: '#444' }}>{task.description}</p>
                      <p>
                        <span style={{ color: '#999' }}>Due:</span>{' '}
                        {task.due_by}
                      </p>
                      <p>
                        <span style={{ color: '#999' }}>Priority:</span>{' '}
                        {task.priority}
                      </p>
                      <p>
                        <span style={{ color: '#999' }}>Status:</span>{' '}
                        {task.status}
                      </p>

                      {task.subtasks && (
                        <ul style={{ paddingLeft: '1rem' }}>
                          {task.subtasks.map((subtask, index) => (
                            <li key={index}>
                              <strong style={{ color: '#10b981' }}>
                                {subtask.name}
                              </strong>
                              <p style={{ color: '#444' }}>
                                {subtask.description}
                              </p>
                              <p>
                                <span style={{ color: '#999' }}>Estimate:</span>{' '}
                                {subtask.estimate} hrs
                              </p>
                              <p>
                                <span style={{ color: '#999' }}>Status:</span>{' '}
                                {subtask.status}
                              </p>
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
