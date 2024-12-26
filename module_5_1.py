class house:
    def __init__(self, name, num_flrs):
        self.name = name
        self.number_of_floors = num_flrs
    def go_to(self, new_floor):
        print(f'Едем на {new_floor} этаж {self.name}:')
        if 1 <= new_floor <= self.number_of_floors:
            i = 1

            while i <= new_floor:
                print(f'Мы на {i} этаже!')
                i = i + 1
        else:
            print('Такого этажа не существует!')

h1 = house('ЖК Горский', 18)
h2 = house('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)