from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Backend API URL
API_URL = os.getenv('BACKEND_API_URL', 'http://backend:5000/api')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/students', methods=['GET'])
def get_students():
    """Proxy to backend API"""
    try:
        response = requests.get(f'{API_URL}/students')
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Failed to fetch students'
        }), 500

@app.route('/api/students', methods=['POST'])
def add_student():
    """Proxy to backend API"""
    try:
        data = request.get_json()
        response = requests.post(f'{API_URL}/students', json=data)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Failed to add student'
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
