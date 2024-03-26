from cart import Cart
from buyer import Buyer


class Order:
    def __init__(self,buyer:Buyer,cart:Cart):
        self.cart = cart
        self.buyer = buyer

    
    def __str__(self):
        return f"Order:\n{self.buyer}\n {self.cart}"
    


