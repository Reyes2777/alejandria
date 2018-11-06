import csv

class Library:

    with open('books.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                     # print(row["id_book"], row["title"],row["sub_title"], row["author"], row["category"], row["publication_date"], row["editor"], row["description"] )

            def __init__(self):
                self.id_book = row["id_book"] 
                self.title = row["title"]
                self.sub_title = row["sub_title"]
                self.author = row["author"]
                self.category = row["category"]
                self.publication_date = row["publication_date"]
                self.editor = row["editor"]
                self.description = row["description"]
