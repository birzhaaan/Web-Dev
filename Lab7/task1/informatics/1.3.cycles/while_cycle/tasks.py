#1
n = int(input())
x = 1
while x<=n:
    if x*x<=n:
        print(x*x)
    x=x+1

#2
n = int(input())
x = 2
while x<=n:
    if n%x==0:
        print(x)
        exit()
    x=x+1

#3
n = int(input())
x = 0
while x<=n:
    if pow(2,x) <= n:
        print(pow(2,x), end=" ")
    x=x+1

#4
n = int(input())
while n%2==0:
    n/=2
if n==1:
    print("YES")
else:
    print("NO")

#5
n = int(input())
k = 0
power = 1  
while power < n:
    power <<= 1 
    k += 1
print(k)