import { switchTheme } from './theme.js';
import { openSidebar } from './sidebar.js';

const switchThemeButton = document.querySelector('.switch-theme-button');
switchThemeButton.addEventListener('click', switchTheme);

const openSidebarButton = document.querySelector('.open-sidebar-button');
if (openSidebarButton) {
    openSidebarButton.addEventListener('click', openSidebar);
}

const openUserMenuButton = document.querySelector('.nav-user-button');
const userMenu = document.querySelector('.user-button-context-menu');

openUserMenuButton.addEventListener('click', () => {
    if (userMenu.classList.contains('flex')) {
        userMenu.classList.replace('flex', 'hidden');
    } else {
        userMenu.classList.replace('hidden', 'flex');
    }
});
