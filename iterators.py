from random import randint

class A:
    def __init__(self, qty):
        self.qty = qty
    def __iter__(self):
        return self
    def __next__(self):
        if self.qty > 0:
            self.qty -= 1
            return '+'
        else:
            raise StopIteration

class Letters:
    def __init__(self, string):
        self.letters = []
        for i in string:
            self.letters.append(i)

    def __iter__(self):
        return LettersIterator(self.letters)

class LettersIterator:
    def __init__(self, letters):
        self.letters = letters
    def __next__(self):
        if self.letters == []:
            raise StopIteration
        item = self.letters[0]
        del self.letters[0]
        return item

# ________________________HOMEWORK______________

class RanIterator:
    def __init__(self, n,  a,  b):
        self.n = n
        self.b = b
        self.a = a
    def __iter__(self):
         return self

    def __next__(self):
        if self.n == 0:
            raise StopIteration
        self.n -= 1
        return randint(self.a, self.b)


lt = Letters('aeoui')
print(type(lt.letters))
print(lt.letters)

lti = iter(lt)
# print(next(lti))
print(lt.letters)
print()
print(type(lti.letters))
for i in lt:
    print(i)

a = A(5)
print(next(a))
print(next(a))
print()

for i in a:
    print(i)

# f = open('new 1.txt')
# print(f.__next__())
# print(f.__next__())
# print(next(f))
# next(f)
# print(f.__next__())

# _______Homework_____________________________________
itr = RanIterator(3,4,8)
for i in itr:
    print(i)