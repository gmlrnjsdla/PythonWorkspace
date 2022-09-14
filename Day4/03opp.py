# 삼각형1

# width = 10      # 삼각형의 밑변
# height = 29     # 삼각형의 높이
# color = 'red'   # 삼각형의 면 색깔


# 삼각형2

# width2 = 30      # 삼각형의 밑변
# height2 = 40     # 삼각형의 높이
# color2 = 'blue'   # 삼각형의 면 색깔


# 함수

# def student(name):
#     print(name)
#
# student('홍길동')

#===================================================================

# class Student:
#     name = '홍길동'    #클래스 변수, 멤버 변수, 속성, 필드
#     hakbun = '20220111'
#     gradeNum = 4
#     def pirntName(self):    # 메서드(methods)
#         print('학생 이름 : {}'.format(self.name))
#         print('학번 : {}'.format(self.hakbun))
#         print('학년 : {}'.format(self.gradeNum))
#
# student1 = Student()
# student1.name = '김유신'
# student2 = Student()
#
# student1.pirntName()
# student2.pirntName()

#==================================================================

class Circle:

    def __init__(self, radius, pi):  # 자동으로 실행/ 초기화자/ 초기값설정용 메서드
        print('반지름 초기값 입력: {}'.format(radius))
        self.radius = radius
        self.pi = pi

    def circleArea(self):
        area = self.radius * self.radius * self.pi
        return area

circle1 = Circle(10, 3.14)
print(circle1.radius)
print(circle1.circleArea())

#==================================================================

# 생성자(Constructor), 초기화자
class Car:
    def __init__(self):     # 초기화자(생성사)
        print('초기화자 메서드가 호출됨')

car = Car()     # Car 클래스로 car 인스턴스 생성
