def add(a, b):
    result = a + b
    print('{} + {} = {}'.format(a,b, result))


a = 10
b = 20
print('나는 {}살 입니다. 너는 {}살 입니다.'.format(a, b))

print(f'나는 {a+b}살 입니다. 너는 {b}살 입니다.') #유용하다..

print(f'{a} + {b} = {a+b}')

add(a, b)