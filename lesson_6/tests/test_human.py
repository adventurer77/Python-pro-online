import unittest
from task1_group.human import Human  # Імпортуємо клас Human із файлу human.py


class TestHuman(unittest.TestCase):
    def test_create_human_valid(self):
        # Перевіряємо коректне створення об'єкта
        person = Human("John", "Doe", 30)
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.second_name, "Doe")
        self.assertEqual(person.age, 30)

    def test_create_human_invalid_first_name(self):
        # Перевіряємо некоректне ім'я
        with self.assertRaises(ValueError) as context:
            Human("", "Doe", 30)
        self.assertEqual(
            str(context.exception), "First name must be a non-empty string."
        )

    def test_create_human_invalid_second_name(self):
        # Перевіряємо некоректне прізвище
        with self.assertRaises(ValueError) as context:
            Human("John", "", 30)
        self.assertEqual(
            str(context.exception), "Second name must be a non-empty string."
        )

    def test_create_human_invalid_age(self):
        # Перевіряємо некоректний вік
        with self.assertRaises(ValueError) as context:
            Human("John", "Doe", -5)
        self.assertEqual(str(context.exception), "Age must be a positive integer.")

    def test_set_valid_first_name(self):
        # Перевіряємо зміну імені
        person = Human("John", "Doe", 30)
        person.first_name = "Jane"
        self.assertEqual(person.first_name, "Jane")

    def test_set_invalid_first_name(self):
        # Перевіряємо некоректне ім'я під час зміни
        person = Human("John", "Doe", 30)
        with self.assertRaises(ValueError) as context:
            person.first_name = ""
        self.assertEqual(
            str(context.exception), "First name must be a non-empty string."
        )

    def test_set_valid_second_name(self):
        # Перевіряємо зміну прізвища
        person = Human("John", "Doe", 30)
        person.second_name = "Smith"
        self.assertEqual(person.second_name, "Smith")

    def test_set_invalid_second_name(self):
        # Перевіряємо некоректне прізвище під час зміни
        person = Human("John", "Doe", 30)
        with self.assertRaises(ValueError) as context:
            person.second_name = ""
        self.assertEqual(
            str(context.exception), "Second name must be a non-empty string."
        )

    def test_set_valid_age(self):
        # Перевіряємо зміну віку
        person = Human("John", "Doe", 30)
        person.age = 35
        self.assertEqual(person.age, 35)

    def test_set_invalid_age(self):
        # Перевіряємо некоректний вік під час зміни
        person = Human("John", "Doe", 30)
        with self.assertRaises(ValueError) as context:
            person.age = -10
        self.assertEqual(str(context.exception), "Age must be a positive integer.")

    def test_str_representation(self):
        # Перевіряємо метод __str__
        person = Human("John", "Doe", 30)
        self.assertEqual(str(person), "Name: John, Surname: Doe, Age: 30")


if __name__ == "__main__":
    unittest.main()
