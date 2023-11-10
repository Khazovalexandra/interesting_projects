from math import sqrt
import numpy as np

# min-max-нормализация
x = list(range(1,11))
print(x)

min_x = min(x)
max_x = max(x)

x_normalized_min_max = [round((x_i - min_x)/(max_x - min_x), 2) for x_i in x]
print(x_normalized_min_max)

# нормализация по среднему
mean_x = np.mean(x) # или sum(x)/len(x)

x_normalized_mean = [round((x_i - mean_x)/(max_x - mean_x), 2) for x_i in x]
print(x_normalized_mean)

# нормализация Z-оценки или стандартизация (среднее = 0, дисперсия = 1)
variance_x = sqrt(sum([(x_i - mean_x)**2 for x_i in x])/len(x))

x_standartized = [round((x_i - mean_x)/variance_x, 2) for x_i in x]
print(x_standartized)

# Масштабирование признаков для машинного обучения
# l2 - норма, или евклидова норма, где р=2  
l2_norm = sqrt(sum([x_i**2 for x_i in x]))

x_scaled = [round(x_i/l2_norm, 2) for x_i in x] #применяем норму для каждого элемента списка
print(x_scaled)
# l1 - норма, р=1