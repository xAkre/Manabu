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

export { Identification, Lock, Tick, XMark, XCircle };



