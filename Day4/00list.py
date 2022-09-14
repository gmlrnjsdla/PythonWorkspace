list1 = {10, 20, 30, 40, 50, 60}

try:
    print(list1.index(140)) #해당 갑의 인덱스를 반환
except:
    print('해당 값은 리스트 안에 없습니다.')

# list1.append(100)  # 한개의 값만 리스트에 추가 가능
# print(list1)
# list1.extend([200, 300, 400])  # 리스트에 리스트 추가
# print(list1)
# list1.insert(2, 150)  # 원하는 인덱스 위치에 새로운 값 추가
# print(list1)

list2 = [50, 40, 30, 100, 10]
list2.sort()  # 오름차순 정렬
print(list2)
list2.reverse()
print(list2)
