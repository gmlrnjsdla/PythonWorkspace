class Car:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("{}가 달립니다.".format(self.name))


class Truck(Car):
    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity

    def load(self):
        print("{}kg 짐을 실었습니다.".format(self.capacity))


truck1 = Truck('봉고트럭', 1200)

truck1.run()
truck1.load()
