

class IterGroup:

    def __init__(self,wrapper):
        
        self.wrapper = wrapper
        self.index = 0

    def __next__(self):

        if self.index < len(self.wrapper):
            self.index += 1
            return self.wrapper[self.index - 1]
        
        raise StopIteration
    
    def __iter__(self):

        return self