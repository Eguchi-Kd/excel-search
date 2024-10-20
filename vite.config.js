import { defineConfig } from 'vite';

export default defineConfig({
  define: {
    'process.env.VITE_TEST_ID': JSON.stringify(process.env.VITE_TEST_ID)
  }
});
