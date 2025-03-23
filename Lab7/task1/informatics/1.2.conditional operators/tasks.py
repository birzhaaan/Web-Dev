#1
n = int(input())
m = int(input())
if n>m:
    print(n)
else:
    print(m)

#2
n = int(input())
if (n%4==0) & (n%100!=0) | (n%400==0):
    print("YES")
else:
    print("NO")

#3
n = int(input())
m = int(input())
if ((n==1)&(m==1)|(n!=1)&(m!=1)):
    print("YES")
else:
    print("NO")

#4
n = int(input())
if n>0:
    print(1)
elif n<0:
    print(-1)
else:
    print(0)

#5
n = int(input())
m = int(input())
if n>m:
    print(1)
elif m>n:
    print(2)
else:
    print(0)