import { defineConfig } from 'motia';

export default defineConfig({
  stepsDir: './src/Steps',

  python: {
    executable: 'python'
    
  },

  logging: {
    level: 'info'
  }
});
