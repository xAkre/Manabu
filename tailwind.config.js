export default {
    darkMode: 'class',
    content: [
        './src/templates/**/*.{jinja,js,html,css}',
        './src/static/**/*.{jina,js,html,css}',
    ],
    theme: {
        extend: {
            fontFamily: {
                megrim: "'megrim', sans-serif",
            },
            fontSize: {
                '2xs': ['10px', '13px'],
                '3xs': ['8px', '10px'],
            },
            height: {
                dvh: ['100vh', '100dvh'],
                svh: ['100vh', '100svh'],
                lvh: ['100vh', '100lvh'],
            },
        },
    },
};
