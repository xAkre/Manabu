/**
 * Base class for application icons
 */
class Icon {
    /**
     * The icon's content as a string
     *
     * @type {string}
     */
    static svgString;

    /**
     * Create a new icon
     * @param {string} [className="h-10 w-10 text-slate-800 dark:text-slate-100"] - The class name to add to the svg element
     */
    constructor(className = 'h-10 w-10 text-slate-800 dark:text-slate-100') {
        const container = document.createElement('div');
        container.innerHTML = this.constructor.svgString;
        this.svgElement = container.querySelector('svg');
        this.svgElement.setAttribute('class', className);
    }
}

/**
 * Represents an identification icon
 */
class Identification extends Icon {
    static svgString =
        '<svg\n' +
        '    xmlns="http://www.w3.org/2000/svg"\n' +
        '    fill="none"\n' +
        '    viewBox="0 0 24 24"\n' +
        '    stroke-width="1.5"\n' +
        '    stroke="currentColor"\n' +
        '>\n' +
        '    <path\n' +
        '        stroke-linecap="round"\n' +
        '        stroke-linejoin="round"\n' +
        '        d="M15 9h3.75M15 12h3.75M15 15h3.75M4.5 19.5h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Zm6-10.125a1.875 1.875 0 1 1-3.75 0 1.875 1.875 0 0 1 3.75 0Zm1.294 6.336a6.721 6.721 0 0 1-3.17.789 6.721 6.721 0 0 1-3.168-.789 3.376 3.376 0 0 1 6.338 0Z"\n' +
        '    />\n' +
        '</svg>\n';
}

/**
 * Represents a lock icon
 */
class Lock extends Icon {
    static svgString =
        '<svg\n' +
        '    xmlns="http://www.w3.org/2000/svg"\n' +
        '    fill="none"\n' +
        '    viewBox="0 0 24 24"\n' +
        '    stroke-width="1.5"\n' +
        '    stroke="currentColor"\n' +
        '>\n' +
        '    <path\n' +
        '        stroke-linecap="round"\n' +
        '        stroke-linejoin="round"\n' +
        '        d="M16.5 10.5V6.75a4.5 4.5 0 1 0-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 0 0 2.25-2.25v-6.75a2.25 2.25 0 0 0-2.25-2.25H6.75a2.25 2.25 0 0 0-2.25 2.25v6.75a2.25 2.25 0 0 0 2.25 2.25Z"\n' +
        '    />\n' +
        '</svg>';
}

/**
 * Represents a tick icon
 */
class Tick extends Icon {
    static svgString =
        '<svg\n' +
        '    xmlns="http://www.w3.org/2000/svg"\n' +
        '    fill="none"\n' +
        '    viewBox="0 0 24 24"\n' +
        '    stroke-width="1.5"\n' +
        '    stroke="currentColor"\n' +
        '>\n' +
        '    <path\n' +
        '        stroke-linecap="round"\n' +
        '        stroke-linejoin="round"\n' +
        '        d="M9 12.75 11.25 15 15 9.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"\n' +
        '    />\n' +
        '</svg>';
}

/**
 * Represents an x mark icon
 */
class XMark extends Icon {
    static svgString =
        '<svg\n' +
        '    xmlns="http://www.w3.org/2000/svg"\n' +
        '    fill="none"\n' +
        '    viewBox="0 0 24 24"\n' +
        '    stroke-width="1.5"\n' +
        '    stroke="currentColor"\n' +
        '>\n' +
        '    <path\n' +
        '        stroke-linecap="round"\n' +
        '        stroke-linejoin="round"\n' +
        '        d="M6 18 18 6M6 6l12 12"\n' +
        '    />\n' +
        '</svg>\n';
}

/**
 * Represents an x circle icon
 */
class XCircle extends Icon {
    static svgString =
        '<svg\n' +
        '    xmlns="http://www.w3.org/2000/svg"\n' +
        '    fill="none"\n' +
        '    viewBox="0 0 24 24"\n' +
        '    stroke-width="1.5"\n' +
        '    stroke="currentColor"\n' +
        '    class="h-6 w-6"\n' +
        '>\n' +
        '    <path\n' +
        '        stroke-linecap="round"\n' +
        '        stroke-linejoin="round"\n' +
        '        d="m9.75 9.75 4.5 4.5m0-4.5-4.5 4.5M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"\n' +
        '    />\n' +
        '</svg>\n';
}

/**
 * Represents an email icon
 */
class Email extends Icon {
    static svgString =
        '<svg\n' +
        '    xmlns="http://www.w3.org/2000/svg"\n' +
        '    fill="none"\n' +
        '    viewBox="0 0 24 24"\n' +
        '    stroke-width="1.5"\n' +
        '    stroke="currentColor"\n' +
        '>\n' +
        '    <path\n' +
        '        stroke-linecap="round"\n' +
        '        stroke-linejoin="round"\n' +
        '        d="M16.5 12a4.5 4.5 0 1 1-9 0 4.5 4.5 0 0 1 9 0Zm0 0c0 1.657 1.007 3 2.25 3S21 13.657 21 12a9 9 0 1 0-2.636 6.364M16.5 12V8.25"\n' +
        '    />\n' +
        '</svg>\n';
}

