class Book:

    def __init__(self):
        self.id_book = input("Ingrese el ID de libro: ")
        self.tittle = input("Ingrese el Titulo de libro: ")
        self.sub_title = input("Ingrese el Sub Titulo de libro: ")
        self.author = []
        x = int(input("Ingrese la catidad de autores: "))
        for i in range(0,x):
            self.author.append(input("Ingrese el nombre del autor:"))
        self.category = []
        x = int(input("Ingrese la catidad de categotias: "))
        for i in range(0,x):
            self.category.append(input("Ingrese la categoria: "))
        self.publication_date = input("Ingrese la fecha de publicación: ")
        self.editor = input("Ingrese la Editorial:")
        self.description = input("Ingrese la Descripción: ")



