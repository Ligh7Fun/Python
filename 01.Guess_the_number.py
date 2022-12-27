import random

user_name = input("Привет. Как тебя зовут? ")

numbers = random.randint(1, 20)

attempts = 0

print(f"{user_name}, я загадываю число от 1 до 20, угадай какое за 6 попыток.")
for _ in range(6):
    attempts += 1
    user_answer = int(input("Введи число: "))
    if user_answer == numbers:
        print(
            f"{user_name}, тебе потребовалось {attempts} попыток! Я загадал число {numbers}")
        break
    elif user_answer > numbers:
        print("Твое число слишком большое, попробуй ещё раз.")
    else:
        print("Твое число слишком маленькое, попробуй ещё раз.")
if attempts == 6:
    print(f"Ты проиграл :(\nЯ загадывал число {numbers}")
