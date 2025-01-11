import unittest
from task1_group.student import Student


class TestStudent(unittest.TestCase):

    def test_create_student_valid(self):
        # Correct object creation
        student = Student("John", "Doe", 20, "ABC-123", "Math")
        self.assertEqual(student.first_name, "John")
        self.assertEqual(student.second_name, "Doe")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.group, "ABC-123")
        self.assertEqual(student.course, "Math")

    def test_create_student_invalid_group(self):
        # Checking for an incorrect group
        with self.assertRaises(ValueError) as context:
            Student("Den", "Don", 22, "", "Java")
        self.assertEqual(str(context.exception), "Group must be a non-empty string.")

    def test_create_student_invalid_course(self):
        # Check for wrong course
        with self.assertRaises(ValueError) as context:
            Student("Den", "Don", 22, "1d", "")
        self.assertEqual(str(context.exception), "Course must be a non-empty string.")

    def test_set_valid_group(self):
        # Checking for the correct group
        student = Student("Den", "Don", 22, "1b", "Java")
        student.group = "2f"
        self.assertEqual(student.group, "2f")

    def test_set_invalid_group(self):
        # Checking the wrong group during the shift
        student = Student("Den", "Don", 22, "1b", "Java")
        with self.assertRaises(ValueError) as context:
            student.group = ""
        self.assertEqual(str(context.exception), "Group must be a non-empty string.")

    def test_set_valid_course(self):
        # Checking for the correct course
        student = Student("Den", "Don", 22, "1b", "Java")
        student.course = "Python"
        self.assertEqual(student.course, "Python")

    def test_set_invalid_course(self):
        # Checking the wrong course during the shift
        student = Student("Den", "Don", 22, "1b", "Java")
        with self.assertRaises(ValueError) as context:
            student.course = ""
        self.assertEqual(str(context.exception), "Course must be a non-empty string.")

    def test_str_representation(self):
        # We check __str__ method
        student = Student("John", "Doe", 30, "1b", "Java")
        self.assertEqual(
            str(student),
            "Student: \nName: John, Surname: Doe, Age: 30, Group: 1b, Course: Java",
        )


if __name__ == "__main__":
    unittest.main()
