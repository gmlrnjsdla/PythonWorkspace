# list1 = [10, 20, 30, 40, 50, 60]
#
# try:
#     print(list1.index(140)) #해당 갑의 인덱스를 반환
# except:
#     print('해당 값은 리스트 안에 없습니다.')
#
# list1.append(100)  # 한개의 값만 리스트에 추가 가능
# print(list1)
# list1.extend([200, 300, 400])  # 리스트에 리스트 추가
# print(list1)
# list1.insert(2, 150)  # 원하는 인덱스 위치에 새로운 값 추가
# print(list1)
#
# list2 = [50, 40, 30, 100, 10]
# list2.sort()  # 오름차순 정렬
# print(list2)
# list2.reverse()
# print(list2)

#===========================================================

# def safe_index(a_list, value):
#     if value in a_list:
#         return a_list.index(value)
#     else:
#         return None
#
# def safe_index2(a_list, value):
#     try:
#         return a_list.index(value)
#     except:
#         return None
#
# list3 = [1, 2, 3, 4, 5]
# val = 3
# index1 = safe_index(list3, val)
# print(index1)
#
# index2 = safe_index2(list3, 6)
# print(index2)

#==============================================================

list1 = [1, 2, 3, 4]
list1.insert(0, 8)  # 첫번째 자리에 '8' 삽입
print(list1)
list1.sort()        # 오름차순
print(list1)
list1.reverse()     # 내림차순
print(list1)
