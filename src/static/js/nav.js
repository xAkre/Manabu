import { switchTheme } from './theme.js';
import { openSidebar } from './sidebar.js';

const switchThemeButton = document.querySelector('.switch-theme-button');
switchThemeButton.addEventListener('click', switchTheme);

const openSidebarButton = document.querySelector('.open-sidebar-button');
if (openSidebarButton) {
    openSidebarButton.addEventListener('click', openSidebar);
}
