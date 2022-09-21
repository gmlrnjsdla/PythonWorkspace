import pandas as pd

ser1 = pd.Series([1, 2, 3, 4], index=['원', '투', '쓰리', '포'])
print(ser1)

print(ser1['투'])

print(ser1[['원','쓰리']])

print(ser1.index)
print(ser1.values)

print('=======================================')

x = pd.Series([3,8,5,9], index=['서울','대구','부산','광주'])
y = pd.Series([2,4,5,1], index=['대구','부산','서울','대전'])

print(x+y)

print('=======================================')

ser2 = [1,24,14,14,1,12,1,26,5]
ser3 = pd.Series(ser2)
print(ser3.unique())    # 중복값 제거하고 출력

dict1 = {'서울':20, '대구':30, '부산':40, '인천':50}
ser4 = pd.Series(dict1)
print(ser4)
