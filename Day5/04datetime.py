import datetime

now_time = datetime.datetime.now()

# print(type(now_time))   # datetime 모듈안의 datetime 클래스로 만든 객체(인스턴스)

new_time = now_time.replace(year=2019, month=10, day=25)
print(new_time)
print(now_time)

print('=====================================================')

time1 = datetime.datetime(2022, 8, 25)
# datetime 모듈안의 datetime 클래스로 객체 생성
result_time1 = now_time - time1
print(result_time1)
print(type(result_time1))

print(result_time1.days)
print(result_time1.seconds)

print('우리가 공부를 시작한지 {}일 {}시간 지났습니다.'.format(result_time1.days,result_time1.seconds//60//60))

print('=====================================================')

def days_until_christmas():
    christmas_2022 = datetime.datetime(2022, 12, 25)
    days = (christmas_2022 - datetime.datetime.now()).days
    return days

print("{}일".format(days_until_christmas()))

