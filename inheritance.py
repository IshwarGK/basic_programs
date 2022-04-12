class Fruit():
    def __init__(self):
        print("I am fruit")


class Mango(Fruit):
    def __init__(self):
        super().__init__()
        print("I am Mango")

obj = Mango()