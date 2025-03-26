console.log('Forms script starting to load...');

function initializeFormToggles() {
    const toggles = document.querySelectorAll<HTMLInputElement>('input[type="checkbox"]');

    toggles.forEach((toggle) => {
        const toggleContainer = toggle.parentElement;
        if (!toggleContainer) return;

        if (!toggleContainer.hasAttribute('data-toggle-initialized')) {
            toggleContainer.setAttribute('data-toggle-initialized', 'true');

            // Add click handler to the container
            toggleContainer.addEventListener('click', (e: Event) => {
                e.preventDefault();
                toggle.checked = !toggle.checked;
                toggle.dispatchEvent(new Event('change'));
            });

            // Add change handler to the checkbox to update visual state
            toggle.addEventListener('change', () => {
                const thumb = toggleContainer.querySelector('span:not(.sr-only)');
                if (thumb) {
                    if (toggle.checked) {
                        thumb.classList.remove('translate-x-0');
                        thumb.classList.add('translate-x-5');
                        toggleContainer.classList.remove('bg-gray-200', 'dark:bg-gray-700');
                        toggleContainer.classList.add('bg-indigo-600', 'dark:bg-indigo-500');
                    } else {
                        thumb.classList.remove('translate-x-5');
                        thumb.classList.add('translate-x-0');
                        toggleContainer.classList.remove('bg-indigo-600', 'dark:bg-indigo-500');
                        toggleContainer.classList.add('bg-gray-200', 'dark:bg-gray-700');
                    }
                }
            });

            // Set initial visual state
            const thumb = toggleContainer.querySelector('span:not(.sr-only)');
            if (thumb) {
                if (toggle.checked) {
                    thumb.classList.remove('translate-x-0');
                    thumb.classList.add('translate-x-5');
                    toggleContainer.classList.remove('bg-gray-200', 'dark:bg-gray-700');
                    toggleContainer.classList.add('bg-indigo-600', 'dark:bg-indigo-500');
                } else {
                    thumb.classList.remove('translate-x-5');
                    thumb.classList.add('translate-x-0');
                    toggleContainer.classList.remove('bg-indigo-600', 'dark:bg-indigo-500');
                    toggleContainer.classList.add('bg-gray-200', 'dark:bg-gray-700');
                }
            }
        }
    });
}

// Initialize on DOMContentLoaded
document.addEventListener('DOMContentLoaded', initializeFormToggles); 