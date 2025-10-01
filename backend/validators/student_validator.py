import re

def validate_student(data):
    """
    Validates student data according to the same rules as the Express backend.
    Returns (is_valid, error_message)
    """
    if not data:
        return False, 'Request body is required'

    # Validate name
    name = data.get('name', '').strip()
    if not name:
        return False, 'Name is required'
    if len(name) < 2 or len(name) > 100:
        return False, 'Name must be between 2 and 100 characters'
    if not re.match(r'^[a-zA-Z\s\-\.]+$', name):
        return False, 'Name can only contain letters, spaces, hyphens, and periods'

    # Validate roll number
    roll_no = data.get('rollNo', '').strip()
    if not roll_no:
        return False, 'Roll number is required'
    if len(roll_no) < 1 or len(roll_no) > 50:
        return False, 'Roll number must be between 1 and 50 characters'
    if not re.match(r'^[a-zA-Z0-9\-_]+$', roll_no):
        return False, 'Roll number can only contain letters, numbers, hyphens, and underscores'

    # Validate university
    university = data.get('university', '').strip()
    if not university:
        return False, 'University name is required'
    if len(university) < 3 or len(university) > 200:
        return False, 'University name must be between 3 and 200 characters'
    if not re.match(r'^[a-zA-Z0-9\s\-\.\,&\']+$', university):
        return False, 'University name contains invalid characters'

    return True, None
