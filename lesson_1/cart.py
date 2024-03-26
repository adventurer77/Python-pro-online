from product import Product

class Cart:
    def __init__(self) -> None:
        self.__items = []
        self.__quantities = []
        self._index = 0
    
    def add_product(self,item:Product,quantity=1):
        self.__items.append(item)
        self.__quantities.append(quantity)

    def __iter__(self):
        return self
    
    def __next__(self):

        if self._index < len(self.__items):
            item1 = self.__items[self._index]
            # item2 = self.__quantities[self._index]
            self._index += 1
            return item1
        
        raise StopIteration
    
    def __getitem__(self,index):
        
        if 0 <= index < len(self.__items):
            return self.__items[index]
        raise IndexError
    
    def __len__(self):

        return len(self.__items)
    



    def total(self):
        return sum(item.price * quantity for item,quantity in zip(self.__items,self.__quantities))
    
    def __str__(self) -> str:
        items = "\n".join([f"{item.name}:{quantity}" for item,quantity in zip(self.__items,self.__quantities)])
        return f"Cart wirh: \n{items}\nTotal: {self.total()} UAH"