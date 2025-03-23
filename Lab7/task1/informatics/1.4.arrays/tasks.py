#1
n = int(input())  
arr = list(map(int, input().split()))  
print(*arr[::2])  

#2
n = int(input())
arr = list(map(int,input().split()))
for a in arr:
    if a%2==0:
        print(a, end=" ")

#3
n = int(input())
arr = list(map(int,input().split()))
count = 0
for a in arr:
    if a>0:
        count+=1
print(count)

#4
n = int(input())
arr = list(map(int, input().split()))
count = 0
for i in range(1, n):
    if arr[i] > arr[i - 1]:
        count += 1  
print(count)

#5
n = int(input())
arr = list(map(int, input().split()))
found = False
for i in range(1, n):
    if (arr[i] > 0 and arr[i - 1] > 0) or (arr[i] < 0 and arr[i - 1] < 0):
        found = True
        break 
if found:
    print("YES")
else:
    print("NO")

#6
n = int(input())
arr = list(map(int, input().split()))
count = 0
for i in range(1, n - 1):
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:  
        count += 1
print(count)

#7
n = int(input())
arr = list(map(int, input().split()))
for i in range(n-1, -1, -1):
    print(arr[i],end = " ")