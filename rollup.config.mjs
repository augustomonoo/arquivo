import typescript from '@rollup/plugin-typescript';
export default {
    input: 'arquivo/frontend_src/main.ts',
    output: {
        file: 'arquivo/static/arquivo/bundle.js',
        format: 'cjs'
    },
    plugins: [typescript()]
};