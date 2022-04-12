class Fruit:
    def __init__(self):
        print("From Fruit Class")
    def print_va(self):
        print("I am from Fruit")


class Apple(Fruit):
    def __init__(self):
        super().__init__(self)
        print("Printing from print_va")

    def print_va(self):
        print("I am from Fruit")


obj_apple = Apple()
obj_apple.print_va()

