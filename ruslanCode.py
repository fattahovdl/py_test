# создать класс животные у которого есть свойство ходить
#
# создать подкласс кот у которого есть наследованное
# свойство ходить и свой  свойство говорить Мяу

class Animal:
    def __init__(self, pet):
        self.pet = pet

    def legs(self, legs):
        self.legs = legs

    def wool(self, wool):
        self.wool = wool

    def sound(self, sound):
        self.sound = sound

    def say(self):
        print(f"Я {self.pet}, хожу на {self.legs} ногах, {self.wool} и говорю {self.sound}")


cat = Animal("кот")
cat.legs("4")
cat.wool("шерстяной")
cat.sound("мяу")


def ch():
    choice = input("1. инфо\n"
                   "2. сказать мяу\n"
                   "3. выйти\n")

    if choice == "1":
        cat.say()

    if choice == "2":
        sayCount = int(input("сколько раз?"))
        for i in range(sayCount):
            print(f"{cat.sound}")

    if choice == "3":
        exit()


while True:
    ch()
