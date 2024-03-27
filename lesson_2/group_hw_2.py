class Human:

    def __init__(self,first_name,second_name,age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def __str__(self):
        return f"Name: {self.first_name} Surname: {self.second_name} Age: {self.age}"
    

class Student(Human):

    def __init__(self, first_name, second_name, age,group,course):
        super().__init__(first_name, second_name, age)
        self.group = group
        self.course = course


    def __str__(self):
        return f"Student: \n{super().__str__()}, Group: {self.group}, Course: {self.course}"


class Group:
    def __init__(self):
       self.__groups = []

    def add_student(self,student:Student):
        self.__groups.append(student)

    def del_student(self,student:Student):

        if student in self.__groups:
            index = self.__groups.index(student)
            del self.__groups[index]
        else:
            print("Group is empty!")

    def find_student(self,surname):
            for student in self.__groups:
                if student.second_name == surname:  
                    return student  
            return None
        
            

    def __str__(self) -> str:
        return "\n".join(map(str,self.__groups))


if __name__ == '__main__':
    
    st = Student("Den","Don",22,"1b","Java")
    st2 = Student("Mark","Vex",33,"2a","Python")
    st3 = Student("Sam","Fex",25,"3f","C#")
    # print(st)

    gg = Group()
    gg.add_student(st)
    gg.add_student(st2)
    gg.add_student(st3)
    # print(gg)

    # gg.del_student(st)
    # print(gg)

    found_student = gg.find_student("Vex")

    if found_student:
        print("Found student:\n",found_student)
    else:
        print("No student with this last name was found.")