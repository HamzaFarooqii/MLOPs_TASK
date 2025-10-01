import re

class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass

class StudentValidator:
    """Validator for student information"""

    @staticmethod
    def validate_name(name):
        """Validate student name"""
        if not name or not name.strip():
            raise ValidationError("Name is required")

        if len(name.strip()) < 2:
            raise ValidationError("Name must be at least 2 characters long")

        if len(name.strip()) > 100:
            raise ValidationError("Name must not exceed 100 characters")

        if not re.match(r'^[a-zA-Z\s\-\.]+$', name.strip()):
            raise ValidationError("Name can only contain letters, spaces, hyphens, and periods")

        return name.strip()

    @staticmethod
    def validate_roll_no(roll_no):
        """Validate roll number"""
        if not roll_no or not roll_no.strip():
            raise ValidationError("Roll number is required")

        if len(roll_no.strip()) < 1:
            raise ValidationError("Roll number cannot be empty")

        if len(roll_no.strip()) > 50:
            raise ValidationError("Roll number must not exceed 50 characters")

        if not re.match(r'^[a-zA-Z0-9\-_]+$', roll_no.strip()):
            raise ValidationError("Roll number can only contain letters, numbers, hyphens, and underscores")

        return roll_no.strip()

    @staticmethod
    def validate_university(university):
        """Validate university name"""
        if not university or not university.strip():
            raise ValidationError("University name is required")

        if len(university.strip()) < 3:
            raise ValidationError("University name must be at least 3 characters long")

        if len(university.strip()) > 200:
            raise ValidationError("University name must not exceed 200 characters")

        if not re.match(r'^[a-zA-Z0-9\s\-\.\,&\']+$', university.strip()):
            raise ValidationError("University name contains invalid characters")

        return university.strip()

    @classmethod
    def validate_student(cls, name, roll_no, university):
        """Validate all student fields"""
        validated_data = {
            'name': cls.validate_name(name),
            'roll_no': cls.validate_roll_no(roll_no),
            'university': cls.validate_university(university)
        }
        return validated_data
