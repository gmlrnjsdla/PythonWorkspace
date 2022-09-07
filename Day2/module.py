import math
import random


# print(math.pi)  # 파이값 (소수점 15자리)
# area = 10*10*math.pi  # 원의 면적
# print(area)
# print(math.floor(area))

gameNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

user = input('"low" 또는 "high"를 입력하세요: ')

com = random.choice(gameNumber)
# gameNumber 리스트에 있는 값들 중 랜덤으로 숫자 선택

if com >= 5:
    gameState = 'high'
else:
    gameState = 'low'

print('컴퓨터가 선택한 숫자는 {}입니다.'.format(com))
if user == gameState:
    print('정답')
else:
    print('실패')

