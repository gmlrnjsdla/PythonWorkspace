class Shape:
    def __init__(self, num1, num2):  # 초기화자, 생성자 -> 객체를 생성할 때 자동실행 메서드
        print('초기화자 호출!!')
        self.width = num1
        self.height = num2
    # width = 100
    # height = 200        # 클래스 변수, 멤버 변수, 속성, 필드

    def area(self):
        area = self.width * self.height
        print('면적 : {}'.format(area))

    def test(self):
        print('부모 클래스의 test 메서드 입니다.')

# shape1 = Shape(10, 20)        # 클래스로 객체(인스턴스)를 생성
# print(shape1.width)
# print(shape1.height)
# shape1.area()
#
# shape2 = Shape(30, 40)
# print(shape1.width)
# print(shape1.height)
# shape2.area()

class Square(Shape):        # Shape 클래스에서 상속받는 클래스로 선언
    def subArea(self):
        print('자식클래스의 메서드 호출')
        sum = self.width + self.height
        print(sum)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def circleArea(self):
        area = self.radius * self.radius * 3.14
        print(area)

    def area(self):
        print('부모 클래스의 area 메서드를 오버라이딩 하였습니다.')

    def test(self):
        print('자식의 test 메서드로 오버라이드 하였습니다.')
        super().test()  # 부모의 test 메서드를 호출

class Triangle(Shape):
    def tri(self):
        print('저는 삼각형입니다.')

tri1 = Triangle(10, 20)
tri1.area()
# square1 = Square(50, 60)
# square1.area()
# square1.subArea()
# circle1 = Circle(10)
# circle1.circleArea()
# circle1.area()
# circle1.test()