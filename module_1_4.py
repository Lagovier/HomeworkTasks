my_string = input("Введите произвольный текст: ")
symbol_count = len(my_string)
print("Количество введённых символов:",symbol_count)
print("В верхнем регистре:",my_string.lower())
print("В нижнем регистре:",my_string.upper())
print("Без пробелов:",my_string.replace(" ",""))
print("Первый символ:",my_string[0])
print("Последний символ:",my_string[-1])