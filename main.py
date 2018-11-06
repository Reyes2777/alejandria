from books import Book

list_of_book = []

print("-----------------------------------------")
print("Bienvenidos a la Biblioteca de Alejandria")
print("-----------------------------------------\n\n")

while True:
    print("\n1. Ingresar libro")
    print("2. Consultar libro")
    print("Salir")
    option = int(input("Selecciona el # de opción: "))

    if option == 1:
        list_of_book.append(Book())
    elif option == 3:
        break
    else:
        print("no has seleccionado una opcion correcta")
