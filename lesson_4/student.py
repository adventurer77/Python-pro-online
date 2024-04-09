from human import Human

class Student(Human):

    def __init__(self, first_name, second_name, age,group,course):
        super().__init__(first_name, second_name, age)
        self.group = group
        self.course = course


    def __str__(self):
        return f"Student: \n{super().__str__()}, Group: {self.group}, Course: {self.course}"