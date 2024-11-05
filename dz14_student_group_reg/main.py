from dz14_student_group_reg.modul_students.group_class import Group
from dz14_student_group_reg.modul_students.student_class import Student


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs', 'AN142') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2', 'AN142') is None

gr.delete_student('Taylor', 'AN145')
print(gr) # Only one student