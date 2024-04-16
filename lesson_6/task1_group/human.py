class Human:

    def __init__(self,first_name,second_name,age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def __str__(self):
        return f"Name: {self.first_name} Surname: {self.second_name} Age: {self.age}"