# 한변의 길이가 1~10 인 정사각형의 넓이를 원소로 가지는 리스트를 만드시오

areas = []                          # 빈 리스트 선언
for i in range(1, 11):              # range(1, 11) ->[1,2,3,4,5,6,7,8,9,10]
    # areas = areas + [i * i]
    area = i * i
    areas.append(area)

print(areas)
print('=======================================')

#===================================================

areas2 = [i * i for i in range(1, 11)]
print(areas2)