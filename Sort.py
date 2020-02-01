# 6. Функция сортировки выбором select:
# Цикл 1 – по i от 0 до N-1 :		# i - счетчик прохода по списку
# 	Действие – объявление переменной m = i;	# m - номер для мин. из неотсортированных
# 	Цикл 2 – по j от i до N :		# j - счетчик позиции при проходе по неотсортированной части
# 		Условие если A[j]<A[m] :	 # сравнение текущего элемента с текущим минимальным
# 			Действие – запоминаем номер обнаруженного нового минимального эл-та m = j
# 	Действие – перестановка местами A[m] и A[i]

import random
import datetime
import prettytable                  # пакет для таблицы
import matplotlib.pyplot as plt     # библиотека для графика


def BubbleSort(A):                  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                a = A[j]
                A[j] = A[j+1]
                A[j+1] = a

def selectSort(A):
    for i in range(0, N-1):
        min=i
        for j in range(i,N):
            if A[j] < A[min]:
             min = j
        A[i],A[min]=A[min],A[i]


table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время Select сортировки"])
x=[]
y1=[]
y2=[]


for N in range(1000,5001,1000):
    x.append(N)
    min=1
    max=N
    A=[]
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))


   # print(A)
    B = A.copy()
    print(B)

    BubbleSort(A)
    print("---")
   # print(A)


    selectSort(B)
    print("---")
  #  print(B)

    t1 = datetime.datetime.now()
    selectSort(B)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Пузырьковая сортировка   " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")




    t3 = datetime.datetime.now()
    selectSort(B)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Select сортировка   " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")

    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C2")
plt.show()