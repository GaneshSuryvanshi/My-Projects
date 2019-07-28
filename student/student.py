class Student:
    def __init__(self,name,year,adid,branch):
        self.name=name
        self.year=year
        self.adid=adid
        self.branch=branch
        self.eno="0187"+branch+adid
        self.num_book_issued=0
        self.book_issued={}
        self.passwrd='0000'
       