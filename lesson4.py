
"""---------EXERCISE from lesson 4: Inheriatence ------------------------"""

from random import randint

class Person:
    number = 0
    def __init__(self, id, team):
        Person.number += 1
        self.id = Person.number
        self.team = team

class Hero(Person):
    def __init__(self, id, team, level):
        Person.__init__(self, id, team)
        self.level = level
    def grow_level(self):
        self.level +=1

class Soldier(Person):
    def __init__(self, id, team):
        Person.__init__(self, id, team)

    def follow_hero(self, hero):
        print ('Soldier', self.id, 'of team', self.team ,'follow Hero', hero.id)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

  hero1 = Hero(1, 'white', 0)
  print(hero1.id)
  hero2 = Hero(2, 'black', 0)
  print(hero2.id)
  team_white = []
  team_black = []

  for i in range(1,11):

      n = randint(1,2)
      if n == 1:
          a = Soldier(i, 'white')
          team_white.append(a)
      else:
          b = Soldier(i, 'black')
          team_black.append(b)

      # print('white team = ', len(team_white))
      # print('black team = ', len(team_black))

      if len(team_black) > len(team_white):
          hero2.grow_level()
      elif len(team_black) < len(team_white):
          hero1.grow_level()


print( [team_white[i].id for i in range(len(team_white))])
print( [team_black[i].id for i in range(len(team_black))])

follower = randint(1,len(team_white))
print(follower)

team_white[follower].follow_hero(hero1)
print()
print(f"Level of Hero1: {hero1.level}")
print(f"Level of Hero2: {hero2.level}")
