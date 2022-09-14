class Figure:
    def areaCalcu(self):
        pass

class Square(Figure):
    def __init__(self, width, height):
        self.width = width
        self.heigh = height

    def areaCalcu(self):                # 오버라이딩
        area = self.width * self.heigh
        return area

class Triangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.heigh = height

    def areaCalcu(self):                # 오버라이딩
        area = self.width * self.heigh * 0.5
        return area

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def areaCalcu(self):                # 오버라이딩
        area = self.radius * self.radius * 3.14
        return area


square1 = Square(10,20)
triangle1 = Triangle(20, 40)
circle1 = Circle(10)


print(square1.areaCalcu())
print(triangle1.areaCalcu())
print(circle1.areaCalcu())
