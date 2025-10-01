class StudentStorage:
    """In-memory storage for student records"""

    def __init__(self):
        self.students = []

    def add_student(self, student):
        """Add a student to storage"""
        self.students.append(student)

    def get_all_students(self):
        """Get all students"""
        return self.students

    def clear_all(self):
        """Clear all students"""
        self.students = []

# Global storage instance
storage = StudentStorage()
