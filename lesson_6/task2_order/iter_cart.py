
class IterCart:

    def __init__(self, cart_item, cart_quantities):
       
       self.cart_item = cart_item
       self.cart_quantities = cart_quantities
       self.index = 0
    
    # def __next__(self):

    #     if self.index < len(self.cart_item):
    #         item1 = self.cart_item[self.index]
    #         # item2 = self.__quantities[self._index]
    #         self.index += 1
    #         return item1
        
    #     raise StopIteration
    
    def __next__(self):

        if self.index < len(self.cart_item):
            index = self.index
            self.index += 1
            return self.cart_item[index], self.cart_quantities[index]
        
        raise StopIteration
    

    def __iter__(self):
        return self
    