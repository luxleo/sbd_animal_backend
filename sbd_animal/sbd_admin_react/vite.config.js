import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
	root: './src',
	server: {
		port: 5173,
	},
	build: {
		manifest: true,
		rollupOptions: {
			input: './src/main.jsx',
		},
		outDir: '../../dist',
	},
	plugins: [react()],
	envDir: './Myenv',
});