/**
 * Represents a hamburger icon
 */
class Hamburger extends Icon {
    static svgString =
        '<svg\n' +
        '    xmlns="http://www.w3.org/2000/svg"\n' +
        '    fill="none"\n' +
        '    viewBox="0 0 24 24"\n' +
        '    stroke-width="1.5"\n' +
        '    stroke="currentColor"\n' +
        '>\n' +
        '    <path\n' +
        '        stroke-linecap="round"\n' +
        '        stroke-linejoin="round"\n' +
        '        d="M3.75 9h16.5m-16.5 6.75h16.5"\n' +
        '    />\n' +
        '</svg>\n';
}

/**
 * Represents a moon icon
 */
class Moon extends Icon {
    static svgString =
        '<svg\n' +
        '    xmlns="http://www.w3.org/2000/svg"\n' +
        '    fill="none"\n' +
        '    viewBox="0 0 24 24"\n' +
        '    stroke-width="1.5"\n' +
        '    stroke="currentColor"\n' +
        '>\n' +
        '    <path\n' +
        '        stroke-linecap="round"\n' +
        '        stroke-linejoin="round"\n' +
        '        d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z"\n' +
        '    />\n' +
        '</svg>';
}

/**
 * Represents a user icon
 */
class User extends Icon {
    static svgString =
        '<svg\n' +
        '    xmlns="http://www.w3.org/2000/svg"\n' +
        '    fill="none"\n' +
        '    viewBox="0 0 24 24"\n' +
        '    stroke-width="1.5"\n' +
        '    stroke="currentColor"\n' +
        '>\n' +
        '    <path\n' +
        '        stroke-linecap="round"\n' +
        '        stroke-linejoin="round"\n' +
        '        d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z"\n' +
        '    />\n' +
        '</svg>\n';
}

/**
 * Represents a log-in icon
 */
class LogIn extends Icon {
    static svgString =
        '<svg\n' +
        '    xmlns="http://www.w3.org/2000/svg"\n' +
        '    fill="none"\n' +
        '    viewBox="0 0 24 24"\n' +
        '    stroke-width="1.5"\n' +
        '    stroke="currentColor"\n' +
        '>\n' +
        '    <path\n' +
        '        stroke-linecap="round"\n' +
        '        stroke-linejoin="round"\n' +
        '        d="M15.75 9V5.25A2.25 2.25 0 0 0 13.5 3h-6a2.25 2.25 0 0 0-2.25 2.25v13.5A2.25 2.25 0 0 0 7.5 21h6a2.25 2.25 0 0 0 2.25-2.25V15M12 9l-3 3m0 0 3 3m-3-3h12.75"\n' +
        '    />\n' +
        '</svg>';
}

/**
 * Represents a log-out icon
 */
class LogOut extends Icon {
    static svgString =
        '<svg\n' +
        '    xmlns="http://www.w3.org/2000/svg"\n' +
        '    fill="none"\n' +
        '    viewBox="0 0 24 24"\n' +
        '    stroke-width="1.5"\n' +
        '    stroke="currentColor"\n' +
        '>\n' +
        '    <path\n' +
        '        stroke-linecap="round"\n' +
        '        stroke-linejoin="round"\n' +
        '        d="M8.25 9V5.25A2.25 2.25 0 0 1 10.5 3h6a2.25 2.25 0 0 1 2.25 2.25v13.5A2.25 2.25 0 0 1 16.5 21h-6a2.25 2.25 0 0 1-2.25-2.25V15m-3 0-3-3m0 0 3-3m-3 3H15"\n' +
        '    />\n' +
        '</svg>\n';
}

/**
 * Represents a register icon
 */
class Register extends Icon {
    static svgString =
        '<svg\n' +
        '    xmlns="http://www.w3.org/2000/svg"\n' +
        '    fill="none"\n' +
        '    viewBox="0 0 24 24"\n' +
        '    stroke-width="1.5"\n' +
        '    stroke="currentColor"\n' +
        '>\n' +
        '    <path\n' +
        '        stroke-linecap="round"\n' +
        '        stroke-linejoin="round"\n' +
        '        d="M18 7.5v3m0 0v3m0-3h3m-3 0h-3m-2.25-4.125a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0ZM3 19.235v-.11a6.375 6.375 0 0 1 12.75 0v.109A12.318 12.318 0 0 1 9.374 21c-2.331 0-4.512-.645-6.374-1.766Z"\n' +
        '    />\n' +
        '</svg>\n';
}

export {
    Identification,
    Lock,
    Tick,
    XMark,
    XCircle,
    Email,
    Hamburger,
    Moon,
    User,
    LogIn,
    LogOut,
    Register,
};
