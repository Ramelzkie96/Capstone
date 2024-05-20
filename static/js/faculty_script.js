// Function to handle theme toggle
const switchMode = document.getElementById('switch-mode');

switchMode.addEventListener('change', function () {
    if (this.checked) {
        document.body.classList.add('dark');
        setThemePreference('dark'); // Save dark mode preference in local storage
    } else {
        document.body.classList.remove('dark');
        setThemePreference('light'); // Save light mode preference in local storage
    }
});

// Function to set the theme preference in local storage
function setThemePreference(theme) {
    localStorage.setItem('theme', theme);
}

// Function to apply the theme based on the preference stored in local storage
function applyThemeFromLocalStorage() {
    const theme = localStorage.getItem('theme');
    if (theme === 'dark') {
        document.body.classList.add('dark');
        switchMode.checked = true; // Update toggle state
    } else {
        document.body.classList.remove('dark');
        switchMode.checked = false; // Update toggle state
    }
}

// Function to handle sidebar toggle
const menuIcon = document.querySelector('.bx.bx-menu');
const sidebar = document.getElementById('sidebar');

menuIcon.addEventListener('click', function () {
    sidebar.classList.toggle('hide'); // Toggle the 'hide' class on sidebar
});

// Apply theme based on preference when the script is executed
applyThemeFromLocalStorage();

document.addEventListener("DOMContentLoaded", function() {
    const submitBtn = document.getElementById("submit-btn");
    const borrowForm = document.getElementById("borrow-form");

    submitBtn.addEventListener("click", function(event) {
        var inputs = document.querySelectorAll('#borrow-form input[required], #borrow-form textarea[required], #borrow-form select[required]');
        var isValid = true;

        inputs.forEach(function(input) {
            if (input.tagName.toLowerCase() === 'select') {
                // Check if the select field is required and the default option is selected
                if (input.selectedIndex === 0) {
                    input.closest('.field').classList.add('error');
                    isValid = false;
                } else {
                    input.closest('.field').classList.remove('error');
                }
            } else if (input.tagName.toLowerCase() === 'textarea') {
                // Check if the textarea is empty or contains only whitespace
                if (!input.value.trim()) {
                    input.closest('.field').classList.add('error');
                    isValid = false;
                } else {
                    input.closest('.field').classList.remove('error');
                }
            } else if (!input.value.trim()) { // Check if the input value is empty or contains only whitespace
                input.closest('.field').classList.add('error');
                isValid = false;
            } else {
                input.closest('.field').classList.remove('error');
            }
        });

        if (!isValid) {
            // If any field is not filled, show the toast alert with the required message
            showRequiredToast();
            event.preventDefault(); // Prevent form submission
        } else {
            // Show the toast alert for success
            showSuccessToast();

            // Clear all fields
            borrowForm.reset();
        }
    });
});

function showSuccessToast() {
    const toastContent = document.querySelector('.toast .message');
    toastContent.innerHTML = `
        <span class="text text-1">Success</span>
        <span class="text text-2">Your changes have been saved</span>
    `;
    const toast = document.querySelector('.toast');
    const progress = document.querySelector('.progress');

    toast.classList.add('activeee');
    progress.classList.add('activeee');

    setTimeout(() => {
        toast.classList.remove('activeee');
    }, 5000);

    setTimeout(() => {
        progress.classList.remove('activeee');
    }, 5300);
}

function showRequiredToast() {
    const toastContent = document.querySelector('.toast .message');
    toastContent.innerHTML = `
        <span class="text text-1">Required!</span>
        <span class="text text-2">Please fill in all fields.</span>
    `;
    const toast = document.querySelector('.toast');
    const progress = document.querySelector('.progress');

    toast.classList.add('activeee');
    progress.classList.add('activeee');

    setTimeout(() => {
        toast.classList.remove('activeee');
    }, 5000);

    setTimeout(() => {
        progress.classList.remove('activeee');
    }, 5300);
}

const closeIcon = document.getElementById('closee');
closeIcon.addEventListener('click', () => {
    const toast = document.querySelector('.toast');
    const progress = document.querySelector('.progress');

    toast.classList.remove('activeee');

    setTimeout(() => {
        progress.classList.remove('activeee');
    }, 300);
});
