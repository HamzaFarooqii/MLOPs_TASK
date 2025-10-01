// Fetch and display students on page load
document.addEventListener('DOMContentLoaded', () => {
    fetchStudents();

    // Handle form submission
    document.getElementById('studentForm').addEventListener('submit', handleSubmit);
});

// Fetch all students from API
async function fetchStudents() {
    try {
        const response = await fetch('/api/students');
        const data = await response.json();

        if (data.success) {
            displayStudents(data.data);
        }
    } catch (error) {
        console.error('Error fetching students:', error);
    }
}

// Display students in table
function displayStudents(students) {
    const tableContainer = document.getElementById('tableContainer');

    if (students.length === 0) {
        tableContainer.innerHTML = `
            <div class="no-data">
                No student records found. Add a student using the form above.
            </div>
        `;
        return;
    }

    let tableHTML = `
        <table>
            <thead>
                <tr>
                    <th>S.No</th>
                    <th>Name</th>
                    <th>Roll Number</th>
                    <th>University</th>
                </tr>
            </thead>
            <tbody>
    `;

    students.forEach((student, index) => {
        tableHTML += `
            <tr>
                <td>${index + 1}</td>
                <td>${student.name}</td>
                <td>${student.rollNo}</td>
                <td>${student.university}</td>
            </tr>
        `;
    });

    tableHTML += `
            </tbody>
        </table>
    `;

    tableContainer.innerHTML = tableHTML;
}

// Handle form submission
async function handleSubmit(e) {
    e.preventDefault();

    const formData = {
        name: document.getElementById('name').value,
        rollNo: document.getElementById('rollNo').value,
        university: document.getElementById('university').value
    };

    try {
        const response = await fetch('/api/students', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        const data = await response.json();

        if (data.success) {
            showFlashMessage(data.message, 'success');
            document.getElementById('studentForm').reset();
            fetchStudents();
        } else {
            showFlashMessage(data.message, 'error');
        }
    } catch (error) {
        showFlashMessage('An unexpected error occurred', 'error');
    }
}

// Show flash message
function showFlashMessage(message, type) {
    const flashContainer = document.getElementById('flash-messages');

    const flashDiv = document.createElement('div');
    flashDiv.className = `flash ${type}`;
    flashDiv.textContent = message;

    flashContainer.innerHTML = '';
    flashContainer.appendChild(flashDiv);

    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        flashDiv.remove();
    }, 5000);
}
