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

/**
 * Represents a tag icon
 */
class Tag extends Icon {
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
        '        d="M9.568 3H5.25A2.25 2.25 0 0 0 3 5.25v4.318c0 .597.237 1.17.659 1.591l9.581 9.581c.699.699 1.78.872 2.607.33a18.095 18.095 0 0 0 5.223-5.223c.542-.827.369-1.908-.33-2.607L11.16 3.66A2.25 2.25 0 0 0 9.568 3Z"\n' +
        '    />\n' +
        '    <path\n' +
        '        stroke-linecap="round"\n' +
        '        stroke-linejoin="round"\n' +
        '        d="M6 6h.008v.008H6V6Z"\n' +
        '    />\n' +
        '</svg>\n';
}

/**
 * Represents a briefcase icon
 */
class Briefcase extends Icon {
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
        '        d="M20.25 14.15v4.25c0 1.094-.787 2.036-1.872 2.18-2.087.277-4.216.42-6.378.42s-4.291-.143-6.378-.42c-1.085-.144-1.872-1.086-1.872-2.18v-4.25m16.5 0a2.18 2.18 0 0 0 .75-1.661V8.706c0-1.081-.768-2.015-1.837-2.175a48.114 48.114 0 0 0-3.413-.387m4.5 8.006c-.194.165-.42.295-.673.38A23.978 23.978 0 0 1 12 15.75c-2.648 0-5.195-.429-7.577-1.22a2.016 2.016 0 0 1-.673-.38m0 0A2.18 2.18 0 0 1 3 12.489V8.706c0-1.081.768-2.015 1.837-2.175a48.111 48.111 0 0 1 3.413-.387m7.5 0V5.25A2.25 2.25 0 0 0 13.5 3h-3a2.25 2.25 0 0 0-2.25 2.25v.894m7.5 0a48.667 48.667 0 0 0-7.5 0M12 12.75h.008v.008H12v-.008Z"\n' +
        '    />\n' +
        '</svg>';
}

/**
 * Represent a plus icon
 */
class Plus extends Icon {
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
        '        d="M12 4.5v15m7.5-7.5h-15"\n' +
        '    />\n' +
        '</svg>\n';
}

/**
 * Represents 3 squares with a plus icon
 */
class SquaresPlus extends Icon {
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
        '        d="M13.5 16.875h3.375m0 0h3.375m-3.375 0V13.5m0 3.375v3.375M6 10.5h2.25a2.25 2.25 0 0 0 2.25-2.25V6a2.25 2.25 0 0 0-2.25-2.25H6A2.25 2.25 0 0 0 3.75 6v2.25A2.25 2.25 0 0 0 6 10.5Zm0 9.75h2.25A2.25 2.25 0 0 0 10.5 18v-2.25a2.25 2.25 0 0 0-2.25-2.25H6a2.25 2.25 0 0 0-2.25 2.25V18A2.25 2.25 0 0 0 6 20.25Zm9.75-9.75H18a2.25 2.25 0 0 0 2.25-2.25V6A2.25 2.25 0 0 0 18 3.75h-2.25A2.25 2.25 0 0 0 13.5 6v2.25a2.25 2.25 0 0 0 2.25 2.25Z"\n' +
        '    />\n' +
        '</svg>\n';
}

/**
 * Represents a home icon
 */
class Home extends Icon {
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
        '        d="M8.25 21v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21m0 0h4.5V3.545M12.75 21h7.5V10.75M2.25 21h1.5m18 0h-18M2.25 9l4.5-1.636M18.75 3l-1.5.545m0 6.205 3 1m1.5.5-1.5-.5M6.75 7.364V3h-3v18m3-13.636 10.5-3.819"\n' +
        '    />\n' +
        '</svg>';
}

/**
 * Represents a cog icon
 */
class Cog extends Icon {
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
        '        d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.325.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 0 1 1.37.49l1.296 2.247a1.125 1.125 0 0 1-.26 1.431l-1.003.827c-.293.241-.438.613-.43.992a7.723 7.723 0 0 1 0 .255c-.008.378.137.75.43.991l1.004.827c.424.35.534.955.26 1.43l-1.298 2.247a1.125 1.125 0 0 1-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.47 6.47 0 0 1-.22.128c-.331.183-.581.495-.644.869l-.213 1.281c-.09.543-.56.94-1.11.94h-2.594c-.55 0-1.019-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 0 1-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 0 1-1.369-.49l-1.297-2.247a1.125 1.125 0 0 1 .26-1.431l1.004-.827c.292-.24.437-.613.43-.991a6.932 6.932 0 0 1 0-.255c.007-.38-.138-.751-.43-.992l-1.004-.827a1.125 1.125 0 0 1-.26-1.43l1.297-2.247a1.125 1.125 0 0 1 1.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.086.22-.128.332-.183.582-.495.644-.869l.214-1.28Z"\n' +
        '    />\n' +
        '    <path\n' +
        '        stroke-linecap="round"\n' +
        '        stroke-linejoin="round"\n' +
        '        d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"\n' +
        '    />\n' +
        '</svg>\n';
}

/**
 * Represents a pencil icon
 */
class Pencil extends Icon {
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
        '        d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L6.832 19.82a4.5 4.5 0 0 1-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 0 1 1.13-1.897L16.863 4.487Zm0 0L19.5 7.125"\n' +
        '    />\n' +
        '</svg>\n';
}

/**
 * Represents a trash icon
 */
class Trash extends Icon {
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
        '        d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0"\n' +
        '    />\n' +
        '</svg>';
}

/**
 * Represents a paint brush icon
 */
class PaintBrush extends Icon {
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
        '        d="M9.53 16.122a3 3 0 0 0-5.78 1.128 2.25 2.25 0 0 1-2.4 2.245 4.5 4.5 0 0 0 8.4-2.245c0-.399-.078-.78-.22-1.128Zm0 0a15.998 15.998 0 0 0 3.388-1.62m-5.043-.025a15.994 15.994 0 0 1 1.622-3.395m3.42 3.42a15.995 15.995 0 0 0 4.764-4.648l3.876-5.814a1.151 1.151 0 0 0-1.597-1.597L14.146 6.32a15.996 15.996 0 0 0-4.649 4.763m3.42 3.42a6.776 6.776 0 0 0-3.42-3.42"\n' +
        '    />\n' +
        '</svg>';
}

/**
 * Represents a clock icon
 */
class Clock extends Icon {
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
        '        d="M12 6v6h4.5m4.5 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"\n' +
        '    />\n' +
        '</svg>';
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
    Tag,
    Briefcase,
    Plus,
    SquaresPlus,
    Home,
    Cog,
    Pencil,
    Trash,
    PaintBrush,
    Clock,
};
