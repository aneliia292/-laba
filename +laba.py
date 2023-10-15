#1
a = int(input("Введите число: "))
k = 0
for i in range(2, a // 2+1):
    if (a % i == 0):
        k = k+1
if (k <= 0):
    print("Число простое")
else:
    print("Число не является простым")

#2
c = [4,7,6,2,9,3,2]
a = 1
while a < len(c):
    for i in range(len(c)-a):
        if c[i] > c[i+1]:
            c[i],c[i+1] = c[i+1],c[i]
    a += 1
print(c)


#3
def large(arr):
    max_ = arr[0]
    for ele in arr:
        if ele > max_:
           max_ = ele
    return max_


list1 = [7,4,9,34,8,99]
result = large(list1)
print(result)

#4
fib1 = fib2 = 1

n = input ("Номер элемента ряда Фибоначчи: ")
n = int (n) - 2

while n > 0:
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1

print ("Значение этого элемента:", fib2)

#5
a = ['erhgwe', 'wqegikm', 'erhgwe']
b = 0
c = 0
for i in a:
    if a.count (i) >= b:
        b = a.count (i)
c = i
print (c)


