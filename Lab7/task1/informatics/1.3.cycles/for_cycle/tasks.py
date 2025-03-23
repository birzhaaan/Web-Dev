#1
a = int(input())
b = int(input())
for i in range(a,b+1):
    if i%2==0:
        print(i, end=" ")

#2
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a,b+1):
    if i%d == c:
        print(i, end=" ")

#3
import math
a = int(input())
b = int(input())
for i in range(a,b+1):
    x = math.isqrt(i)
    if x*x == i:
        print(i, end=" ")

#4
x = int(input())
d = int(input())
count = 0
while x>0:
    if x%10 == d:
        count+=1
    x//=10
print(count)

#5
n = int(input())
sum = 0
while n>0:
    sum+=n%10
    n//=10
print(sum)

#6
x = int(input())

if x == 0:
    print(0)
else:
    while x % 10 == 0:  
        x //= 10

    while x > 0:
        print(x % 10, end="")  
        x //= 10  

#7
n = int(input())
x = 2
while x<=n:
    if n%x==0:
        print(x)
        exit()
    x=x+1

#8
n = int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")

#9
n = int(input())
count = 0

for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        count += 2 if i * i != n else 1  

print(count)

#10
print(sum(map(int, (input() for _ in range(100)))))

#11
N = int(input())  
print(sum(int(input()) for _ in range(N)))

#12
print(int(input(), 2))

#13
n = int(input())
count = 0
for _ in range(n):
    if int(input()) == 0:
        count += 1
print(count)