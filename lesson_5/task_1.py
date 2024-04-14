class Rectangle:

    def __init__(self,width,height):

        if not isinstance(width, int|float):
            raise TypeError('width must be an integer')
        if not isinstance(height, int|float):
            raise TypeError('height must be an integer')
        if width == 0 or height == 0:
            raise ZeroDivisionError('width or height must not be zero')
        if width < 0 or height < 0:
            raise ValueError('width or height must be positive')


        self.width = width 
        self.height = height


    def area(self):
        return self.width * self.height
    
    def __add__(self,other):
        if not isinstance(other, Rectangle):
            raise TypeError("Can only combine with another Cart")

        return Rectangle(1, self.area() + other.area())
    
    def __mul__(self, other):
        if isinstance(other, Rectangle):
            raise TypeError("Can only combine with another Rectangle")
 
        return self.area() * other
        
    def __eq__(self, other) -> bool:

        if isinstance(other, Rectangle):
            raise TypeError("Can only combine with another Rectangle")

        return self.area() == other.area() 
    
    def __str__(self) -> str:

        return f" Width:{self.width} and Height:{self.height} = Area: {self.area()}"


if __name__ == '__main__':
    try:
        test1 = Rectangle(7,2)

        test2 = Rectangle(4,2)

        test3 = Rectangle(4,2)
        test4 = Rectangle(3,2)


        new_res = test1 + test2
        print(new_res)

        res = test4 * 3
        print(res)

        print(f"Comparison results :{test3 == test2}")
    
    except Exception as e:
        print(e)
