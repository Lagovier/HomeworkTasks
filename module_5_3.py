class house:
    def __init__(self, name, num_flrs):
        self.name = name
        self.number_of_floors = num_flrs

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"

    def __lt__(self, other):
        return self.number_of_floors < other

    def __gt__(self, other):
        return self.number_of_floors > other

    def __eq__(self, other):
        return self.number_of_floors == other

    def __le__(self, other):
        return self.number_of_floors <= other

    def __ge__(self, other):
        return self.number_of_floors >= other

    def __ne__(self, other):
        return self.number_of_floors != other

    def __add__(self, other):
        self.number_of_floors = self.number_of_floors + other
        return self

    def __iadd__(self, other):
        self.number_of_floors += other
        return self

    def __radd__(self, other):
        self.number_of_floors = other + self.number_of_floors
        return self

h1 = house('ЖК Эльбрус', 10)
h2 = house('ЖК Акация', 20)

print(h1)
print(h2)
print(f'Равенство: {h1 == h2}') # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(f'Равенство: {h1 == h2}')
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(f'Дом {h1.name} больше дома {h2.name}: {h1 > h2}') # __gt__
print(f'Дом {h1.name} больше или равен дому {h2.name}: {h1 >= h2}') # __ge__
print(f'Дом {h1.name} меньше дома {h2.name}: {h1 < h2}') # __lt__
print(f'Дом {h1.name} меньше или равен дому {h2.name}: {h1 <= h2}') # __le__
print(f'Дом {h1.name} не равен дому {h2.name}: {h1 != h2}') # __ne__

