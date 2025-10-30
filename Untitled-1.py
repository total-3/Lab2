for i in range(2, 101, 2):
    print(i)
2
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Факториал числа {n} равен {factorial}")
3
num = 7
for i in range(1, 11):
    print(f"{num} × {i} = {num * i}")
4
number = 12345
sum_digits = 0
for digit in str(number):
    sum_digits += int(digit)
print(f"Сумма цифр числа равна {sum_digits}")
5
number = 987654321
count = 0
for digit in str(abs(number)):
    count += 1
print(f"Количество цифр в числе: {count}")
6
number = 12345
reversed_number = ""
for digit in str(abs(number)):
    reversed_number = digit + reversed_number
print(f"Перевёрнутое число: {reversed_number}")
7
n = 17
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print("Число простое")
else:
    print("Число составное")
8
a = 3
n = 4
result = 1
for _ in range(n):
    result *= a
print(f"{a} в степени {n} равно {result}")
9
height = 5
for i in range(1, height + 1):
    print('*' * i)
10 
n = 10
if n <= 0:
    print("Пожалуйста, введите положительное число.")
elif n == 1:
    print(0)
elif n == 2:
    print(0, 1)
else:
    a, b = 0, 1
    print(a, b, end=' ')
    for _ in range(2, n):
        a, b = b, a + b
        print(b, end=' ')


