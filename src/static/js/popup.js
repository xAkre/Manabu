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
        'flex w-full items-center gap-2 rounded-md border-l-2 bg-slate-50 p-2 transition-all duration-1000 ease-in-out dark:bg-slate-900 shadow-md md:p-3';
    container.dataset['id'] = popupUuid;

    /*
        There is definitely a better way to do this, such as declaring the color
        earlier and interpolating it, however, I need tailwind to detect the class name which
        is why I do it like this
    */
    if (type === 'success') {
        container.classList.add('border-green-500', 'dark:border-green-900');
    } else {
        container.classList.add('border-red-500', 'dark:border-red-900');
    }

    /* Set the icon */
    let { svgElement } =
        type === 'success'
            ? new Tick('h-6 aspect-square shrink-0 md:h-7')
            : new XCircle('h-6 aspect-square shrink-0 md:h-7');
    if (type === 'success') {
        svgElement.classList.add('text-green-500', 'dark:text-green-900');
    } else {
        svgElement.classList.add('text-red-500', 'dark:text-red-900');
    }

    container.appendChild(svgElement);

    /* Create the content container */
    const content = document.createElement('div');
    content.className = 'flex flex-col gap-0.5';

    /* Set the title */
    const errorTitle = document.createElement('div');
    errorTitle.textContent = type === 'success' ? 'Success' : 'Error';
    errorTitle.className = 'text-xs text-slate-900 dark:text-slate-100';
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
 * @param {HTMLElement} container - The container to be appended to
 */
const appendPopup = (popup, container) => {
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
