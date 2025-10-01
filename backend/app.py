from flask import Flask, request, jsonify
from flask_cors import CORS
from models.student import Student
from models.storage import storage
from validators.student_validator import validate_student

app = Flask(__name__)
CORS(app)

# Health check
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({'message': 'Student Management API is running'}), 200

# Get all students
@app.route('/api/students', methods=['GET'])
def get_students():
    try:
        students = storage.get_all_students()
        return jsonify({
            'success': True,
            'data': students
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'An unexpected error occurred'
        }), 500

# Add new student
@app.route('/api/students', methods=['POST'])
def add_student():
    try:
        data = request.get_json()

        # Validate input
        is_valid, error_message = validate_student(data)
        if not is_valid:
            return jsonify({
                'success': False,
                'message': error_message
            }), 400

        # Create and store student
        student = Student(
            data.get('name'),
            data.get('rollNo'),
            data.get('university')
        )
        storage.add_student(student)

        return jsonify({
            'success': True,
            'message': 'Student record added successfully!',
            'data': student.to_dict()
        }), 201

    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'An unexpected error occurred'
        }), 500

# 404 handler
@app.errorhandler(404)
def not_found(e):
    return jsonify({
        'success': False,
        'message': 'Route not found'
    }), 404

# Error handler
@app.errorhandler(500)
def server_error(e):
    return jsonify({
        'success': False,
        'message': 'Something went wrong!'
    }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
