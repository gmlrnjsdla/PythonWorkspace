# 삼각형 클래스 만들기
# 초기값으로 밑변, 높이를 입력해서 인스턴스를 생성
# 삼각형의 면적을 출력하는 메서드가 존재
# 인스턴스를 2개 생성하고 각각 밑변 10, 높이 20
# 밑변 20, 높이 40 인 삼각형의 면적을 출력하시오.

class Triangle:
    def __init__(self, width, height):
        print('밑변 : {}'.format(width))
        print('높이 : {}'.format(height))
        self.width = width
        self.height = height

    def tri_area(self):
        tri_area = self.width * self.height * 0.5
        return tri_area

area1 = Triangle(10, 20)
print(area1.tri_area())
area2 = Triangle(20, 40)
print(area2.tri_area())

#==========================================================================
print('========================================')
# 사칙연산 클래스 만들기
# 두 개의 수를 초기값으로 입력하여 인스턴스 생성
# 사칙연산을 하는 메서드 4개 생성
# 20, 10 의 사칙연산 결과를 출력하도록 프로그램 작성

class Calculator:
    def __init__(self, a, b):
        print('두개의 수 입력: {} {}'.format(a, b))
        self.a = a
        self.b = b

    def sum(self):
        sum = self.a + self.b
        return sum

    def minus(self):
        minus = self.a - self.b
        return minus

    def mul(self):
        mul = self.a * self.b
        return mul

    def divide(self):
        div = self.a / self.b
        return div

cal1 = Calculator(20, 10)
print(cal1.sum())
print(cal1.minus())
print(cal1.mul())
print(cal1.divide())

print('=====================================================')
#=======================================================

# 자식 클래스 만들기 (부모는 Calculator 클래스)
class SubCalculator(Calculator):
    def power(self):
        return self.a ** self.b

sub1 = SubCalculator(20, 10)
print(sub1.sum())
sub2 = SubCalculator(10, 2)
print(sub2.power())

print('===============================================')
#=========================================================

class Car:
    def run(self):
        print('차가 달립니다.')

class Truck(Car):
    def __init__(self, weight):
        self.weight = weight

    def load(self):
        print('{}kg 짐을 실었습니다.'.format(self.weight))

    def run(self):
        print('트럭이 달립니다.')

class SportCar(Car):
    pass

truck1 = Truck(200)
truck1.run()
truck1.load()

print('===============================================')
sportCar1 = SportCar()
sportCar1.run()
