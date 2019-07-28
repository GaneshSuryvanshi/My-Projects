class Book:
    def __init__(self,title,author,isbn,numofcopies):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.numofcopies=numofcopies
        self.avail=numofcopies
        self.students={}
        self.faculties={}
        