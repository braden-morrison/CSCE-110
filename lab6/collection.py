# File: book_library.py
# Author: Braden Morrison
# Date: xx/xx/2022
# Section: Student section number
# E-mail: student_email@tamu.edu
# Description:
# e.g., This program asks for ...

import math


def main():
    """Driver function"""
    library = {}
    while True:
        print_menu()
        option = input('Choose a menu option: ')
        if option == '1':
            # add_books(library)
            add_books(library)
        elif option == '2':
            print_books(library)
        elif option == '3':
            create_collections(library)
        elif option == '4':
            sort_collections(library)
        elif option == '5':
            delete_collection(library)
        elif option == '6':
            print("End", end='')
            break
        else:
            print('\nInvalid entry\n')


def print_menu():
    """Prints the menu of options to the librarian"""
    print('*******************Main Menu*******************')
    print('1. Add books to the library')
    print('2. Print available books in the library')
    print('3. Create book collections')
    print('4. Sort books in the collections')
    print('5. Delete a collection')
    print('6. Quit')
    print('***********************************************')
    print()
    pass


def check_isbn(isbn):
    """Checks the format of an ISBN"""
    # to do
    pass


def add_books(library):

    num_books = int(input("How many books would you like to enter: "))
    print()
    counter = 1
    dic = library

    for x in range(num_books):
        val = True
        while val:
            print('Enter book ', counter, ': ', end="", sep="")
            user_input = input()
            dic[counter] = {'title': '', 'ISBN': ''}
            title_I, number_I = user_input.rsplit(maxsplit=1)
            if len(number_I) != 10:
                print('Invalid entry')
            elif number_I.isdigit() != True:
                print('Invalid entry')
            elif number_I in [book_data['ISBN'] for book_data in library.values()]:
                print('Invalid entry')

            else:
                dic[counter]['title'] = title_I
                dic[counter]['ISBN'] = number_I
                counter += 1
                val = False
    print()
    return dic
    # pass


def print_books(library):
    """Prints available books in the library"""
    if len(library) == 0:
        print('Invalid entry')
    print()
    print("Books available in the library:")
    for book in library.values():
        title = book['title']
        isbn = book['ISBN']
        print(f"{title:20}{isbn:10}")
    print()
    return library
    pass


def create_collections(library):
    """Creates book collections"""
    num = int(input("What is the size of the collection? "))
    num2 = len(library)
    num3 = int(num2 / num)
    num4 = num2 % num

    print()

    collections = []
    for x in range(1, num + 1):
        print(f"Enter the book ISBNs for collection {x}:")
        books = []
        if x == num3:
            user_input = input()
            if len(user_input) != 10:
                print('Invalid entry')
                user_input = input()
            if user_input.isdigit() != True:
                print('Invalid entry')
                user_input = input()
            if user_input not in [book_data['ISBN'] for book_data in library.values()]:
                print('Invalid entry')
                user_input = input()

            title = next((book_data['title'] for book_data in library.values(
            ) if book_data['ISBN'] == user_input), None)
            books.append((title, user_input))
        else:
            for y in range(num3):
                user_input = input()
                if len(user_input) != 10:
                    print('Invalid entry')
                    user_input = input()
                if user_input.isdigit() != True:
                    print('Invalid entry')
                    user_input = input()
                if user_input not in [book_data['ISBN'] for book_data in library.values()]:
                    print('Invalid entry')
                    user_input = input()

                title = next((book_data['title'] for book_data in library.values(
                ) if book_data['ISBN'] == user_input), None)
                books.append((title, user_input))
        if books:
            collections.append(books)
            print()

    print('Current book collections:')
    for i, collection in enumerate(collections, 1):
        print(f"Collection {i}:")
        for title, isbn in collection:
            print(f"{title:20}{isbn:10}")
        print()
    library.clear()
    return collections


def sort_collections(library):
    """Sort books in the collections"""
    print(library)
    choice = input("Sort books in ascending or descending order of ISBN: ")
    if choice.capitalize() == 'Ascending':
        sorted_library = sorted(library.values(), key=lambda x: x['ISBN'])
    elif choice.capitalize() == 'Descending':
        sorted_library = sorted(
            library.values(), key=lambda x: x['ISBN'], reverse=True)
    print('\nCurrent book collections:')
    for i, collection in enumerate(sorted_library, 1):
        print(f"Collection {i}:")
        for title, isbn in collection:
            print(f"{title:20}{isbn:10}")
        print()
        print()


def delete_collection(library):
    """Deletes a collection"""
    num = input("Which collection would you like to delete? ")
    print()
    del library[num - 1]
    print()
    print('Current book collections:')
    for i, collection in enumerate(library, 1):
        print(f"Collection {i}:")
        for title, isbn in collection:
            print(f"{title:20}{isbn:10}")
        print()


main()
