# 문제1) 다음코드가 출력결과 처럼 동작하도록 Car클래스를
# 상속받는Bus클래스를?정의하시오.


class Car:
    def __init__(self, tire, price):
        self.tire = tire
        self.price = price


class Bus(Car):
    def info(self):
        print("버스의 타이어수는 {}개 입니다.".format(self.tire))
        print("버스의 가격은 {}만원입니다.".format(self.price))


bus = Bus(4, 1000)
bus.info()

# < 출력결과 >버스의타이어수는4개입니다.
# 버스의가격은1000만원입니다.

print('======================================================')

# 문제2) 다음코드가출력결과처럼동작하도록Car클래스를상속받는Truck클래스를정의하시오.


class Car:
    def __init__(self, tire, price):
        self.tire = tire
        self.price = price

    def info(self):
        print('타이어수:', self.tire)
        print('가격:', self.price)


class Truck(Car):
    def __init__(self, tire, price, name):
        super().__init__(tire, price)
        self.name = name

    def info(self):
        super().info()
        print("트럭이름 :", self.name)


truck = Truck(6, 5000, '포터')
truck.info()

# < 출력결과 >
# 타이어수: 6
# 가격: 5000
# 트럭이름: 포터