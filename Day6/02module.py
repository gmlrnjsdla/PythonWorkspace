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
