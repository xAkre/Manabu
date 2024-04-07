/**
 * Open the sidebar
 */
const openSidebar = () => {
    const sidebar = document.querySelector('.sidebar');
    const pageCover = document.querySelector('.page-cover');

    if (sidebar) {
        pageCover.classList.add('w-screen');
        pageCover.classList.remove('w-0');
        sidebar.classList.add('w-64');
        sidebar.classList.remove('w-0');
    }
};

/**
 * Close the sidebar
 */
const closeSidebar = () => {
    const sidebar = document.querySelector('.sidebar');
    const pageCover = document.querySelector('.page-cover');

    if (sidebar) {
        pageCover.classList.add('w-0');
        pageCover.classList.remove('w-screen');
        sidebar.classList.add('w-0');
        sidebar.classList.remove('w-64');
    }
};

export { openSidebar, closeSidebar };
