from .human import Human


class Student(Human):

    def __init__(
        self, first_name: str, second_name: str, age: int, group: str, course: str
    ):
        super().__init__(first_name, second_name, age)

        if not isinstance(group, str) or not group.strip():
            raise ValueError("Group must be a non-empty string.")
        if not isinstance(course, str) or not course.strip():
            raise ValueError("Course must be a non-empty string.")

        self._group = group.strip()
        self._course = course.strip()

    @property
    def group(self) -> str:
        return self._group

    @group.setter
    def group(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Group must be a non-empty string.")
        self._group = value.strip()

    @property
    def course(self) -> str:
        return self._course

    @course.setter
    def course(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Course must be a non-empty string.")
        self._course = value.strip()

    def __str__(self):
        return f"Student: \n{super().__str__()}, Group: {self.group}, Course: {self.course}"
