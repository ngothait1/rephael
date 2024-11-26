# Python course - level 2 - Intermediate
# Lesson 40 - Final Project - Revision 1
# Author: Rephael Sintes


def printMenu():
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all Names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Exit")


def saveNewEntry(entries_lst, ids_dict, ages_sum_value):
    id_number = input("ID: ")
    if not id_number.isdigit():
        print(f"Error: ID must be a number. {id_number} is not a number")
        return
    id_number = int(id_number)
    if id_number in ids_dict:
        existing_entry = entries[ids_dict[id_number]]
        existing_name = f"'name': '{existing_entry[1]}'"
        existing_age = f"'age': {existing_entry[2]}"
        print(f"Error: ID already exists: {{{existing_name}, {existing_age}}}")
        return

    name = input("Name: ")
    if not name.isalpha():
        print(
            f"Error: Name must contain only alphabetical characters. {name} is not alphabetical"
        )
        return

    age = input("Age: ")
    if not age.isdigit():
        print(f"Error: Age must be a whole number. {age} is not a whole number")
        return
    age = int(age)

    entries_lst.append([id_number, name, age])
    ids_dict[id_number] = len(entries_lst) - 1
    print(f"ID [{id_number}] saved successfully")
    return ages_sum_value + age


def searchById(entries_lst):
    id_to_search = input("Please enter the ID you want to look for: ")
    if not id_to_search.isdigit():
        print(f"Error: ID must be a number. {id_to_search} is not a number")
        return
    id_to_search = int(id_to_search)
    if id_to_search not in ids_to_indices:
        print(f"Error: ID {id_to_search} is not saved")
        return
    index = ids_to_indices[id_to_search]
    printByIndex(index, entries_lst)


def printAgesAverage(entries_num, ages_sum_value):
    if entries_num == 0:
        print(0.0)
    else:
        print(ages_sum_value / (entries_num))


def printAllItems(index_of_item):
    for index, item in enumerate(entries):
        print(f"{index}. {item[index_of_item]}")


def printAllEntries():
    for index, item in enumerate(entries):
        print(f"{index}. ID: {item[0]}")
        print(f"    Name: {item[1]}")
        print(f"    Age: {item[2]}")


def printEntryByIndex(last_index, entries_lst):
    index_to_print = input("Please enter the index of the entry you want to print: ")
    if not index_to_print.isdigit():
        print(f"Error: Index must be a number. {index_to_print} is not a number")
        return
    index_to_print = int(index_to_print)
    if index_to_print > last_index:
        print(f"Error: Index out of range. The maximum index allowed is {last_index}")
        return
    printByIndex(index_to_print, entries_lst)


def exitProgram():
    to_exit = input("Are you sure? (y/n)")
    while to_exit not in ["y", "n"]:
        to_exit = input("Are you sure? (y/n)")
    if to_exit == "y":
        exit(0)


def printByIndex(by_index, entries_lst):
    print(f"ID: {entries_lst[by_index][0]}")
    print(f"Name: {entries_lst[by_index][1]}")
    print(f"Age: {entries_lst[by_index][2]}")


entries = []
ids_to_indices = {101: 0, 102: 1, 103: 2}
ages_sum = 27 + 36 + 24

entries.append([101, "Rephael", 27])
entries.append([102, "Nadav", 36])
entries.append([103, "Sapir", 24])

while True:
    printMenu()
    option = input("Please enter your option:")
    if not option.isdigit():
        print(f"Error: Option must be a whole number. {option} is not a whole number")
        continue
    option = int(option)

    if option < 1 or option > 8:
        print(f"Error: Option {option} does not exist. Please try again")
        continue
    elif option == 1:
        ages_sum = saveNewEntry(entries, ids_to_indices, ages_sum)
    elif option == 2:
        searchById(entries)
    elif option == 3:
        printAgesAverage(len(entries), ages_sum)
    elif option == 4:
        # Prints all names
        printAllItems(index_of_item=1)
    elif option == 5:
        # Prints all IDs
        printAllItems(index_of_item=0)
    elif option == 6:
        printAllEntries()
    elif option == 7:
        printEntryByIndex(len(entries) - 1, entries)
    elif option == 8:
        exitProgram()
    input("Press enter to continue")
