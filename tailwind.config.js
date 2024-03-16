export default {
    darkMode: 'class',
    content: [
        './src/templates/**/*.{jinja,js,html}',
        './src/static/**/*.{jinja,js,html}',
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
            width: {
                'screen-3/4': '75vw',
                'screen-1/2': '50vw',
                'screen-1/4': '25vw',
            },
        },
    },
};
