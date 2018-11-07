import csv

class Book:

    def __init__(self):
        self.id_book = input("Ingrese el ID de libro: ")
        self.title = input("Ingrese el Titulo de libro: ")
        self.sub_title = input("Ingrese el Sub Titulo de libro: ")
        self.author = []
        x = int(input("Ingrese la catidad de autores: "))
        for i in range(0,x):
            self.author.append(input("Ingrese el nombre del autor:"))
        self.category = []
        y = int(input("Ingrese la catidad de categotias: "))
        for i in range(0,y):
            self.category.append(input("Ingrese la categoria: "))
        self.publication_date = input("Ingrese la fecha de publicacion: ")
        self.editor = input("Ingrese la Editorial:")
        self.description = input("Ingrese la Descripcion: ")

        with open('books.csv', 'a', newline='') as csvfile:
            fieldnames = ['id_book', 'title', "sub_title", "author", "category", "publication_date", "editor", "description"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'id_book': self.id_book, 'title': self.title, "sub_title": self.sub_title, "author": self.author, "category": self.category, "publication_date": self.publication_date, "editor": self.editor, "description": self.description} )

        