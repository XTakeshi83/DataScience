import numpy as np


def binary_search(number):
    '''Функция бинарного поиска загаданного числа'''
    count = 1   # счётчик попыток
    pivot = 50  # опорный элемент
    left = 1    # левый предел
    right = 100 # правый предел
    
    while number!=pivot:
        count += 1
        if number>pivot: 
            left = pivot
            delta = right - left
            pivot += delta//2 + delta%2
        elif number<pivot: 
            right = pivot
            delta = right - left
            pivot -= delta//2 + delta%2
            
    return(count) # выход из цикла, если угадали
        
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_list = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы наш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_list.append(game_core(number))
    
    score = int(np.mean(count_list))
    print(f"Мой алгоритм угадывает число в среднем за {score} попыток")
    
    return(score)


score_game(binary_search)