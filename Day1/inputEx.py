print('원의 면적을 구하는 프로그램입니다.')
print('원의 반지름을 입력해주세요.: ', end='')

input_r = input()  # 반지름을 문자열로 입력받음

def circleArea(r):
    reslut = r ** 2 * 3.14
    return reslut  # 반지름 r인 원의 면적을 반환

area = circleArea(int(input_r))  # 형변환 해줘야 한다.! input 은 문자열로 받기때문!
print('입력하신 반지름 {}인 원의 넓이는 {}입니다.'.format(input_r,area))

#숙제1
#사용자가 입력한 수가 짝수인지 홀수인지 판별하여 '홀수' 또는 '짝수'라고 출력하는
# 프로그램을 작성하시오


#숙제2
#사용자가 입력한 점수를 판별하여 수우미양가 중
#1개를 출력하는 프로그램 작성.