#1
if __name__ == '__main__':
    print("Hello, World!")

#2
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2==1:
        print("Weird")
    elif n%2==0:
        if n>=2 and n<=5 or n>20:
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
    

#3
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

#4
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#5
if __name__ == '__main__':
    n = int(input())
    for i in range(0,n+1):
        if i*i<n*n:
            print(i*i)

#6
def is_leap(year):
    leap = False
    
    if year%4==0 and year%100!=0 or year%400==0:
        leap=True
    
    return leap

year = int(input())
print(is_leap(year))

#7
if __name__ == '__main__':
    n = int(input())
    output = ""
    for i in range(1,n+1):
        output+=str(i)
    print(output)

#8
n = int(input())
arr1 = set(map(int, input().split()))  
m = int(input())
arr2 = set(map(int, input().split()))  
union_set = arr1.union(arr2)  
print(len(union_set)) 

#9
n = int(input().strip())  
arr1 = set(map(int, input().split()))  
m = int(input().strip())  
arr2 = set(map(int, input().split()))  
intersection_set = arr1.intersection(arr2)  
print(len(intersection_set))  

#10
if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))  
    arr2 = sorted(arr) 
    print(arr2[-2])  