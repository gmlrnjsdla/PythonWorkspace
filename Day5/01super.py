class Car():

    def __init__(self, name):
        self.name = name

    def run(self):
        print("차가 달립니다.")

class Truck(Car):
# 다음 줄에 __init__ 메서드를 오버라이드하세요.
    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity
    def load(self):
        print("{}톤 짐을 실었습니다.".format(self.capacity))

truck1 = Truck('이름',8)
truck1.load()
