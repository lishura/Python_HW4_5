
# Задание №2
# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.


from random import randint
import sys

__all__ = ['guess_number']
def guess_number(low:int=0, up:int=100, counter:int=10)->bool:
    guess = randint(low, up)
    for _ in range(counter):
        number = int(input("Введите число: "))
        if number < guess:
            print("Загаданное число больше")
        elif number > guess:
            print("Загаданное число меньше")
        else:
            print("Поздравляю Вы угадали!")
            return True
    print("Увы, Вы не угадали. Попытки кончились")
    return False

# if __name__ == '__main__':
#     guess_number()

# Задание №3 Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

if __name__ == '__main__':
    param = sys.argv[1:]
    guess_number(*(int(item) for item in param))

