#enemy
# враги взяты отсюда:
# https://www.playground.ru/dark_souls/guide/dark_souls_protivniki_ryadovye_protivniki-1204499
class enemy:
    def __init__(self, name, hp, armor, dmg):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.dmg = dmg
    def __str__(self):
        return f'противник: {self.name} \n' \
               f'хп: {self.hp} \n' \
               f'броня: {self.armor} \n' \
               f'урон: {self.dmg} \n'

vasilisk = enemy('василиск', 110, 10, 35,)
print(vasilisk)
