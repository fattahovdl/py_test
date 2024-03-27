class Animal:
    def __init__(self):
        self.nogi = 0
    def walk(self):
        return print(f"Я хожу на {self.nogi} ногах")

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.say = "Miya"
    def talk(self):
        return print(self.say)

caty = Cat()
caty.say = "GAV"
caty.talk()
caty.nogi = 4
caty.walk()
# создать класс животные у которого есть свойство ходить
#
# создать подкласс кот у которого есть наследованное
# свойство ходить и свой  свойство говорить Мяу

# class Stack:
#     def __init__(self):
#         self.__stackList = []
#
#     def push(self, val):
#         self.__stackList.append(val)
#
#     def pop(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         return val
#
# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0
#
#     def getSum(self):
#         return self.__sum
#
#     def push(self, val):
#         self.__sum += val
#         Stack.push(self, val)
#
#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val
#
# stackObject = AddingStack()
# for i in range(5):
#     stackObject.push(i)
#     print(stackObject.getSum())
#
#
# for i in range(5):
#     print(stackObject.pop())