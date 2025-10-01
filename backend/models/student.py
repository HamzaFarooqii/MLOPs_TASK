import time

class Student:
    def __init__(self, name, roll_no, university):
        self.name = name
        self.roll_no = roll_no
        self.university = university
        self.id = str(int(time.time() * 1000))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'rollNo': self.roll_no,
            'university': self.university
        }
