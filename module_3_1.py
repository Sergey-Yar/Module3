calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()
def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower() == i.lower():
            return True
        else:
            continue
    return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Кукарача'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('КУКАрача', ['товарищ', 'скрипка', 'кукарамба', 'Мол']))
print(calls)