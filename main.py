from books import Book
from consult_library import Library
from consult_library import consult_by_name
from os import system, name
from time import sleep
import csv

list_of_book = []

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

print("-----------------------------------------")
print("Bienvenidos a la Biblioteca de Alejandria")
print("-----------------------------------------\n\n")

print("Cargando libros ...")

with open('books.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                list_of_book.append(Library(row["id_book"], row["title"],row["sub_title"], row["author"], row["category"], row["publication_date"], row["editor"], row["description"] ))

sleep(1)
print("Libros actualizados")

while True:
    print("\n1. Ingresar libro")
    print("2. Consultar libro")
    print("Salir")
    option = int(input("Selecciona el # de opcion: "))
    clear

    if option == 1:
        list_of_book.append(Book())
    elif option == 2:
        print(consult_by_name())
    elif option == 3:
        break
    else:
        print("no has seleccionado una opcion correcta")
