// 👇 ADD THIS LINE FIRST
require('electron-reload')(__dirname, {
  electron: require(`${__dirname}/node_modules/electron`),
});

const { app, BrowserWindow } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let pyProc = null;

function createWindow() {
  const win = new BrowserWindow({
    width: 1000,
    height: 800,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
    },
  });

  win.loadURL('http://localhost:3000');
  mainWindow.webContents.openDevTools({ mode: 'detach' });
}

function startPythonBackend() {
  const script = path.join(__dirname, '../back-end/server.py');
  pyProc = spawn('python3', [script]);

  pyProc.stdout.on('data', (data) => {
    console.log(`Python: ${data}`);
  });
  pyProc.stderr.on('data', (data) => {
    console.error(`Python error: ${data}`);
  });
}

app.whenReady().then(() => {
  startPythonBackend();
  createWindow();
});

app.on('will-quit', () => {
  if (pyProc) pyProc.kill();
});
