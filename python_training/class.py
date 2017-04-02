#coding: UTF-8
class Dog:
    name = ""
    def brak(self):
        m = self.name + " : Bow-wow!"
        print(m)

pochi = Dog()
pochi.name = "Pochi"
pochi.brak()

hachi = Dog()
hachi.name = "Hachi"
hachi.brak()