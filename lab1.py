import numpy
import math

# option 10

#first task
# Число делится на 3 тогда, когда сумма его цифр делится на 3. Проверить этот признак на примере заданного трехзначного числа.
n = int(input("Введите трехзначное число\n "))
x=int (n/100)
y=int(((n-(x*100))/10))
z=int(n-(x*100)-(y*10))
print (x,y,z)
if ((x+y+z)%3 ==0):
    print ("делеться без остатка")
else: print("no!")

print("/////////////////")
#second task

k=(4, 9, 0.5)
f=3.2+(10**4)
s=7.2
m=10
for j in range(len(k)):
     y=(s / numpy.math.log  (5.2 * f) / (numpy.e ** ((-s)) + 2))
     v=(1+m*y-m*k[j])*numpy.math.log(y)
     print(v)

print("/////////////////")


k=0
while k<=4 :
    y = (s / numpy.math.log(5.2 * f) / (numpy.e ** ((-s)) + 2))
    a = (1 + m * y - m * k) * numpy.math.log(y)
    k+=0.5
    print(a)


print("/////////////////")

k=(0.9,12,0.5)
m=0.3
for j in range(len(k)):
    while m<=0.7:
        y = (s / numpy.math.log(5.2 * f) / (numpy.e ** ((-s)) + 2))
        b = (1 + m * y - m * k[j]) * numpy.math.log(y)
        m+=0.1
        print(b)

