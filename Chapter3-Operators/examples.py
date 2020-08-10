# -*- coding: utf-8 -*-
# Arithmetic Operators
a = 10
b = 5

print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b)
print('a ** b =', a ** b)
print('a // b =', a // b)
print('a % b =', a % b)

# Assignment Operators
# let us assign `c`, `d`, `e`, `f`, `g`, `h`, `i` all to 10
c = d = e = f = g = h = i = 10

c += 2
print('c += 2, c is', c)

d -= 2
print('d -= 2, d is', d)

e *= 2
print('e *= 2, e is', e)

f /= 2
print('f /= 2, f is', f)

g **= 2
print('g **= 2, g is', g)

h //= 2
print('h //= 2, h is', h)

i %= 2
print('i %= 2, i is', i)

# Comparison Operators
# No examples!

# Logical Operators
# No examples too!

# Member Operators
j = 30
numbers = [10, 20, 30, 40, 50]

if j in numbers:
    print('`j` is in `numbers`')
else:
    print('`j` is not in `numbers`')

# Identity Operations
k = [1, 2, 3]
m = n = [1, 2, 3]

print(m is n)
print(k is n)
