class Human:
    """Abstract class for human"""

    def __init__(self, gender:str, age:int, first_name:str, last_name:str):
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

    def __init__(self, gender:str, age:int, first_name:str, last_name:str, record_book:str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book


    def __str__(self):
        return f'{super().__str__()}, {self.record_book}'

    # Test Case
    def __repr__(self) -> str:
        return (f'Student(gender={self.gender}, age={self.age}, '
                f'first_name={self.first_name}, last_name={self.last_name}, '
                f'record_book={self.record_book})')

class Teacher(Human):
    """Creating Teacher class"""

    def __init__(self, gender:str, age:int, first_name:str, last_name:str, teacher_book:str ):
        super().__init__(gender, age, first_name, last_name)
        self.teacher_book = teacher_book



class CheckCapacityError(Exception):
    """Checking capacity of  the group <`10"""
    def __init__(self, message="Group capacity are 10 students"):
        self.message = message
        super().__init__(self.message)


class Group:
    """Creating Group class for students"""

    MAX_CAPACITY = 10

    def __init__(self, number):
        self.number = number
        self.group = []

    def add_student(self, student:Student):
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


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 34, 'Shiza', 'Taylor', 'AN147')
st4 = Student('Female', 18, 'Vasya', 'Roui', 'AN148')
st5 = Student('Male', 21, 'Sasha', 'Tay', 'AN149')
st6 = Student('Female', 25, 'Sergey', 'lor', 'AN150')
st7 = Student('Female', 25, 'Dima', 'Ylor', 'AN151')
st8 = Student('Male', 24, 'Vova', 'Derty', 'AN152')
st9 = Student('Female', 24, 'Nastya', 'Sahj', 'AN153')
st10 = Student('Female', 19, 'Masha', 'Kyur', 'AN154')
gr = Group('PD1')

try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    print(gr)

    st11 = Student('Female', 25, 'Joye', 'Bayden', 'AN155')
    gr.add_student(st11)
except CheckCapacityError as e:
    print(f"Error Student Add: {e}")

# print(gr)

try:
    st12 = Teacher('Male', 30, 'Steve', 'Jobs', 'VN1119')
    gr.add_student(st12)
except TypeError as e:
    print(f"Error type: {e}")



