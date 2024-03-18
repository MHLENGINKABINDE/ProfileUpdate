// Function to update the user profile
function updateProfile(username, email, fullname, password, dob, gender, address, phone) {
    // Perform necessary actions to update the profile
    console.log("Updating profile...");
    console.log("Username:", username);
    console.log("Email:", email);
    console.log("Name:", fullname);
    console.log("Password:", password);
    console.log("Date of Birth:", dob);
    console.log("Gender:", gender);
    console.log("Address:", address);
    console.log("Phone Number:", phone);
}

// Event listener for form submission
document.getElementById('profileForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Get form data
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const fullname = document.getElementById('fullname').value;
    const password = document.getElementById('password').value;
    const dob = document.getElementById('dob').value;
    const gender = document.getElementById('gender').value;
    const address = document.getElementById('address').value;
    const phone = document.getElementById('phone').value;

    // Update profile
    updateProfile(username, email, fullname, password, dob, gender, address, phone);

    // Display success message (for demonstration)
    document.getElementById('message').innerText = 'Profile updated successfully!';
});
