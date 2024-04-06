/**
 * Open the sidebar
 */
const openSidebar = () => {
    const sidebar = document.querySelector('.sidebar');

    if (sidebar) {
        sidebar.classList.add('w-64');
        sidebar.classList.remove('w-0');
    }
};

/**
 * Close the sidebar
 */
const closeSidebar = () => {
    const sidebar = document.querySelector('.sidebar');

    if (sidebar) {
        sidebar.classList.add('w-0');
        sidebar.classList.remove('w-64');
    }
};

export { openSidebar, closeSidebar };
