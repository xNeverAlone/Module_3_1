calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    stroka = str(string)
    itog = (len(stroka), stroka.upper(), stroka.lower())
    count_calls()
    return itog
def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            itog = True
            break
        else:
            itog = False
            continue
    return itog
print(string_info('Balalaika'))
print(string_info('Molotov'))
print(is_contains('gubka', ['frame', 'blame', 'flame']))
print(is_contains('BiVER', ['Budka', 'Vodka', 'LaMpa', 'FoMKA']))

print(calls)

