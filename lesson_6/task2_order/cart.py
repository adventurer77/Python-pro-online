from product import Product
from iter_cart import IterCart

class Cart:
    def __init__(self) -> None:
        self.__items = []
        self.__quantities = []
        # self._index = 0
    
    def add_product(self,item:Product,quantity=1):
        self.__items.append(item)
        self.__quantities.append(quantity)
    
    def __get_item_slice(self, index):
        default_start = 0
        default_stop = len(self.__items) - 1 

        start = index.start or default_start
        stop = index.stop or default_stop
        step = index.step or 1
        result = []

      
        for i in range(start, stop, step):
            item = self.__items[i]
            result.append(item)
        return result

     
    def __get_item(self,index):
            if index < len(self.__items):
                return self.__items[index]
            
            raise IndexError
    
    
    def __getitem__(self, index):
        if isinstance(index, int):
            return self.__get_item(index)
        if isinstance(index, slice):
            return self.__get_item_slice(index)

        raise TypeError
    
    def __len__(self):

        return len(self.__items)
    
    def __iter__(self):
        return  IterCart(self.__items,self.__quantities)
    
    

    def total(self):
        return sum(item.price * quantity for item,quantity in zip(self.__items,self.__quantities))
    
    def __str__(self) -> str:
        items = "\n".join([f"{item.name}:{quantity}" for item,quantity in zip(self.__items,self.__quantities)])
        return f"Cart wirh: \n{items}\nTotal: {self.total()} UAH"
    

    # def __getitem__(self,index):
        
    #     if 0 <= index < len(self.__items):
    #         return self.__items[index]
    #     raise IndexError


    # def __next__(self):

    #     if self._index < len(self.__items):
    #         item1 = self.__items[self._index]
    #         # item2 = self.__quantities[self._index]
    #         self._index += 1
    #         return item1
        
    #     raise StopIteration