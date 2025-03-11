import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  server: {
    host: true,
    port: 4242,
    watch: {
      usePolling: true, // Enable polling
      interval: 1000, // Poll every 1000 milliseconds (1 second)
      ignored: ['**/node_modules/**'], // Ignore node_modules directory
    }
  }
})
