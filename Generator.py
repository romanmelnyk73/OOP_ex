import random


def starmaker(n):
    while n > 0:
        yield '*'
        n-=1
n = 5
s = starmaker(5)
print(next(s))
for i in s:
    print(i)

a = [i for i in range(11) if i%2 !=0]
print(type(a))
b = (i for i in range(11) if i%2 !=0)
print(type(b))

c = ['h' for i in range(5)]
d = '5'
for i in c:
    d.join(i)
print(i)
# _________________HOMEWORK__LESSON_15__________________________
def IndGenerate(n,a,b):
    while n > 0:
        yield random.randrange(a,b)
        n -=1

cas = IndGenerate(3,5,91)
for i in cas:
    print(i)

n, a ,b = 3,5,91
cas2 = (random.randrange(a,b) for i in range(n))
for i in cas2:
    print(i)
