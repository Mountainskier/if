x = 43
print('Здравствуйте')
if x < 0:
    print('Меньше чем 0 ')

print('До свидания')

a, b, c, d = 15, 6, 24, 50
if a > b:
    print('да')
if d >= c:
    print('ессс')
if a > b and a > 0:
    print('оке')
if (a > b) and (a > 0 or b < 1000):
    print('оке')
if (a < c) and (b > 0 or 77 == d):
    print('ноуп')
if 1 < b and c > 4:
    print("оке")
if (c + d) > (a * b):
    print('оке')

# Можно сравнивать
if '48' > '123':
    print('оке')
if '987654' > '123456789':
    print('оке')
if [1, 2, 3, 5] > [1, 2, 3, 4]:
    print('оке')

# Нельзя сравнивать
#  if '6' > 5:
#     print('успех')
# if [5, 6] > 5:
#     print('успех')
# но
if '10' != 99:
    print('оке')
