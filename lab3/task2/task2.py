# Побудувати три класи (базовий і 2 нащадка),
# що описують деяких працівників з погодинною оплатою (один з нащадків) 
# і фіксованою оплатою (другий нащадок). Описати в базовому класі 
# абстрактний метод для розрахунку середньомісячної заробітної плати. 
# Для «почасових» формула для розрахунку така: 
#     «середньомісячна заробітна плата = 20.8 * 8 * погодинну ставку», 
#     для працівників з фіксованою оплатою «середньомісячна заробітна 
#     плата = фіксованою місячної оплати».
#     a) Упорядкувати всю послідовність працівників по спадаючій середньомісячного заробітку. 
#         При збігу зарплати - упорядковувати дані за алфавітом по імені. 
#         Вивести ідентифікатор працівника, ім'я та середньомісячний заробіток 
#         для всіх елементів списку.
#     b) Вивести перші 5 імен працівників з отриманого в пункті а) списку.
#     c) Вивести останні 3 ідентифікатора працівників з отриманого в пункті а) списку.
#     d) Організувати запис і читання колекції у / з файл.
#     e) Організувати обробку некоректного формату вхідного файлу.
import random as rd
import csv
f = open('out.csv', 'w')
class employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def monthlySalary(self):
        raise NotImplementedError

    def typeName(self):
        return self.__class__.__name__


class employeeFixed(employee):
    def __init__(self, id, name, wage):
        self.wage = wage
        super().__init__(id, name)

    def monthlySalary(self):
        return self.wage


class employeeHourly(employee):
    def __init__(self, id, name, wage):
        self.wage = wage
        super().__init__(id, name)

    def monthlySalary(self):
        return self.wage * 8 * 20.8

names = ['Vova', 'Ania', 'Jek', 'Bill', 'Stiv', 'Li', 'Misha', 'Li', 'Jek', 'Bill']

a = [employeeFixed(x, names[x], rd.randint(1700, 2000)) for x in range(5)]
b = [employeeHourly(x, names[x], rd.randint(10, 12)) for x in range(5, 10)]
c = a.copy()
c.extend(b)
c.sort(key = lambda x: (-x.monthlySalary(), x.name))
print('a)')
for x in c:
    print(x.id, x.name, x.monthlySalary())
print('b)')
for y in c[:5]:
    print(y.name)
print('c)')
for y in c[-3:]:
    print(y.id)
fieldnames = ['id', 'type', 'name', 'wage']

out = csv.DictWriter(f, fieldnames = fieldnames)
out.writeheader()
for i in c:
    a = {'id': i.id, 'type': i.typeName() , 'name': i.name, 'wage': i.wage }
    out.writerow(a)
f.close()
a = ''
f = open('out.csv', 'r')
input = csv.DictReader(f)
d = []
try:
    for x in input:
        if  x['type'] == 'employeeFixed':
            a = employeeFixed(int(x['id']), x['name'], int(x['wage']))
        elif x['type'] == 'employeeHourly':
            a = employeeHourly(int(x['id']), x['name'], int(x['wage']))
        d.append(a)
except:
    print("Uncorrect file")
f.close()