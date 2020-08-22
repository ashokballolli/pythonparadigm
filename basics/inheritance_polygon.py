class Polygon:
    __width = None
    __height = None

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_values(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height


class Triangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height() / 2

class Rectangel(Polygon):
    def area(self):
        return self.get_width() * self.get_height()

triangle = Triangle()
triangle.set_height(100)
triangle.set_width(50)
area = triangle.area()
print(area)

rectangle = Rectangel()
rectangle.set_values(30, 50)
area_rect = rectangle.area()
print(area_rect)
