from Student import Student


class StudentStorage:
    studentsArray = []

    def __init__(self):
        print("Storage initialized")

    def fill_init_students(self) -> None:
        print("fill_init_students called")
        student1 = Student("Иванов", "А97", 1)
        student2 = Student("Смирнов", "С76", 2)
        student3 = Student("Петров", "Е54", 3)

        self.studentsArray.append(student1)
        self.studentsArray.append(student2)
        self.studentsArray.append(student3)

    def get_all_students(self) -> []:
        return self.studentsArray

    def add_student(self, student):
        self.studentsArray.append(student)
