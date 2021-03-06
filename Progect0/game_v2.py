"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 5) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    limit_a = 1
    limit_b = 101
    predict = np.random.randint(limit_a, limit_b) # предполагаемое число
    
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
            limit_b = number
            number = np.random.randint(limit_a, limit_b)
            
        elif number < predict:
            predict -= 1
            limit_a = number
            number = np.random.randint(limit_a, limit_b)
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 запусков угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
