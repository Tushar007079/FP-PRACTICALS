class Book:
    def __init__(self, book, author):
        self.title = book.split('.')[0]
        self.b_format = book.split('.')[1]
        self.author = author
        self.type = ""


class EBook(Book):
    def __init__(self, book, author, pages):
        super().__init__(book, author)
        self.pages = pages
        self.type = "EBook"

        if self.b_format not in ['pdf', 'epub', 'mobi', 'azw']:
            raise Exception("Invalid Format!")

    def show_details(self):
        print("\n----------------------------------")
        print(f"\nBook Name : {self.title}")
        print(f"\nBook Author : {self.author}")
        print(f"\nBook Type : {self.type}")
        print(f"\nBook Format : {self.b_format}")
        print(f"\nBook Length : {self.pages}pgs")
        print("\n----------------------------------")


class AudioBook(Book):
    def __init__(self, book, author, length):
        super().__init__(book, author)
        self.length = length
        self.type = "AudioBook"

        if self.b_format not in ['mp3', 'wma', 'wav']:
            raise Exception("Invalid Format!")

    def show_details(self):
        print("\n***********************************")
        print(f"\n  Book Name : {self.title}       ")
        print(f"\n  Book Author : {self.author}    ")
        print(f"\n  Book Type : {self.type}        ")
        print(f"\n  Book Format : {self.b_format}  ")
        print(f"\n  Book Length : {self.length}    ")
        print("\n***********************************")


book1 = EBook('BOOK1.pdf', 'author1', '250')
book2 = AudioBook('BOOK2.mp3', 'Author2', '7:10:25')
# book3 = EBook('BOOK3.mp4', 'Author3', '1:00:00')  # ERROR

book1.show_details()
book2.show_details()
# book3.show_details()
