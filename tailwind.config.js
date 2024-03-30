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
                '2xs': ['0.7rem', '1rem'],
                '3xs': ['0.6rem', '1rem'],
            },
            height: {
                dvh: ['100vh', '100dvh'],
                svh: ['100vh', '100svh'],
                lvh: ['100vh', '100lvh'],
            },
            width: {
                'screen-9/10': '90vw',
                'screen-4/5': '80vw',
                'screen-3/5': '60vw',
                'screen-3/4': '75vw',
                'screen-1/2': '50vw',
                'screen-1/4': '25vw',
            },
        },
    },
};
