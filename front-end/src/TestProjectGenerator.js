import React, { useState } from 'react';

const TestProjectGenerator = () => {
  const [prompt, setPrompt] = useState('');
  const [project, setProject] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    try {
      setLoading(true);
      const res = await fetch('http://localhost:5000/api/generate/project', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt }),
      });

      if (!res.ok) {
        throw new Error(`Server responded with ${res.status}`);
      }

      const data = await res.json();
      console.log('API Response:', data);
      setProject(data.project);
    } catch (err) {
      console.error('Error generating project:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '20px', maxWidth: '700px', margin: '0 auto' }}>
      <h2>Generate Project</h2>
      <textarea
        rows="3"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Describe your project..."
        style={{ width: '100%', marginBottom: '10px' }}
      />
      <br />
      <button onClick={handleGenerate} disabled={loading}>
        {loading ? 'Generating...' : 'Generate Project'}
      </button>

      {project && (
        <div style={{ marginTop: '30px' }}>
          <h3>{project.name}</h3>
          <p>
            <strong>Description:</strong> {project.description}
          </p>
          <p>
            <strong>Category:</strong> {project.category}
          </p>
          <p>
            <strong>Estimate:</strong> {project.estimate} hours
          </p>

          <h4>Tasks</h4>
          <ul>
            {project.tasks.map((task, tIdx) => (
              <li key={tIdx} style={{ marginBottom: '10px' }}>
                <strong>{task.name}</strong>: {task.description} (
                {task.estimate}h)
                <ul>
                  {task.subtasks.map((subtask, sIdx) => (
                    <li key={sIdx}>
                      {subtask.name} – {subtask.description} ({subtask.estimate}
                      h)
                    </li>
                  ))}
                </ul>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default TestProjectGenerator;
