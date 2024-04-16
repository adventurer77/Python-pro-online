from product import Product
from buyer import Buyer
from cart import Cart
from order import Order

if __name__ == "__main__":
    try:
        p1 = Product("Coffee table",320,"Table for rest.","Overall size:1000 x 600 x 550 mm")
        # print(p1)
        p2 = Product("Sofa",200,"The best sofa for relaxing.","Overall dimensions:2120x1680x1010")
        p3 = Product("Work table",450,"Table for work.","Overall size:1000 x 700 x 650 mm")


        b1 = Buyer("Sam","Fisher",3245674)
        
        cart = Cart()
        cart.add_product(p1,2)
        cart.add_product(p2,1)
        cart.add_product(p3,2)

        

        for i,q  in cart:  # Sequence protocol.
            print (i,"\n","Quantities:",q)

        # print (len(cart))
        # print(cart[2])   # Iteration protocol.
        


        # order = Order(b1,cart)
        # print(order)

    except IndexError:
        print("Index out of range. Please provide a valid index.")
    except Exception as e:
        print(e)