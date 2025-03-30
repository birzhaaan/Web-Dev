#1
def hello_name(name):
  return "Hello "+name+"!"

#2
def make_abba(a, b):
  return a+b+b+a

#3
def make_tags(tag, word):
    return f"'<{tag}>{word}</{tag}>'"

#4
def make_out_word(out, word):
    return out[:2] + word + out[2:]

#5
def extra_end(s):
    return s[-2:] * 3

#6
def first_two(str):
  return str[:2]

#7
def first_half(str):
  return str[:len(str)//2]

#8
def without_end(str):
    return str[1:-1]

#9
def combo_string(a, b):
    if len(a) < len(b):
        short, long = a, b
    else:
        short, long = b, a
    return short + long + short

#10
def non_start(a, b):
  return a[1:]+b[1:]

#11
def left2(str):
    return str[2:] + str[:2]