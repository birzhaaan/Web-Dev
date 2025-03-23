#1
def make_bricks(small, big, goal):
    used_big = min(big, goal // 5)  
    remaining = goal - used_big * 5  
    return remaining <= small

#2
def lone_sum(a, b, c):
    if a == b == c:  
        return 0
    if a == b:
        return c
    if a == c:
        return b
    if b == c:
        return a
    return a + b + c

#3
def lucky_sum(a, b, c):
    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return a + b
    return a + b + c

#4
def fix_teen(n):
    if 13 <= n <= 19 and n not in (15, 16):
        return 0
    return n

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

#5
def round10(num):
    return (num + 5) // 10 * 10

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

#6
def close_far(a, b, c):
    close_b = abs(a - b) <= 1
    close_c = abs(a - c) <= 1
    far_b = abs(a - b) >= 2 and abs(b - c) >= 2
    far_c = abs(a - c) >= 2 and abs(b - c) >= 2

    return (close_b and far_c) or (close_c and far_b)

#7
def make_chocolate(small, big, goal):
    max_big = min(big, goal // 5)  
    remaining = goal - max_big * 5  
    if remaining <= small:  
        return remaining
    return -1