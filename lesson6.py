"""---- Lesson 6: Incapsulation----
        part1: Classwork """
# class B:
#     __count = 0
#     def __init__(self):
#         B.__count += 1
#     def __del__(self):
#         B.__count -= 1
#     def qtyObject():
#         return B.__count
#
# class DoubleList:
#     def __init__(self, l):
#         self.list = l
#         self.double = DoubleList.__makeDouble(self)
#     def __makeDouble(self):
#         new = []
#         for i in self.list:
#             new.append(i)
#             new.append(i)
#         return new
#
# class A:
#     def __init__(self, v1, v2, v3):
#         self.field1 = v1
#         self.field2 = v2
#         self.field3 = v3
#     def __setattr__(self, attr, value):
#         if attr == 'field1' or attr == 'field2' or attr == 'field3':
#             self.__dict__[attr] = value
#         else:
#             raise AttributeError

"""---- Lesson 6: Incapsulation
        part2: Homework --------- """

class D:
    def __init__(self,n,s,p):
        self.position = p
        self.__name = D.__checkName(n)
        self.__surname = D.__checkName(s)
    def setName(self,n,s):
        self.__name = D.__checkName(n)
        self.__surname = D.__checkName(s)
    def getName(self):
        return self.__name, self.__surname

    def __checkName(k):
        if k[0].islower():
            return k.capitalize()
        else:
            return k
# WHY ???  This overloading (see below) doesn't work here. WHY ???
    # def __setattr__(self, attr, value):
    #     if attr == 'position':
    #         self.__dict__[attr] = value
    #     else:
    #         raise AttributeError
if __name__ == '__main__':

 # ------------------Classwork:
 # a = B()
 # b = B()
 # c = B()
# print(B.qtyObject())
# del c
# print(B.qtyObject())
# del a
# print(B.qtyObject())
# lt = DoubleList([1,2,3])
# print(lt.list)
# print(lt.double)

 # aa = A(10, 20, 30)
 # print(aa.field1)
 # aa.field2 = 20
 # print(aa.field2)
 # print(aa.__dict__)

 # ------------------Homework:
 person = D('Jack', 'brown', 'clener')

#-- Check name
 # print(person.name)
 print(person._D__name)

 person.setName('Bob', 'dilan')
 print(person.getName())
 print(person.position)
 print()
 person.__name = 'dack'
 print(person.__name)
 # person.__checkName()
