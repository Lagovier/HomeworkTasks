my_dict = {"Alex":1982,"Boris":1990,"Viktor":1993}
print("Словарь: ",my_dict)
print("Существующее значение: ",my_dict["Alex"])
print("Отсутствующее значение: ",my_dict.get("Grigory"))
my_dict["Dmitry"]=1976
my_dict["Egor"]=1979
print("Извлечённое по ключу значение: ",my_dict.pop("Alex"))
print("Словарь без извлечённой пары: ",my_dict)
my_set = {"string",4,2,True,3,5,7,5,2,1,6}
print("Множество: ",my_set)
my_set.add(33)
my_set.add(44)
print("Множество с дополнениями: ",my_set)
my_set.discard(1) # 1 считается за True, а 0 за False
print('Множество с исключённым значением "1": ',my_set)