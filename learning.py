class Bird:
    ClassName = "Пташка"
    objInstancesCount = 0

    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
        Bird.objInstancesCount = Bird.objInstancesCount + 1

    def info(self): # Функція info всередині класу Bird називається методом класу
        print(self.name)
        print("Айдішка птахи " + str(self.id))
        print("Вік птахи: " + str(self.age))

b = Bird("обєкт №1 класу " + Bird.ClassName, 11, 3)
b.info()