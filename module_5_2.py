class house:
    def __init__(self, name, num_flrs):
        self.name = name
        self.number_of_floors = num_flrs

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"

h1 = house('ЖК Эльбрус', 10)
h2 = house('ЖК Акация', 20)

print(h1)
print(h2)

print(len(h1))
print(len(h2))