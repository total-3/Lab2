import random

secret_number = random.randint(1, 10)  # Загадываем число (например, 7)
guess = None  # Инициализируем переменную

while guess != secret_number:
    guess = int(input("Угадайте число от 1 до 10: "))  # Ввод: 3 → 5 → 7
    if guess < secret_number:
        print("Слишком мало, попробуйте ещё раз!")
    elif guess > secret_number:
        print("Слишком много, попробуйте ещё раз!")
    else:
        print(f"Правильно! Загаданное число — {secret_number}.")
2
total = 0
number = int(input("Введите число (0 для завершения): "))  # Ввод: 5 → 10 → -3 → 0

while number != 0:
    total += number
    number = int(input("Введите число (0 для завершения): "))

print(f"Сумма всех введённых чисел: {total}")  # Вывод: 12
3
password = "12345"
user_input = ""

while user_input != password:
    user_input = input("Введите пароль: ")  # Ввод: "111" → "12345"
    if user_input != password:
        print("Неверный пароль, попробуйте ещё раз.")

print("Пароль принят!")
4
balance = 1000

while balance > 0:
    print(f"Ваш баланс: {balance} руб.")
    withdrawal = int(input("Сколько хотите снять? "))  # Ввод: 200 → 500 → 400

    if withdrawal > balance:
        print("Недостаточно средств!")
    else:
        balance -= withdrawal
        print(f"Вы сняли {withdrawal} руб. Остаток: {balance} руб.")

print("Счёт опустошён!")
5
while True:
    num1 = float(input("Первое число: "))      # Ввод: 8.5
    num2 = float(input("Второе число: "))       # Ввод: 1.5
    op = input("Операция (+, -, *, /): ")        # Ввод: "+"

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Ошибка: деление на ноль!")
            continue
        result = num1 / num2
    else:
        print("Неверная операция!")
        continue

    print(f"Результат: {result}")  # 8.5 + 1.5 = 10.0

    again = input("Продолжить? (да/нет): ")
    if again.lower() != "да":
        break

print("Калькулятор завершён.")
6
a = int(input("Первое число: "))  # Ввод: 48
b = int(input("Второе число: "))  # Ввод: 18

while b != 0:
    a, b = b, a % b  # 48,18 → 18,12 → 12,6 → 6,0

print(f"НОД равен {a}")  # Вывод: 6
7
total = 0
count = 0

while True:
    num = float(input("Число (0 для завершения): "))  # 10 → 20 → 30 → 0
    if num == 0:
        break
    total += num
    count += 1

if count > 0:
    average = total / count
    print(f"Среднее арифметическое: {average}")  # (10+20+30)/3 = 20.0
else:
    print("Числа не введены.")
8
number = abs(int(input("Введите число: ")))  # Ввод: -5382 → 5382
min_digit = 9

while number > 0:
    digit = number % 10     # 2 → 8 → 3 → 5
    if digit < min_digit:
        min_digit = digit  # min_digit: 2
    number //= 10

print(f"Наименьшая цифра: {min_digit}")  # Вывод: 2
9
number = int(input("Введите число: "))  # Ввод: 121
original = number
reversed_num = 0

while number > 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit  # 1 → 12 → 121
    number //= 10

if original == reversed_num:
    print("Число — палиндром.")
else:
    print("Число не палиндром.")
