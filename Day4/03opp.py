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

class Student:
    name = '홍길동'    #클래스 변수, 멤버 변수, 속성, 필드
    hakbun = '20220111'
    gradeNum = 4
    def pirntName(self):    # 메서드(methods)
        print('학생 이름 : {}'.format(self.name))
        print('학번 : {}'.format(self.hakbun))
        print('학년 : {}'.format(self.gradeNum))

student1 = Student()
student1.name = '김유신'

print(student1.name)
print(student1.hakbun)
print(student1.gradeNum)
student1.pirntName()

#==================================================================

class Circle:
    pi = 3.14

    def circleArea(self, radius):
        area = radius * radius * self.pi
        return area

circle1 = Circle()
print(circle1.circleArea(10))
