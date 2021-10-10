"""--------Lesson 7: Composition-------"""

class WinDoor:
    def __init__(self, x, y):
        self.square = x*y

class Room:
    def __init__(self, x, y, z):
        self.length = x
        self.width = y
        self.hight = z
        self.wd = []

    def add_wd(self, h, w):
        self.wd.append(WinDoor(h, w).square)

    def work_square(self):
        ws = 2*self.hight*(self.length + self.width)
        for i in self.wd:
            ws -=i
        return ws

    def how_many_rulons(self, w, l, ws):
        number = ws/w/l
        return number

if __name__ == '__main__':

 x = float((input('Enter room length(in metres): ')))
 y = float((input('room width: ')))
 z = float((input('room higth: ')))
 r1 = Room(x, y, z)

 n = int((input('Enter number of windows and doors: ')))

 for l in range(n):
      print('Enter parameters of window-door №:', l+1)
      lh = float((input('win_door hight: ')))
      lw = float((input('win_door width: ')))
      r1.add_wd(lh,lw)

 ws = r1.work_square()

 print('Enter parameters of rulon: ')
 rh = float((input('length: ')))
 rw = float((input(' width: ')))
 rq = int(r1.how_many_rulons(rh,rw,ws))
 print()
 print('The total area of gluing', ws, 'm2')
 print('You need to buy ', rq, 'rulons')

