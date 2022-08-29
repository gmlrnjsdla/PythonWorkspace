# 삼각형 넓이 계산 함수

width1 = 100 # 삼각형의 밑변
height1 = 50 # 삼각형의 높이

tri_area1 = width1 * height1 * 0.5 # 삼각형의 넓이
print(tri_area1)

width2 = 200
height2 = 200
tri_area2 = width2 * height2 * 0.5 # 삼각형의 넓이
print(tri_area2)

def triArea(width, height):  # 매개변수 입력 //함수는 선언한 후에 호출.
    tri_area = width * height * 0.5
    print(tri_area)
    
triArea(20, 50) # 호출

def rootClacu(a, b, c):
    root1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    root2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print(root1, root2)

rootClacu(1, 2, -8)