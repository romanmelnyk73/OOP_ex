"""------Operator __getitem__(): - overloading---"""
class A:
    def __init__(self, arg):
        self.arg = arg
    def __str__(self):
        return str(self.arg)

class B:
    def __init__(self, *args):
        self.aList = []
        for i in args:
            self.aList.append(A(i))
    def __getitem__(self, item):
        return self.aList[item]

# -----------------------------------------------------
"""---Part2:----EXERCISE from lesson 8: Operators Overloading---------"""
# ______________________________________________________
class Snow:
    def __init__(self, number):
        self.number = int(number)
        self.sign = '*'
    def __call__(self, n):
        self.number = n
        return self.number
    def __add__(self, other):
        self.number += other
        return self.number
    def __sub__(self, other):
        self.number -= other
        return self.number
    def __mul__(self, other):
        self.number *= other
    def __truediv__(self, other):
        self.number //= other
    def makeSnow(self, n):
        k = int(self.number/n)
        r = self.number - k*n
        snow = []
        for i in range(k):
            snow.append(self.sign*n)
        snow.append(self.sign * r)
        snow = "\n".join(snow)
        return snow
#     ________ANSWER from Ex.book for method makeSnow________________
#     def makeSnow(self, n):
#         k = int(self.number/n)
#         s = ''
#         for i in range(k):
#             s += n*'*' + '\n'
#         s += '*' * (self.number - k*n)
#         if s[-1] == '\n':
#             s = s[:-1]
#         return s

if __name__ == '__main__':

 group = B(5, 7, 'abc')
 print(group.aList[0])
 print(group.aList[1])
 print(group[2])

# __________PART 2____________________________
 sn = Snow(30)
 print(sn(30))
 print(sn.makeSnow(11))

 sn + 14
 print(sn.number)
 print(sn.makeSnow(11))

 sn - 19
 print(sn.number)
 print(sn.makeSnow(17))

 sn/2
 print(sn.number)
 print(sn.makeSnow(17))

 sn * 2
 print(sn.number)
 print(sn.makeSnow(17))

