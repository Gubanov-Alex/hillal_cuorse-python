from dz14_student_group_reg.modul_students.human_class import Human


class Student(Human):
    """Creating Student class"""

    def __init__(self, gender:str, age:int, first_name:str, last_name:str, record_book:str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __eq__(self, other):
        return str(self.last_name) == str(other.last_name) and str(self.record_book) == str(other.record_book)


    def __str__(self):
        return f'{super().__str__()}, {self.record_book}'

    # Test Case
    def __repr__(self) -> str:
        return (f'Student(gender={self.gender}, age={self.age}, '
                f'first_name={self.first_name}, last_name={self.last_name}, '
                f'record_book={self.record_book})')





