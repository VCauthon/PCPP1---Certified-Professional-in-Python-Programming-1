class Duck:
    def __init__(self, color) -> None:
        self.color = color


duck_a = Duck("white")
print(duck_a.__dict__)
duck_a.other_color = "black"
print(duck_a.__dict__)


print(Duck.__dict__)
Duck.class_variable = 1
print(Duck.__dict__)
