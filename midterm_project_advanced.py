# Python course - level 3 - Advanced
# Lesson 51 - Midterm Project
# Author: Rephael Sintes

import os
import json
import pandas as pd


def printMenu():
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all Names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Save all data")
    print("9. Exit")


def saveNewEntry(entries_lst, ids_dict):
    id_number = input("ID: ")
    if isDigit(id_number, "ID"):
        id_number = int(id_number)
    else:
        return 0
    if id_number in ids_dict:
        existing_entry = entries[ids_dict[id_number]]
        existing_name = f"'name': '{existing_entry[1]}'"
        existing_age = f"'age': {existing_entry[2]}"
        print(f"Error: ID already exists: {{{existing_name}, {existing_age}}}")
        return 0

    name = input("Name: ")
    if not name.isalpha():
        print(
            f"Error: Name must contain only alphabetical characters. {name} is not alphabetical"
        )
        return 0

    age = input("Age: ")
    if isDigit(age, "Age"):
        age = int(age)
    else:
        return 0

    entries_lst.append([id_number, name, age])
    ids_dict[id_number] = len(entries_lst) - 1
    print(f"ID [{id_number}] saved successfully")
    return age


def searchByID(entries_lst):
    id_to_search = input("Please enter the ID you want to look for: ")
    if isDigit(id_to_search, "ID"):
        id_to_search = int(id_to_search)
    else:
        return

    if id_to_search not in ids_to_indices:
        print(f"Error: ID {id_to_search} is not saved")
        return

    index = ids_to_indices[id_to_search]
    printEntryData(index, entries_lst[index])


def printAgesAverage(entries_num, ages_sum_value):
    if entries_num == 0:
        print(0.0)
    else:
        print(ages_sum_value / entries_num)


def printAllNames(entries_lst):
    for index, entry in enumerate(entries_lst):
        print(f"{index}. {entry[1]}")


def printAllIDs(entries_lst):
    for index, entry in enumerate(entries_lst):
        print(f"{index}. {entry[0]}")


def printAllEntries():
    for index, item in enumerate(entries):
        printEntryData(index, item)


def printEntryByIndex(last_index, entries_lst):
    index_to_print = input("Please enter the index of the entry you want to print: ")
    if isDigit(index_to_print, "Index"):
        index_to_print = int(index_to_print)
    else:
        return

    if index_to_print > last_index:
        print(f"Error: Index out of range. The maximum index allowed is {last_index}")
        return

    printEntryData(index_to_print, entries_lst[index_to_print])


def saveAllData(entries_lst):
    current_working_directory = os.getcwd()
    config_file = "conf.json"
    config_file_path = os.path.join(current_working_directory, config_file)

    if not os.path.exists(config_file_path):
        conf_data = {"id": "id", "name": "name", "age": "age"}
        with open(config_file_path, "w") as file:
            json.dump(conf_data, file, indent=4)
    else:
        with open(config_file_path) as file:
            conf_data = json.load(file)

    output_file_name = input("What is your output file name? ")

    data_to_save = {
        conf_data["id"]: [item[0] for item in entries_lst],
        conf_data["name"]: [item[1] for item in entries_lst],
        conf_data["age"]: [item[2] for item in entries_lst],
    }

    df = pd.DataFrame(data_to_save)
    df.to_csv(output_file_name, index=False)


def exitProgram():
    to_exit = input("Are you sure? (y/n)")
    while to_exit not in ["y", "n"]:
        to_exit = input("Are you sure? (y/n)")
    if to_exit == "y":
        exit(0)


def isDigit(num_value, num_name):
    if num_value.isdigit():
        return True
    print(f"Error: {num_name} must be a number. {num_value} is not a number")
    return False


def printEntryData(index, item):
    spacer = len(str(index)) * " " + "  "
    print(f"{index}. ID:   {item[0]}")
    print(f"{spacer}Name: {item[1]}")
    print(f"{spacer}Age:  {item[2]}")


entries = []
ids_to_indices = {}
ages_sum = 0

entries.append([101, "Rephael", 27])
entries.append([102, "Nadav", 36])
entries.append([103, "Sapir", 24])

ids_to_indices[101] = 0
ids_to_indices[102] = 1
ids_to_indices[103] = 2

ages_sum += 27
ages_sum += 36
ages_sum += 24

while True:
    printMenu()
    option = input("Please enter your option:")
    if isDigit(option, "Option"):
        option = int(option)
    else:
        continue

    if option < 1 or option > 9:
        print(f"Error: Option {option} does not exist. Please try again")
        continue
    elif option == 1:
        ages_sum += saveNewEntry(entries, ids_to_indices)
    elif option == 2:
        searchByID(entries)
    elif option == 3:
        printAgesAverage(len(entries), ages_sum)
    elif option == 4:
        printAllNames(entries)
    elif option == 5:
        printAllIDs(entries)
    elif option == 6:
        printAllEntries()
    elif option == 7:
        printEntryByIndex(len(entries) - 1, entries)
    elif option == 8:
        saveAllData(entries)
    elif option == 9:
        exitProgram()
    input("Press enter to continue")
