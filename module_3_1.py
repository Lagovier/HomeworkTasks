calls = 0
def count_calls():
    global calls
    calls = calls+1
def string_info(string):
    count_calls()
    return len(string), string.lower(), string.upper()
def is_contains(string, list_to_search):
    count_calls()
    list_to_search = str(list_to_search).lower()
    string = str(string).lower()
    found = string in list_to_search
    return found

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print("Количество вызовов функций: ", calls)