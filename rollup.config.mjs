import typescript from '@rollup/plugin-typescript';
import { nodeResolve } from '@rollup/plugin-node-resolve';
export default {
    input: 'arquivo/frontend_src/main.ts',
    output: {
        file: 'arquivo/static/arquivo/bundle.js',
        format: 'cjs'
    },
    plugins: [typescript(), nodeResolve()]
};