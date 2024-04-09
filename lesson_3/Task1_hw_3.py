
class UserExceptiion(Exception):
    """
    A custom exception class raised for invalid product price input.

    This exception is raised when the user enters a price that does not meet the
    criteria for a valid product price. For example, the price might be non-numeric
    or negative.

    Attributes:
        message (str): The error message associated with the exception.
    """

    def __init__(self, message):
        """
        Initializes a `UserExceptiion` object with an error message.

        Args:
            message (str): The error message to be associated with the exception.
        """

        super().__init__()
        self.message = message

    def __str__(self) -> str:
        """
        Returns the error message associated with the exception.

        Returns:
            str: The error message.
        """

        return self.message
    

class PriceFilter:
    """
    This class validates and stores product prices.

    Args:
        my_price (int | float): The product price to be validated.

    Raises:
        TypeError: If the provided price is not a numerical value.
        UserExceptiion: If the provided price is not a valid positive number.

    Attributes:
        my_price (int | float): The validated and stored product price.
    """

    def __init__(self,my_price):
        """
        Initializes a `PriceFilter` object with a validated product price.

        Args:
            my_price (int | float): The product price to be validated.

        Raises:
            TypeError: If the provided price is not a numerical value.
            UserExceptiion: If the provided price is not a valid positive number.
        """

        if not isinstance(my_price,(int, float)):
            raise TypeError("Price must be a number.")
        if my_price <= 0:
            raise UserExceptiion("The price cannot be negative or Zero")
        
        self.my_price = my_price
        
    
    def __str__(self) -> str:
        """
        Returns a string representation of the product price.

        Returns:
            str: The price as a string.
        """

        return f"{self.my_price}"
    

if __name__ == "__main__":
    try:
        test1 = PriceFilter(32)
        print(test1)
        test2 = PriceFilter(-2)
        print(test2)
        # test3 = PriceFilter("f")
        # print(test3)
        
    except UserExceptiion as ue:
        print(ue)
    except Exception as e:
        print(e)
     

