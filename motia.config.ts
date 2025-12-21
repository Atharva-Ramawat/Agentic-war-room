import { defineConfig } from 'motia';

export default defineConfig({
  stepsDir: './src/Steps',

  python: {
    executable: 'python'
    // Windows:
    // executable: '../venv/Scripts/python.exe'
    // macOS/Linux:
    // executable: '../venv/bin/python'
  },

  logging: {
    level: 'info'
  }
});
