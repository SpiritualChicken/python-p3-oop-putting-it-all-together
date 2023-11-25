#!/usr/bin/env python3

class Shoe:
    def __init__ (self, brand, initial_size):
        self.brand = brand 
        self._size = None
        self.size = initial_size
        self.condition = None
    
    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if type(size) is int:
            self._size = size
        else:
            print("size must be an integer")
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
    
    
    size = property(get_size, set_size)
    # cobble = property(repair)

stan_smith = Shoe("Adidas", 9)
stan_smith.cobble()