from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.validators import StudentValidator, ValidationError
from app.models import Student
from app.storage import storage

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    """Main route to handle form submission and display"""
    if request.method == 'POST':
        try:
            # Get form data
            name = request.form.get('name', '')
            roll_no = request.form.get('roll_no', '')
            university = request.form.get('university', '')

            # Validate input
            validated_data = StudentValidator.validate_student(name, roll_no, university)

            # Create and store student
            student = Student(
                validated_data['name'],
                validated_data['roll_no'],
                validated_data['university']
            )
            storage.add_student(student)

            flash('Student record added successfully!', 'success')
            return redirect(url_for('main.index'))

        except ValidationError as e:
            flash(str(e), 'error')
        except Exception as e:
            flash(f'An unexpected error occurred: {str(e)}', 'error')

    # Get all students for display
    students = storage.get_all_students()
    return render_template('index.html', students=students)

@main.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@main.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('500.html'), 500
