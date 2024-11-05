from dz14_student_group_reg.modul_students.check_status import CheckCapacityError
from dz14_student_group_reg.modul_students.student_class import Student


class Group:
    """Creating Group class for students"""
    MAX_CAPACITY = 10

    def __init__(self, number):
        self.number = number
        self.group = []

    def add_student(self, student):
        """Adding student to group"""
        if not isinstance(student, Student):
            raise TypeError("Ты кто такой? Только студентов принимаем))")
        elif len(self.group) >= Group.MAX_CAPACITY:
            raise CheckCapacityError()
        self.group.append(student)

    def delete_student(self, last_name,record_book):
        """Deleting student from group"""
        student = self.find_student(last_name,record_book)
        if student:
            self.group.remove(student)

    def find_student(self, last_name,record_book):
        """Checking for student in group"""
        for student in self.group:
            if student.last_name == last_name and student.record_book == record_book:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'