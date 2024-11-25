# Python course - level 2 - Intermediate
# Lesson 40 - Final Project
# Author: Rephael Sintes


def saveNewEntry(last_index_value, ages_sum_value):
    id_number = input('ID: ')
    if not id_number.isdigit():
        return {'error': True, 'msg': f'Error: ID must be a number. {id_number} is not a number'}
    id_number = int(id_number)
    if id_number in ids_to_indices:
        existing_entry = entries[ids_to_indices[id_number]]
        existing_name = f"'name': '{existing_entry[1]}'"
        existing_age = f"'age': {existing_entry[2]}"
        return {'error': True, 'msg': f'Error: ID already exists: {{{existing_name}, {existing_age}}}'}

    name = input('Name: ')
    if not name.isalpha():
        return {'error': True, 'msg': f'Error: Name must contain only alphabetical characters. {name} is not alphabetical'}

    age = input('Age: ')
    if not age.isdigit():
        return {'error': True, 'msg': f'Error: Age must be a whole number. {age} is not a whole number'}
    age = int(age)

    return {'error': False,
            'id': int(id_number),
            'name': name,
            'age': age,
            'last_index': last_index_value + 1,
            'ages_sum': ages_sum_value + age
            }


def searchById():
    id_to_search = input('Please enter the ID you want to look for: ')
    if not id_to_search.isdigit():
        return {'error': True, 'msg': f'Error: ID must be a number. {id_to_search} is not a number'}
    id_to_search = int(id_to_search)
    if id_to_search not in ids_to_indices:
        return {'error': True, 'msg': f'Error: ID {id_to_search} is not saved'}
    index = ids_to_indices[id_to_search]
    printByIndex(index)


def printAgesAverage(last_index_value, ages_sum_value):
    if last_index_value == -1:
        return {'error': True, 'msg': 'Error: No ages to calculate. Please enter at least one data entry'}
    print(ages_sum_value / (last_index_value + 1))
    return {'error': False}


def printAllItems(index_of_item):
    for index, item in enumerate(entries):
        print(f'{index}. {item[index_of_item]}')


def printAllEntries():
    for index, item in enumerate(entries):
        print(f'{index}. ID: {item[0]}')
        print(f'    Name: {item[1]}')
        print(f'    Age: {item[2]}')


def printEntryByIndex(last_index_value):
    index_to_print = input(
        'Please enter the index of the entry you want to print: ')
    if not index_to_print.isdigit():
        return {'error': True, 'msg': f'Error: Index must be a number. {index_to_print} is not a number'}
    index_to_print = int(index_to_print)
    if index_to_print > last_index_value:
        return {'error': True, 'msg': f'Error: Index out of range. The maximum index allowed is {last_index_value}'}
    printByIndex(index_to_print)
    return {'error': False}


def exitProgram():
    to_exit = input('Are you sure? (y/n)')
    while to_exit not in ['y', 'n']:
        to_exit = input('Are you sure? (y/n)')
    if to_exit == 'y':
        exit(0)


def printByIndex(by_index):
    print(f'ID: {entries[by_index][0]}')
    print(f'Name: {entries[by_index][1]}')
    print(f'Age: {entries[by_index][2]}')


entries = []
ids_to_indices = {}
last_index = -1
ages_sum = 0

while True:
    print('1. Save a new entry')
    print('2. Search by ID')
    print('3. Print ages average')
    print('4. Print all Names')
    print('5. Print all IDs')
    print('6. Print all entries')
    print('7. Print entry by index')
    print('8. Exit')
    choice = input('Please enter your choice:')

    if choice not in '12345678' and len(choice) > 1:
        print(f'Error: Option {choice} does not exist. Please try again')
        continue
    elif choice == '1':
        result = saveNewEntry(last_index, ages_sum)
        if result['error']:
            print(result['msg'])
        else:
            last_index = result['last_index']
            ages_sum = result['ages_sum']
            entries.append([result['id'], result['name'], result['age']])
            ids_to_indices[result['id']] = last_index
            print(f'ID [{result['id']}] saved successfully')
    elif choice == '2':
        result = searchById()
        if result['error']:
            print(result['msg'])
    elif choice == '3':
        result = printAgesAverage(last_index, ages_sum)
        if result['error']:
            print(result['msg'])
    elif choice == '4':
        # Prints all names
        printAllItems(index_of_item=1)
    elif choice == '5':
        # Prints all IDs
        printAllItems(index_of_item=0)
    elif choice == '6':
        printAllEntries()
    elif choice == '7':
        result = printEntryByIndex(last_index)
        if result['error']:
            print(result['msg'])
    elif choice == '8':
        exitProgram()
    input('Press enter to continue')
