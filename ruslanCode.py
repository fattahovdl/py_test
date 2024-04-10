#enemy

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

vasilisk = enemy('василиск', 110, 30, 35,)
print(vasilisk)
thief = enemy('вор', 100, 10, 25)
assassin = enemy('ассассин', 60, 15, 45)
flesh = enemy('плоть', 50, 2, 15)
jerboa = enemy('тушкан', 20, 0, 5)
buhrer = enemy('бюрер', 140, 4, 46)
