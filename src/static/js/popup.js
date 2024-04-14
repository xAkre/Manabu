import { uuidv4 } from './helpers/uuid.js';
import { Tick, XCircle } from './icon.js';

/**
 * Creates a popup
 *
 * @param {string} type - The type of popup
 * @param {string} message - The popup message
 * @returns {HTMLDivElement} The popup
 */
const createPopup = (type, message) => {
    /* Create the container */
    const popupUuid = uuidv4();
    const container = document.createElement('div');
    container.className =
        'flex w-full items-center gap-2 rounded-md border-l-2 bg-slate-50 p-3 transition-all duration-1000 ease-in-out dark:bg-slate-900 shadow-md';
    container.dataset['id'] = popupUuid;

    /*
        There is definitely a better way to do this, such as declaring the color
        earlier and interpolating it, however, I need tailwind to detect the class name which
        is why I do it like this
    */
    if (type === 'success') {
        container.classList.add('border-green-500', 'dark:border-green-400');
    } else {
        container.classList.add('border-red-500', 'dark:border-red-400');
    }

    /* Set the icon */
    let { svgElement } =
        type === 'success'
            ? new Tick('h-7 aspect-square shrink-0')
            : new XCircle('h-7 aspect-square shrink-0');
    if (type === 'success') {
        svgElement.classList.add('text-green-500', 'dark:text-green-400');
    } else {
        svgElement.classList.add('text-red-500', 'dark:text-red-400');
    }

    container.appendChild(svgElement);

    /* Create the content container */
    const content = document.createElement('div');
    content.className = 'flex flex-col gap-1';

    /* Set the title */
    const errorTitle = document.createElement('div');
    errorTitle.textContent = type === 'success' ? 'Success' : 'Error';
    errorTitle.className =
        'text-sm text-slate-900 dark:text-slate-100 leading-none';
    content.appendChild(errorTitle);

    /* Set the popup content */
    const errorText = document.createElement('div');
    errorText.className =
        'text-2xs text-slate-500 dark:text-slate-400 leading-none';
    errorText.textContent = message;
    content.appendChild(errorText);

    container.appendChild(content);

    return container;
};

/**
 * Append a popup to a container. The popup will be automatically removed after 5 seconds
 *
 * @param {HTMLDivElement} popup - The popup to be appended
 * @param {HTMLElement} container - The container to be appended to. Defaults to document.querySelector('.popup-container')
 */
const appendPopup = (
    popup,
    container = document.querySelector('.popup-container'),
) => {
    container.appendChild(popup);

    setTimeout(() => {
        popup.style.transform = 'translateY(-100%)';
        popup.style.opacity = '0';

        setTimeout(() => {
            popup.remove();
        }, 1000);
    }, 5000);
};

export { createPopup, appendPopup };
