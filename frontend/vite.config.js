import { defineConfig } from 'vite';
const path = require('path');
import react from '@vitejs/plugin-react';

export default defineConfig({
    root: path.join(__dirname, 'src'),
    build: {
        outDir: path.join(__dirname, '../dist'),
        emptyOutDir: true,
        sourcemap: true
    },
    css: {
        preprocessorOptions: {
            scss: {
            silenceDeprecations: [
                'import',
                'mixed-decls',
                'color-functions',
                'global-builtin',
                ],
            },
        },
    },
    plugins: [react()]
});