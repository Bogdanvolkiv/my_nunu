# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, 
# которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. 
# Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()


import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

def one_hot_encode(row): # Функция для перевода в one hot
    if row == 'robot':
        return pd.Series([1, 0], index = ['robot', 'human'])
    elif row == 'human':
        return pd.Series([0, 1], index = ['robot', 'human'])
    
one_hot_encode = data['whoAml'].apply(one_hot_encode) # Применение функции к каждому элементу столбца

result = pd.concat([data, one_hot_encode], axis = 1)  # Объединение исходного DataFrame и one hot encoded данных

print(result.head())



    