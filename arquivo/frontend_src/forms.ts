function updateSliderVisual(container: HTMLElement, slider: HTMLElement, checkbox: HTMLInputElement) {
   if(checkbox.checked) {
       container.classList.remove('bg-gray-200', 'dark:bg-gray-700');
       container.classList.add('bg-indigo-600', 'dark:bg-indigo-500');
       slider.classList.remove('translate-x-0');
       slider.classList.add('translate-x-5');
   }  else {
       container.classList.remove('bg-indigo-600', 'dark:bg-indigo-500');
       container.classList.add('bg-gray-200', 'dark:bg-gray-700');
       slider.classList.remove('translate-x-5');
       slider.classList.add('translate-x-0');
   }
}

function initializeFormToggles() {
    const checkboxes = document.querySelectorAll<HTMLInputElement>('input[type="checkbox"]');
    checkboxes.forEach((checkbox) => {
        const container = checkbox.parentElement;
        if (!container) return;
        const slider = container.querySelector<HTMLElement>('span:not(.sr-only)');
        if (!slider) return;
        container.addEventListener('click', () => {
            checkbox.checked = !checkbox.checked;
            updateSliderVisual(container, slider, checkbox);
        });
    });
}

document.addEventListener('DOMContentLoaded', initializeFormToggles);