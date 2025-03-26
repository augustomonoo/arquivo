// Dark mode functionality
function updateTheme(theme: 'light' | 'dark' | 'system') {
    if (theme === 'system') {
        if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
    } else {
        if (theme === 'dark') {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
    }
    localStorage.theme = theme;
}

function togglePanel(show: boolean) {
    const panel = document.getElementById('themePanel');
    if (panel) {
        if (show) {
            panel.classList.remove('-translate-x-full');
        } else {
            panel.classList.add('-translate-x-full');
        }
    }
}

function updateThemeIcon(theme: string) {
    const icons = document.querySelectorAll('.theme-icon');
    const isDark = document.documentElement.classList.contains('dark');
    
    icons.forEach(icon => {
        // Show moon icon if light, sun icon if dark
        if (isDark && icon.getAttribute('data-theme') === 'light') {
            icon.classList.remove('hidden');
        } else if (!isDark && icon.getAttribute('data-theme') === 'dark') {
            icon.classList.remove('hidden');
        } else {
            icon.classList.add('hidden');
        }
    });
}

function setTheme(theme: string) {
    if (theme === 'system') {
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        document.documentElement.classList.toggle('dark', prefersDark);
    } else if (theme === 'dark') {
        document.documentElement.classList.add('dark');
    } else {
        document.documentElement.classList.remove('dark');
    }
    localStorage.setItem('theme', theme);
    updateThemeIcon(theme);
}

function initializeTheme() {
    const savedTheme = localStorage.getItem('theme') || 'system';
    if (savedTheme === 'system') {
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        document.documentElement.classList.toggle('dark', prefersDark);
    } else {
        setTheme(savedTheme);
    }
    updateThemeIcon(savedTheme);
}

function initDarkMode() {
    const darkModeToggle = document.getElementById('darkModeToggle');
    const themePanel = document.getElementById('themePanel');
    const themeOptions = document.querySelectorAll('.theme-option');

    // Set initial theme
    initializeTheme();

    // Toggle panel
    if (darkModeToggle && themePanel) {
        darkModeToggle.addEventListener('click', () => {
            const isVisible = !themePanel.classList.contains('-translate-x-full');
            togglePanel(!isVisible);
        });

        // Close panel when clicking outside
        document.addEventListener('click', (e) => {
            if (!darkModeToggle.contains(e.target as Node) && !themePanel.contains(e.target as Node)) {
                togglePanel(false);
            }
        });
    }

    // Handle theme selection
    themeOptions.forEach(option => {
        option.addEventListener('click', () => {
            const theme = (option as HTMLElement).dataset.theme as 'light' | 'dark' | 'system';
            setTheme(theme);
            togglePanel(false);
        });
    });

    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (localStorage.theme === 'system') {
            if (e.matches) {
                document.documentElement.classList.add('dark');
            } else {
                document.documentElement.classList.remove('dark');
            }
            // Update the icon when system theme changes
            updateThemeIcon('system');
        }
    });
}

// Initialize dark mode when the DOM is loaded
document.addEventListener('DOMContentLoaded', initDarkMode); 