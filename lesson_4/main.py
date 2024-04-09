
from student import Student
from group import Group
from user_exception import UserException



if __name__ == '__main__':

    try:
        st = Student("Den","Don",22,"1b","Java")
        st2 = Student("Mark","Vex",33,"2a","Python")
        st3 = Student("Sam","Fex",25,"3f","C#")
        # print(st)

        gg = Group()
        gg.add_student(st)
        gg.add_student(st2)
        gg.add_student(st3)
        # gg.add_student(st3)
        # gg.add_student(st3)
        # gg.add_student(st3)
        # gg.add_student(st3)
        # gg.add_student(st3)
        # gg.add_student(st3)
        # gg.add_student(st3)
        # gg.add_student(st3)
        
        print(gg)

        gg.del_student(st)
        print(gg)

        # found_student = gg.find_student("Vex")

        # if found_student:
        #     print("Found student:\n",found_student)
        # else:
        #     print("No student with this last name was found.")

    except UserException as ex:
        print(ex)
    except Exception as e:
        print(e)