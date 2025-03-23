#1
def function(a, b, c, d):
    return min(a,b,c,d)

a, b, c, d = map(int, input().split())
print(function(a, b, c, d))

#2
def power(a, n):
    return pow(a, n)

a, b = map(float, input().split())
print(power(a, int(b)))

#3
def xor(a,b):
    return a^b

a, b = map(int, input().split())
print(xor(a,b))