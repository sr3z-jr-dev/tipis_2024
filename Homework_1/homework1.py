import pandas as pd
import numpy as np


# СПИСОК ОТВЕТОВ В КОНЦЕ ФАЙЛА !!

url = "https://raw.githubusercontent.com/Yorko/mlcourse.ai/main/data/"
data = pd.read_csv(url + "adult.data.csv")

# task 1
print(data.head)
print("\n################### [ ВОПРОС №1 ] ###################")
print("Число столбцов в наборе данных: ", len(data.columns)) # --------> 15

#task 2
print("\n################### [ ВОПРОС №2 ] ###################")
missing_data = data.isnull().sum().sum ()
print(f"Пропуски в данных: {missing_data}") # --------> 0

#task 3
print("\n################### [ ВОПРОС №3 ] ###################")
unique_race_count = data['race'].nunique()
print("Количество уникальных значений в столбце 'race':", unique_race_count) # --------> 5

#task 4
print("\n################### [ ВОПРОС №4 ] ###################")
median_hours_per_week = data['hours-per-week'].median()
print("Медиана значений в столбце 'hours-per-week':", median_hours_per_week) # --------> 40.0

#task 5
print("\n################### [ ВОПРОС №5 ] ###################")
salary_check = data['salary'] == '>50K'
male_count = data[salary_check]['sex'].value_counts()['Male']
female_count = data[salary_check]['sex'].value_counts()['Female']

if male_count > female_count:
     print("Male")
elif male_count < female_count:
     print("Female")
else:
     print("M = F") # --------> Male

#task 6
print("\n################### [ ВОПРОС №6 ] ###################")
for column in data.columns:
    most_common_value = data[column].mode()[0]
    data[column] = data[column].fillna(most_common_value)

missing_data_after = data.isnull().sum()
if missing_data_after.sum() == 0:
    print("Все пропущенные данные успешно заполнены.")
else:
    print(f"Остались пропуски:\n{missing_data_after[missing_data_after > 0]}")



"""
ОТВЕТЫ:
1) 15
2) 0
3) 5
4) 40.0
5) Male
6) Другие методы заполнения пропусков:
     * Средним значением
     * Медианой
     * Метод интерполяции
     * Заполнение специальными значениями (например, "Unknown", 0, -1)
     * Удаление строк или столбцов с пропусками
     * Алгоритмы машинного обучения

"""