from student import Student
from user_exception import UserException

class Group:

    def __init__(self,limit_group = 10):
       
       self.__groups = []
       self.limit_group = limit_group  

    def add_student(self,student:Student):

        if len(self.__groups) >= self.limit_group:
            raise UserException("The group is full", self.limit_group)
        
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