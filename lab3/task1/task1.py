# Дана колекція ALPHA на 150 елементів, 
# заповніть її рандомно цілими числами від 1 до 200. 
# Потрібно утворити колекцію BETA з 15 елементів, 
# які є найбільшими в ALPHA. 
# ALPHA змінювати не можна. 
# BETA виведіть в консоль і Файл.
import random

alpha = [random.randint(1, 200) for x in range(150)]
beta = alpha[0:15]
print(alpha)
print (beta)
