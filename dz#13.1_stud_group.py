class Human:
    """Abstract class for human"""

    def __init__(self, gender:str, age:str, first_name:str, last_name:str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return (f'{self.first_name} '
                f'{self.last_name}, '
                f'{self.age}, '
                f'{self.gender}'
                )

class Student(Human):
    """Creating Student class"""

    def __init__(self, gender:str, age:str, first_name:str, last_name:str, record_book:str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book


    def __str__(self):
        return f'{super().__str__()}, {self.record_book}'

    # Test Case
    def __repr__(self) -> str:
        return (f'Student(gender={self.gender}, age={self.age}, '
                f'first_name={self.first_name}, last_name={self.last_name}, '
                f'record_book={self.record_book})')


class Group:
    """Creating Group class for students"""

    def __init__(self, number):
        self.number = number
        self.group = []

    def add_student(self, student):
        """Adding student to group"""
        if not isinstance(student, Student):
            raise TypeError("Ты кто такой? Только студентов принимаем))")
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

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs', 'AN142')) == str(st1), 'Test1'
assert gr.find_student('Jobs2', 'AN142') is None, 'Test2'
assert isinstance(gr.find_student('Jobs', 'AN142'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor', 'AN145')
print(gr)  # Only one student

gr.delete_student('Taylor', 'AN145')  # No error!