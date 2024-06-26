/**
 * Load the user's preferred theme
 *
 * @returns void
 */
const initTheme = () => {
    let prefersDarkScheme = localStorage.getItem('prefers-dark-scheme');

    if (prefersDarkScheme === 'true') {
        return document.documentElement.classList.add('dark');
    } else if (prefersDarkScheme === 'false') {
        return document.documentElement.classList.remove('dark');
    }

    prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');

    if (prefersDarkScheme.matches) {
        document.documentElement.classList.add('dark');
    }
};

/**
 * Set the current theme
 *
 * @returns void
 */
const setTheme = (theme) => {
    if (theme === 'light') {
        localStorage.setItem('prefers-dark-scheme', 'false');
        return document.documentElement.classList.remove('dark');
    }

    localStorage.setItem('prefers-dark-scheme', 'true');
    document.documentElement.classList.add('dark');
};

/**
 * Switch the current theme
 *
 * @returns void
 */
const switchTheme = () => {
    const prefersDarkScheme = localStorage.getItem('prefers-dark-scheme');

    if (prefersDarkScheme === 'true') {
        return setTheme('light');
    } else if (prefersDarkScheme === 'false') {
        return setTheme('dark');
    }

    setTheme('light');
};

export { initTheme, setTheme, switchTheme };
