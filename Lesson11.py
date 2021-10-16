from random import randint

class Data:
    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self,i):
        return self.info[i]

class Teacher:
    def __init__(self, name):
        self.name = name
    def teach_data(self, data, *pupil):
        for i in pupil:
            i.take_data(data)

class Pupil:
    def __init__(self, name):
        self.name = name
        self.knowledge = []
    def take_data(self, data):
        self.knowledge.append(data)
    def forget_smth(self):
        l = randint(0,len(self.knowledge))
        self.knowledge.pop(l)

if __name__ == '__main__':

    MI = Teacher('Maria')
    p1 = Pupil('Ivan')
    p2 = Pupil('Petro')
    lesson = Data('oop', 'polimorph', 'incapsulat', 'inheriten')
    MI.teach_data(lesson[1], p1, p2)
    MI.teach_data(lesson[2], p1)
    p1.take_data(lesson[3])
    print(p1.knowledge)
    print(p2.knowledge)
    p1.forget_smth()
    print(p1.knowledge)