// src/components/Sidebar.jsx
import React, { useEffect, useState, useRef } from 'react';
const [minWidth, maxWidth, defaultWidth] = [100, 500, 200];

function Sidebar({ onSelectProject }) {
  const [projects, setProjects] = useState([]);
  const [isProjectsOpen, setIsProjectsOpen] = useState(false);
  const [width, setWidth] = useState(
    parseInt(localStorage.getItem('sidebarWidth')) || defaultWidth
  );
  const isResized = useRef(false);

  useEffect(() => {
    localStorage.setItem('sidebarWidth', width);
  }, [width]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/projects')
      .then((res) => res.json())
      .then((data) => setProjects(data))
      .catch((err) => console.error('Error loading projects:', err));
  }, []);

  useEffect(() => {
    window.addEventListener('mousemove', (e) => {
      if (!isResized.current) {
        return;
      }

      setWidth((previousWidth) => {
        const newWidth = previousWidth + e.movementX / 2;

        const isWidthInRange = newWidth >= minWidth && newWidth <= maxWidth;

        return isWidthInRange ? newWidth : previousWidth;
      });
    });

    window.addEventListener('mouseup', () => {
      isResized.current = false;
    });
  }, []);

  return (
    <div className="flex h-screen overflow-hidden">
      <div
        style={{ width: `${width / 16}rem` }}
        className="flex flex-col bg-gray-800 text-white"
      >
        <aside
          id="default-sidebar"
          className="flex flex-col flex-1 overflow-y-auto"
          aria-label="Sidebar"
        >
          <ul className="space-y-2 font-medium">
            <li>
              <a
                href="#"
                className="flex items-center p-2 rounded-lg text-white hover:bg-gray-700 group"
              >
                {/* Dashboard Icon */}
                <svg
                  className="w-5 h-5 text-gray-400 group-hover:text-white"
                  fill="currentColor"
                  viewBox="0 0 22 21"
                >
                  <path d="M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z" />
                  <path d="M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z" />
                </svg>
                <span className="ml-3">Dashboard</span>
              </a>
            </li>

            <li>
              <a
                href="#"
                className="flex items-center p-2 rounded-lg text-white hover:bg-gray-700 group"
              >
                {/* Kanban Icon */}
                <svg
                  className="w-5 h-5 text-gray-400 group-hover:text-white"
                  fill="currentColor"
                  viewBox="0 0 18 18"
                >
                  <path d="M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10Zm10 0h-4.286A1.857 1.857 0 0 0 10 11.857v4.286c0 1.026.831 1.857 1.857 1.857h4.286A1.857 1.857 0 0 0 18 16.143v-4.286A1.857 1.857 0 0 0 16.143 10Z" />
                </svg>
                <span className="ml-3">Kanban</span>
              </a>
            </li>

            <li>
              <button
                type="button"
                onClick={() => setIsProjectsOpen((prev) => !prev)}
                className="flex items-center w-full p-2 rounded-lg text-white hover:bg-gray-700 group"
              >
                {/* Projects Icon */}
                <svg
                  className="w-6 h-6 text-gray-400 group-hover:text-white"
                  fill="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path d="M5.566 4.657A4.505 4.505 0 0 1 6.75 4.5h10.5c.41 0 .806.055 1.183.157A3 3 0 0 0 15.75 3h-7.5a3 3 0 0 0-2.684 1.657ZM2.25 12a3 3 0 0 1 3-3h13.5a3 3 0 0 1 3 3v6a3 3 0 0 1-3 3H5.25a3 3 0 0 1-3-3v-6ZM5.25 7.5c-.41 0-.806.055-1.184.157A3 3 0 0 1 6.75 6h10.5a3 3 0 0 1 2.683 1.657A4.505 4.505 0 0 0 18.75 7.5H5.25Z" />
                </svg>
                <span className="ml-3 text-left">Projects</span>
                <svg className="w-3 h-3 ml-auto" fill="none" viewBox="0 0 10 6">
                  <path
                    d="m1 1 4 4 4-4"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  />
                </svg>
              </button>

              <ul
                className={`${
                  isProjectsOpen ? '' : 'hidden'
                } py-2 pl-4 space-y-1`}
              >
                {projects.map((project) => (
                  <li key={project.id}>
                    <a
                      href="#"
                      onClick={() => onSelectProject(project)}
                      className="block p-2 rounded hover:bg-gray-700"
                    >
                      {project.name}
                    </a>
                  </li>
                ))}
              </ul>
            </li>
          </ul>
        </aside>
      </div>

      {/* Resize Handle */}
      <div
        className="w-1 cursor-col-resize bg-gray-700 hover:bg-blue-500"
        onMouseDown={() => {
          isResized.current = true;
        }}
      />
    </div>
  );
}

export default Sidebar;
