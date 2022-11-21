import math
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        instance_str = f"Rectangle(width={self.width}, height={self.height})" 
        return instance_str   

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height        

    def get_area(self):
        return (self.width * self.height)  

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)     

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)  

    def get_picture(self):
        lines = 0
        pict = ''
        while True:
            if self.height > 50 or self.width > 50:
                pict = 'Too big for picture.'
                break
            elif self.height > lines:
                pict += ('*' * self.width) + '\n'
                lines += 1
            else:
                break    
        return pict    

    def get_amount_inside(self, rect2):
        fit_width = math.floor(self.width / rect2.width)
        fit_height = math.floor(self.height / rect2.height)
        fit_total = fit_width * fit_height
        return(fit_total)
    

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side 

    def __str__(self):
        instance_str = f"Square(side={self.width})" 
        return instance_str    

    def set_side(self, side):
        self.width = side
        self.height = side    

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side
