import { defineConfig } from 'vite';
export default defineConfig({
  define{
    VITE_TEST: JSON.stringify('VITE_TEST:123'),
  },
  //envDir:'../'
});
