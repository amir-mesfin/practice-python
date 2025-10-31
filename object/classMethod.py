class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):

        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

        #  inistant method

    def get_info(self):
        return f"{self.name} {self.gpa}"

      # class method
    @classmethod
    def get_count(cls):
        return f"total of student {cls.count}"

    @classmethod
    def get_total_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            average = cls.total_gpa / cls.count
            return f" total gpa of the year {average:.2f}"


student1 = Student("abushe", 4.00)
student2 = Student("amirachn", 4.78)

print(Student.get_count())
print(Student.get_total_gpa())
