class Student:
    """Student model to store student information"""

    def __init__(self, name, roll_no, university):
        self.name = name
        self.roll_no = roll_no
        self.university = university

    def to_dict(self):
        """Convert student object to dictionary"""
        return {
            'name': self.name,
            'roll_no': self.roll_no,
            'university': self.university
        }

    def __repr__(self):
        return f"Student(name='{self.name}', roll_no='{self.roll_no}', university='{self.university}')"
