import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6])     # numpy 1차원 배열
print(arr1)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

print(arr1.mean())  # 배열 원소의 평균 출력 함수
print(arr1.shape)   # 배열의 형태를 출력
print(arr2.shape)

arr3 = np.array([10, 20, 30, 40, 50, 60])

arr0 = arr3.reshape(2, 3)   # 배열의 형태를 변경
print(arr0)


list1 = [1, 2, 3, 4, 5]
print(list1[2:5])
arr5 = np.array(list1)
print(arr5[2:5])

list2 = [[1, 11], [2, 22], [3, 33]]
print(list2)

print(list2[0:2][0:2])
arr6 = np.array(list2)
print(arr6)
print(arr6[:, 1])

print(np.sqrt(2)) # 제곱근
print(np.sqrt([2,3,4,5]))

list3 = [1,2,3,4,5]
list4 = [6,7,8,9,10]

list5 = list3 + list4
print(list5)

arr7 = np.array(list3)
arr8 = np.array(list4)
arr9 = arr7 + arr8  # 리스트 각 원소의 합으로 리스트를 생성(리스트의 개수가 동일해야함)
print(arr9)
arr10 = arr7 * arr8 # 리스트 각 원소의 곱으로 리스트를 생성
print(arr10)
print(arr7 + 1)

arr11 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr12 = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr11[:,1]+arr12[:,0])

arr13 = np.array([10,20,30,40,50])
i = [0,2,4]
print(arr13[i])

arr14 = np.array(arr13[0:5:2])
print(arr14)

print(arr13>=30)    # numpy배열의 각원소값이 30 이상인지 검사

print(np.random.random(10)*10) # 0부터 1사이의 수중 랜덤 10개 출력

print(np.linspace(0,12,4))


arr15 = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9],
                  [10,11,12],
                  [13,14,15]
                  ])

print(np.sum(arr15, axis = 1))  # axis = 1 은 x축 0은 y축


