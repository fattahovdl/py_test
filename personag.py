class Persona:
    def __init__(self, imya,hp,dmg,armor):
        self.imya=imya
        self.hp=hp
        self.dmg=dmg
        self.armor=armor

name=input("Введите имя персонажа: ")
my_hp=100
my_dmg=20
my_armor=5
personag=Persona(name,my_hp,my_dmg,my_armor)
print(personag.imya)
print(personag.hp)
print(personag.dmg)
