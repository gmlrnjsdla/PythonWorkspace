# list1 = ['사과', '수박', '참외', '배']
#
# print(list1[1:3])  # 인덱스 1부터 3전까지 추출
#
# print(list1[1:len(list1)])
#
# print(list1[:3])
# print(list1[0:3])  # 처음부터 인덱스 3전까지 추출
#
# print(list1[1:4])
# print(list1[1:])  # 동일
#
# print(list1[:])  # 리스트의 모든 원소를 추출

#===========================================================

# rainbow = ["빨", "주", "노", "초", "파", "남", "보"]
# red_colors = rainbow[:3]
# blue_colors = rainbow[4:]
# print(red_colors,blue_colors)

#============================================================

# def substring(s, start, end):
#     return s[start:end]
#
# str = "Hello world"
# between_2_5 = substring(str, 2, 5)
# print(between_2_5)

#==============================================================

# list2 = list(range(10))
# print(list2)
#
# print(list2[4:9])
# print(list2[4:9:2])     # [4, 6, 8]
# print(list2[:9:3])      # [0, 3, 6]
# print(list2[::2])       # [0, 2, 4, 6, 8]

#===============================================================

# list1 = list(range(20))
#
# new_list = list1[5:15:3]    # [5, 8, 11, 14]
# print(new_list)
#
# another_list = list1[5::4]  # [5, 9, 13, 17]
# print(another_list)

#==============================================================

# list4 = [10, 20, 30, 40, 50]
# print(list4[1:3])   # [20, 30]
# del list4[1:3]      # [20, 30] 삭제
# print(list4)        # [10, 40, 50]

#=================================================================

# list5 = [1, 2, 3, 4, 5]
# print(list5[1:3])       # [2, 3]
# list5[1:3] = [10, 20, 30]   # [2, 3] 을 [10, 20, 30]으로 변경
# print(list5)

#=================================================================

list1 = [0, 1, 2, 3, 4, 5]
list1[1:4] = [11, 22, 33]
print(list1)

list2 = [0, 1, 2, 3, 4, 5]
del list2[1:4]
print(list2)

list6 = [10, 25, 30, 25]
print(list6.count(25))      # 리스트안에 25가 몇개?

