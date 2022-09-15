import datetime

hundred_days = datetime.timedelta(days=100)
print(datetime.datetime.now() + hundred_days)

print('===========================================')

hundred_after = datetime.datetime.now().replace(hour=9, minute=0, second=0) + datetime.timedelta(days=100)
print(hundred_after)
print("{}/{}/{}".format(hundred_after.year, hundred_after.month, hundred_after.day))