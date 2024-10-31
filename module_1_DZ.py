# Дано:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Решение:
# Преобразуем список списков оценок в список средних баллов:
grades = [[(sum(grades[0])/len(grades[0]))],[(sum(grades[1])/len(grades[1]))],[(sum(grades[2])/len(grades[2]))],[(sum(grades[3])/len(grades[3]))],[(sum(grades[4])/len(grades[4]))]]
# Преобразуем множество студентов в упорядочиваемый список:
students = list(students)
# Упорядочиваем (в этом месте погуглил функцию .sort, которая по умолчанию делает порядок алфавитным):
students.sort()
# Объединяем в словарь в пары по индексам
dict_pairs=[(students[0],grades[0]),(students[1],grades[1]),(students[2],grades[2]),(students[3],grades[3]),(students[4],grades[4])]
print(dict_pairs)
