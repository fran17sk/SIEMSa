/**
 * SIEMSa - Gestión de Interfaz (Sidebar, Temas y Submenús)
 * Versión optimizada para archivos estáticos
 */

// --- 1. FUNCIONES GLOBALES (Disponibles para atributos onclick del HTML) ---

function updateIcons() {
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
}

function toggleCollapse() {
    const sidebar = document.getElementById('sidebar');
    const btnIcon = document.querySelector('.collapse-btn i');
    
    if (!sidebar) return;

    document.documentElement.classList.remove('sidebar-init-collapsed');
    sidebar.classList.toggle('collapsed');
    
    const isCollapsed = sidebar.classList.contains('collapsed');
    localStorage.setItem('sidebarCollapsed', isCollapsed);
    
    if (btnIcon) {
        btnIcon.setAttribute('data-lucide', isCollapsed ? 'chevrons-right' : 'chevrons-left');
    }
    
    updateIcons();
}

function toggleTheme() {
    const body = document.body;
    const themeIcon = document.getElementById('theme-icon');
    const themeText = document.getElementById('theme-text');
    
    body.classList.toggle('light-mode');
    document.documentElement.classList.toggle('light-mode');
    
    const isLight = document.documentElement.classList.contains('light-mode');
    localStorage.setItem('theme', isLight ? 'light' : 'dark');
    
    if (themeIcon && themeText) {
        themeIcon.setAttribute('data-lucide', isLight ? 'sun' : 'moon');
        themeText.innerText = isLight ? 'Modo Claro' : 'Modo Oscuro';
    }
    
    updateIcons();
}

// --- 2. INICIALIZACIÓN Y EVENTOS DINÁMICOS ---

window.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById('sidebar');
    const btnIcon = document.querySelector('.collapse-btn i');
    const themeIcon = document.getElementById('theme-icon');
    const themeText = document.getElementById('theme-text');

    // A. Gestión de Submenús (Delegación de eventos para mayor robustez)
    document.addEventListener('click', (e) => {
        const trigger = e.target.closest('.submenu-trigger');
        
        if (trigger) {
            e.preventDefault();
            e.stopPropagation();

            const parent = trigger.closest('.menu-item');
            if (!parent) return;

            const isOpen = parent.classList.contains('open');

            // Efecto Acordeón: Cerrar otros submenús
            document.querySelectorAll('.menu-item.open').forEach(item => {
                if (item !== parent) {
                    item.classList.remove('open');
                }
            });

            // Toggle del actual
            parent.classList.toggle('open');
            updateIcons();
        }
    });

    // B. Recuperar estados de localStorage
    const isCollapsed = localStorage.getItem('sidebarCollapsed') === 'true';
    const savedTheme = localStorage.getItem('theme');

    // C. Aplicar Tema Guardado
    if (savedTheme === 'light') {
        document.documentElement.classList.add('light-mode');
        document.body.classList.add('light-mode');
    } else {
        document.documentElement.classList.remove('light-mode');
        document.body.classList.remove('light-mode');
    }

    // D. Aplicar Estado de Sidebar Guardado
    if (sidebar) {
        if (isCollapsed) {
            sidebar.classList.add('collapsed');
            if (btnIcon) btnIcon.setAttribute('data-lucide', 'chevrons-right');
        } else {
            sidebar.classList.remove('collapsed');
            if (btnIcon) btnIcon.setAttribute('data-lucide', 'chevrons-left');
        }
    }

    // E. Sincronizar textos e iconos de tema
    const isLightNow = document.documentElement.classList.contains('light-mode');
    if (themeIcon && themeText) {
        themeIcon.setAttribute('data-lucide', isLightNow ? 'sun' : 'moon');
        themeText.innerText = isLightNow ? 'Modo Claro' : 'Modo Oscuro';
    }

    // F. Renderizado final de iconos
    updateIcons();
});