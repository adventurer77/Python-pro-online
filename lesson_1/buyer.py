class Buyer:
    def __init__(self,first_name,second_name,phone_number):
        self.first_name = first_name
        self.second_name = second_name
        self.phone_number = phone_number

    def __str__(self):
        return f"Name: {self.first_name}\nSurname: {self.second_name}\nPhone namber: {self.phone_number}"
        