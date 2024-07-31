// app/static/js/script.js

document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const submitButton = document.querySelector('button[type="submit"]');
    const resultContainer = document.querySelector('.result');

    form.addEventListener('submit', function (e) {
        const inputs = form.querySelectorAll('input[type="number"]');
        let valid = true;

        // Basic client-side validation
        inputs.forEach(input => {
            if (input.value.trim() === '') {
                alert(`Please enter a value for ${input.previousElementSibling.textContent}`);
                valid = false;
            } else if (parseFloat(input.value) <= 0) {
                alert('Please enter a positive number');
                valid = false;
            }
        });

        if (!valid) {
            e.preventDefault(); // Prevent form submission
            return;
        }

        // Add loading state
        submitButton.disabled = true;
        submitButton.textContent = 'Predicting...';

        // Show a loading animation
        resultContainer.innerHTML = '<p>Loading...</p>';

        // Allow form submission to proceed after a brief delay
        setTimeout(() => {
            submitButton.disabled = false;
            submitButton.textContent = 'Predict';
        }, 2000); // Adjust the timeout as needed
    });
});
