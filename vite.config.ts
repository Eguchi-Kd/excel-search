import { defineConfig } from 'vite';

export default defineConfig(({ command, mode }) => {
  const env = loadEnv(mode, process.cwd(), '');
  return {
    define: {
      VITE_TEST_ID: JSON.stringify(env.VITE_TEST_ID),
    },
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./', import.meta.url))
      }
    }
  }
});
