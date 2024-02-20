"""Загадываем число от 1 до заданного нами т и компьютер сам должен его угадать"""
import numpy as np


def binary_predict(start_number=1, finish_number=100) -> int:
    """Функция выдает число в качестве попытки угадать

    Args:
        start_number (int, optional): Минимальное число. Defaults to 1.
        finish_number (int, optional): Максимальное число. Defaults to 100.

    Returns:
        int: Предсказание
    """
   
    if finish_number - start_number == 2:
        if start_number == 1:
            result = finish_number - 1
        else:
            result = start_number + 1
    elif finish_number - start_number == 1:
        if start_number == 1:
            result = start_number
        else:
            result = finish_number
    else:
         # Возвращаем среднее значение в интервале, округленное до целого
        result = (start_number + finish_number) // 2
    return result


def puzzle(start_number=1, finish_number=100) -> int:
    """Загадывает число в заданном диаапазоне

    Args:
        start_number (int): Начало интервала Defaults to 1
        finish_number (int): Конец интервала Defaults to 100

    Returns:
        int: Загаданное число
    """
    # np.random.seed(100) 
    random_number = np.random.randint(start_number, finish_number+1)
    return random_number


def puzzle_answer(start_number=1, finish_number=100):
    """AI is creating summary for puzzle_answer

    Args:
        start_number (int): начало интервала, в котором будет загадано число Defaults to 1
        finish_number (int): конец интервала Defaults to 1

    Returns:
        [int]: возвращает количество попыток которые затрачены на поиск загаданного числа
    """
    count = 0 # Задаем переменную, где буем хранить количество попыток
    puzzle_number = puzzle(start_number, finish_number) # Задаем загаданное число
    while True:
        count += 1
        answer = binary_predict(start_number, finish_number)
        if answer > puzzle_number:
            finish_number = answer
        elif answer < puzzle_number:
            start_number = answer
        else:
            break
    return count
        
    
    
if __name__ == '__main__':
    print(f'Моя функция угадывает число за {puzzle_answer()} попыток')
    # Для оценки результата выведем среднее количество попыток за 1000 повторений
    count = []
    for i in range(1000):
        count.append(puzzle_answer())
    average_count = np.average(count)
    print(f'За {len(count)} повторейний в среднем затрачивается {average_count} попыток')
        
