import csv

class Library:
    
    def __init__(self,id_book,title,sub_title,author,category,publication_date,editor,description):
    
        self.id_book = row["id_book"] 
        self.title = row["title"]
        self.sub_title = row["sub_title"]
        self.author = row["author"]
        self.category = row["category"]
        self.publication_date = row["publication_date"]
        self.editor = row["editor"]
        self.description = row["description"]
    
  
def consult_by_name():
        for book in list_of_book:
            print("{}, {}".format(book.title,book.sub_title))
        print("\n")

list_of_book = []            

with open('books.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                list_of_book.append(Library(row["id_book"], row["title"],row["sub_title"], row["author"], row["category"], row["publication_date"], row["editor"], row["description"] ))
                #libro = Library(row["id_book"], row["title"],row["sub_title"], row["author"], row["category"], row["publication_date"], row["editor"], row["description"] )



