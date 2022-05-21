class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_amount_inside(self, sq):
        return int(Rectangle.get_area(self) / sq.get_area())

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            result = ''
            for i in range(self.height):
                result += '*' * self.width + '\n'
            return result

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side=0):
        Square.set_side(self, side)

    def set_side(self, side=0):
        Rectangle.set_width(self, side)
        Rectangle.set_height(self, side)

    def __str__(self):
        return f'Square(side={self.width})'
