'''Игра угадай число'''
'''компьютер будет сам угадывать число'''

import numpy as np

def number_predict(number: int=1) -> int:
    
    '''Указываем в аргументе функции через двоеточие тип данных,
    Стрелочкой указываем что у нас на выходе'''
    
    '''Рандомно подбираем чсло'''
    count = 0
    
    while True:
        count += 1
        num_predict = np.random.randint(1,200) # Предполагаемое число
        if number == num_predict:
            break
    
    return(count)
def scor_count(number) -> int:
    """За Сколько в среднем угадывает 
    Args:
        number ([type]): функция угадывания 
    Returns:
        int: среднее колличество попыток 
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для вопроизводимости
    random_array = np.random.randint(1,101,size=(1000)) # загадали список oдинаковых чисел
    
    for number in random_array: 
        count_ls.append(number_predict(number))
    
    score = int(np.mean(count_ls)) # берём среднее арефмет. из чисел в списке count_ls (в списке числа, каждое - это число попыток)
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)
    
# RUN
if __name__ == '__main__':
    scor_count(number_predict)
    
