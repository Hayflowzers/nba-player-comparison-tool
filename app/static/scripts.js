// Wait for the DOM to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', function() {

    // Basic input validation for player name fields
    document.querySelectorAll('form').forEach(function(form) {
        form.addEventListener('submit', function(event) {
            const playerNameInputs = form.querySelectorAll('input[type="text"]');
            let allValid = true;

            playerNameInputs.forEach(function(input) {
                if (input.value.trim() === '') {
                    allValid = false;
                    input.classList.add('input-error');  // Add a class to highlight the error
                } else {
                    input.classList.remove('input-error');
                }
            });

            if (!allValid) {
                event.preventDefault();  // Prevent the form from submitting if any inputs are invalid
                alert('Please enter a valid player name.');
            }
        });
    });

    // Example for toggling visibility of a section
    document.querySelectorAll('.toggle-btn').forEach(function(button) {
        button.addEventListener('click', function() {
            const target = document.querySelector(button.getAttribute('data-target'));
            if (target) {
                target.classList.toggle('hidden');
            }
        });
    });

    // Adding hover effects on table rows
    document.querySelectorAll('.stats-table tr').forEach(function(row) {
        row.addEventListener('mouseover', function() {
            row.classList.add('row-highlight');
        });

        row.addEventListener('mouseout', function() {
            row.classList.remove('row-highlight');
        });
    });

});

// Function to add row highlighting on hover
function addRowHoverEffect() {
    document.querySelectorAll('.stats-table tr').forEach(function(row) {
        row.addEventListener('mouseover', function() {
            row.style.backgroundColor = '#e9ecef';
        });

        row.addEventListener('mouseout', function() {
            row.style.backgroundColor = '';
        });
    });
}

// Call the function to apply hover effect
addRowHoverEffect();
