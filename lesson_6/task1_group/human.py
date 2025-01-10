class Human:

    def __init__(self, first_name: str, second_name: str, age: int):
        if not isinstance(first_name, str) or not first_name.strip():
            raise ValueError("First name must be a non-empty string.")
        if not isinstance(second_name, str) or not second_name.strip():
            raise ValueError("Second name must be a non-empty string.")

        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")

        self._first_name = first_name
        self._second_name = second_name
        self._age = age

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("First name must be a non-empty string.")
        self._first_name = value.strip()

    @property
    def second_name(self) -> str:
        return self._second_name

    @second_name.setter
    def second_name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Second name must be a non-empty string.")
        self._second_name = value.strip()

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Age must be a positive integer.")
        self._age = value

    def __str__(self) -> str:
        return f"Name: {self.first_name}, Surname: {self.second_name}, Age: {self.age}"