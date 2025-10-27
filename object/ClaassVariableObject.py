class Student :
    gratuition_year = 2025  # Class Variable
    num_students = 0      # Class Variable

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

print(f"{student1.name} will graduate in {student1.gratuition_year}")
print(f"{student2.name} will graduate in {student2.gratuition_year}")

student3 = Student("Charlie", 23)

print(f"{student3.name} will graduate in {Student.gratuition_year}")
print(f"Total number of students: {Student.num_students}")
