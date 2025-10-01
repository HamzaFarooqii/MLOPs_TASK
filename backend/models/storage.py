class Storage:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_all_students(self):
        return [student.to_dict() for student in self.students]

    def clear_all(self):
        self.students = []

# Singleton instance
storage = Storage()
