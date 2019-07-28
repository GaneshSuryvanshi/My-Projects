import student.student as s
import faculty.faculty as f1
import Book.book as b
import pickle
import os,getpass
from datetime import datetime,date,timedelta
#*************************************************************************************************************************
def add_student():
    name=input("enter student name \n")
    while 1:
        year=int(input("enter Admission year\n"))
        if int(datetime.today().year)>=year:
            break
        else:
            c=input("invalid year \n1.Try again\n 2.Cancle\n")
            if c=='2':
                return
    adid=input("enter admission id\n")
    branch=input("enter branch \n")
    if(os.stat("student.dat").st_size != 0):
        with open("student.dat","rb") as f:
            l=pickle.load(f)
            for i in l:
                if(i.adid==adid):
                    return False
        with open("student.dat","wb") as f:
            p=s.Student(name,year,adid,branch)
            l.append(p)
            pickle.dump(l,f)
    else:
        with open("student.dat","wb") as f:
            p=s.Student(name,year,adid,branch)
            pickle.dump([p],f)
    return p.eno
#*************************************************************************************************************************
def remove_student(enroll):
    with open("student.dat","rb") as f:
            l=pickle.load(f)
            for i in l:
                if(i.eno==enroll):
                    if(len(i.book_issued)!=0):
                        print("Please Return all the book to library then you can delete this student")
                        return False
                    l.remove(i)
                    break
            else:
                return False
    with open("student.dat","wb") as f:
        pickle.dump(l,f)
    return True
#*************************************************************************************************************************
def add_faculty():
    name=input("enter faculty name\n ")
    eid=input("enter employee id \n")
    if(os.stat("faculty.dat").st_size != 0):
        with open("faculty.dat","rb") as f:
            l=pickle.load(f)
            for i in l:
                if(i.eid==eid):
                    return False
        with open("faculty.dat","wb") as f:
            l.append(f1.Faculty(name,eid))
            pickle.dump(l,f)
    else:
        with open("faculty.dat","wb") as f:
                pickle.dump([f1.Faculty(name,eid)],f)
    return True
#*************************************************************************************************************************
def remove_Faculty(eid):
    with open("Faculty.dat","rb") as f:
            l=pickle.load(f)
            if l==[]:
                return False
            for i in l:
                if(i.eid==eid):
                    if(len(i.book_issued)!=0):
                        print("Faculty having some BOOK ,can't delete")
                        return False
                        
                    re=1
                    l.remove(i)
                    break
    with open("faculty.dat","wb") as f:
        pickle.dump(l,f)
    if(re==1):
        return True
    else:
        return False
#*************************************************************************************************************************
def add_book():
    title=input("enter the title of the book \n")
    author=input("enter the name of author of the book \n")
    while 1:
        isbn=input("enter the 13 digit isbn of the book \n")
        if len(isbn)==13:
            break
        else:
            c=input("invalid ISBN \n1.Try Again\n2.Cancle\n")
            if c=='2':
                return
    ncopy=int(input("enter the number of copies\n "))
    if(os.stat("book.dat").st_size != 0):
        with open("book.dat","rb") as f:
            l=pickle.load(f)
            for i in l:
                if(i.isbn==isbn):
                    i.numofcopies+=ncopy
                    i.avail+=ncopy
                    return True
        with open("book.dat","wb") as f:
            l.append(b.Book(title,author,isbn,ncopy))
            pickle.dump(l,f)
    else:
        with open("book.dat","wb") as f:
            pickle.dump([b.Book(title,author,isbn,ncopy)],f)
    return True
#*************************************************************************************************************************
def del_book(isbn):
    with open("book.dat","rb") as f:
        l=pickle.load(f)
        for i in l:
            if(i.isbn==isbn):
                if(i.avail==i.numofcopies):
                    l.remove(i)
                    break
                else:
                    print("Some copies of the Book issued to users,try again ")
                    return False
        else:
            return False
    with open("book.dat","wb") as f:
        pickle.dump(l,f)
    return True
#*************************************************************************************************************************    
def update_book(isbn):
    with open("book.dat","rb") as f:
        l=pickle.load(f)
    for i in l:
        if i.isbn==isbn and i.avail==i.numofcopies:
            print("\nOnly filled those field in which you want update otherwise nothing have to fill\n")
            title=input("Book Title:")
            if title:
                i.title=title
            author=input("Author:")
            if author:
                i.author=author
            isbn=input("ISBN: ")
            if isbn:
                i.isbn=isbn
            num=input("Copies: ")
            if num:
                i.numofcopies=num
            with open("book.dat","wb") as f:
                pickle.dump(l,f)
                print("Book Updated!!")
                if input("Press enter for back")=='':
                    return
    print("Book is Unavailable in Library Records or Book is issued to the users!!")
    if input("Press enter for back")=='':
        return
        

#*************************************************************************************************************************
def update_student(eno):
    with open("student.dat","rb") as f:
        l=pickle.load(f)
    for n,i in enumerate(l):
        if i.eno==eno and len(i.book_issued)==0:
            print("print only those thing which you want to update")
            name=input("Student Name:")
            if name:
                i.name=name
            year=input("Admission Year:")
            if year:
                i.year=year
            branch=input("Branch:")
            if branch:
                i.branch=branch
            if adid:
                i.adid=adid
                print("Student Data Updated!!")
            with open("student.dat","wb") as f:
                pickle.dump(l,f)
                if input("Press enter for back")=='':
                    return
    print("Student is Unavailable in Library Records Or Student having issued Books !!")
    if input("Press enter for back")=='':
        return
    
    
#*************************************************************************************************************************
def update_faculty(eid):
    with open("faculty.dat","rb") as f:
        l=pickle.load(f)
    for i in l:
        if i.eid==eid and len(i.book_issued)==0:
            print("\nOnly filled those field in which you want update otherwise nothing have to fill\n")
            name=input("Employee Name:")
            if name:
                i.ename=name
            with open("faculty.dat","wb") as f:
                pickle.dump(l,f)
                print("Faculty Data Updated!!")
                if input("Press enter for back")=='':
                    return
    print("Faculty  is Unavailable in Library Records Or Faculty has issue books !!")
    if input("Press enter for back")=='':
        return
    
#*************************************************************************************************************************

def show_students():
    try:
        with open("student.dat","rb") as f:
            l=pickle.load(f)
            if(l==[]):
                print("No record found")
                if(input('press enter for back')==''):
                    return  
            print("\n***Student Details*****\n")
            print(" Name         \t      Branch \t Enrollment Number\tBook issued")
            print("*********************************************************************")
            for i in l:
                print(f"{i.name}      \t{i.branch}\t  {i.eno}    \t{len(i.book_issued)}")
    except EOFError:
        print("No record found")
    if input("press enter for back:")=='':
        return
#*************************************************************************************************************************
def show_faculties():
    try:
        with open("faculty.dat","rb") as f:
            l=pickle.load(f)
            if(l==[]):
                print("No record found!")
                if input("press enter for back")=='':
                    return
            print("\n***Faculty Details*****\n")
            print(" name       \t  id  \t  Book issued ")
            print("************************************")
            for i in l:
                    print(f"{i.ename} \t       {i.eid}\t  {len(i.book_issued)}")
    except EOFError:
        print("No record found !")
    if input()=='':
        return
#*************************************************************************************************************************
def show_books():
    try:
        with open("book.dat","rb") as f:
            l=pickle.load(f)
            if(l==[]):
                print("No record found!")
                if input("press enter for back:")=='':
                    return
            print("\n***Book Details*****\n")
            print(" Title         \tAuthor         \tISBN       \tCopies       \t Available Copies")
            print("******************************************************************************************")
            for i in l:
                print(f"{i.title}  \t{i.author}   \t{i.isbn}  \t{i.numofcopies}        \t{i.avail} ")
    except EOFError:
        print("No record found")
    if input("press enter for back")=='':
        return
#*************************************************************************************************************************            
def issue_book_student(en,mode):
    with open("student.dat","rb") as f:
        l=pickle.load(f)
        for i in l:
            if(i.eno==en):
                isbn=input("enter the book isbn to issue\n")
                with open("book.dat","rb") as f1:
                    l1=pickle.load(f1)
                    for i1 in l1:
                        if(i1.isbn==isbn):
                            if(isbn in i.book_issued):
                                print("this book already issued to this student")
                            elif i1.avail<1:
                                print("book are exahused!!")
                            elif len(i.book_issued)<5:
                                if(mode=='a'):
                                    rdays=int(input("Enter the Days for Book is issued\n"))
                                else:
                                    rdays=30
                                idate=date.today()
                                rdate=idate+timedelta(rdays)
                                i.book_issued[isbn]=[i1.title,idate,rdate]
                                i1.students[i.name]=[i.eno,rdate]
                                i1.avail-=1
                                print( "book issued")
                            else:
                                print( "student reached maximum limit of there books!!")
                            with open("student.dat","wb") as f:
                                pickle.dump(l,f)
                            with open("book.dat","wb") as f:
                                pickle.dump(l1,f)
                            return
                    else:
                        print("book for this isbn not exist!") 
                        return
    print("student not exist!!")
#*************************************************************************************************************************            
def issue_book_faculty(en):
    with open("faculty.dat","rb") as f:
        l=pickle.load(f)
        for i in l:
            if(i.eid==en):
                isbn=input("enter the book isbn to issue\n")
                with open("book.dat","rb") as f1:
                    l1=pickle.load(f1)
                    for i1 in l1:
                        if(i1.isbn==isbn):
                            n=int(input("enter the number of copies to be want \n"))
                            if(isbn in i.book_issued and i1.avail>=n):
                                i.book_issued[isbn][2]+=n
                                i1.avail-=n
                                i1.faculties[i.ename]=[i.eid,n]
                            elif i1.avail<n:
                                if i1.avail<1:
                                    print("book are exahused!!")
                                else:
                                    print(f"only {i1.avail} left")
                                    return
                            else:
                                  i.book_issued[isbn]=[i1.title,str(date.today()),n]
                                  i1.avail-=n
                                  i1.faculties[i.ename]=[i.eid,n]
                            with open("faculty.dat","wb") as f:
                                pickle.dump(l,f)
                            with open("book.dat","wb") as f:
                                pickle.dump(l1,f)  
                            print("book issued")
                            return 
                    else:
                        print("book for this ISBN not exist!")
                    return

        print("faculty of this id not exist") 
#*************************************************************************************************************************
def search_book():
    while(1):
        f=open("book.dat","rb")
        l=pickle.load(f)
        c=input("1.search by Title\n2.search by ISBN\n3.search by author\n4.back\n")
        if c=='1':
            d=input("\nenter the name of the book to be search\n")
            flag=0
            print("   Title       \t         Author  \tISBN \t Available")
            for i in l:
                if i.title==d:
        
                    print("********************************************************************")
                    print(f"{i.title}    \t{i.author} \t {i.isbn}\t   {i.avail}")
                    flag=1
          
            if flag==1:
                print("please notedown the book ISBN for issue purpose")
            else:
                print("This book not available try again !")
        if c=='2':
            d=input("enter the 13 digit ISBN Number\n")
            if(len(d)!=13):
                print("invalid ISBN try again!!")
            else:
                flag=0
                for i in l:
                    if i.isbn==d:
                        print("   Title       \t         Author  \tISBN \t Available")
                        print("********************************************************************")
                        print(f"{i.title}    \t{i.author} \t {i.isbn}\t   {i.avail}")
                        print("please notedown the book ISBN for issue purpose")        
                if flag==0:
                    print("This book not available try again !")
        if c=='3':
            d=input("enter book Author name \n")
            print("   Title       \t         Author  \tISBN \t Available")
            print("********************************************************************")
            flag=0
            for i in l:
              
                
                if i.author==d:
                    #print("   Title       \t         Author  \tISBN \t Available")
                   
                    print(f"{i.title}    \t{i.author} \t {i.isbn}\t   {i.avail}")
                    flag=1
            print("********************************************************************")
            if flag==1:
                print("please notedown the book ISBN for issue purpose")
            else:
                print("This book not available try again !")
        if c=='4':
            break
#*************************************************************************************************************************   

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return ((d1 - d2).days)
#*************************************************************************************************************************   
def return_book(en):
    if(len(en)>5):
        if(chek(en)):
            isbn=input("enter book ISBN Number to be return\n")
            if(chekissued(en,isbn)):
                with open("student.dat","rb") as f:
                    l=pickle.load(f)
                    for i in l:
                        if i.eno==en:
                            chek1=calculate_fine(en,i,isbn)
                            if(chek1):
                                print(f"pay fine of RS {chek1}")
                                c=input("1.pay\n2.not pay\n")
                                if c=='1':
                                    i.book_issued.pop(isbn)
                                    book_put(i.name,isbn)
                                if c=='2':
                                    print("book not return due to fine")
                            else:
                                i.book_issued.pop(isbn)
                                book_put(i.name,isbn)
                                
                with open("student.dat","wb") as f:
                    pickle.dump(l,f)
                    
            else:
                print("This bookis not allocated to this student")
        else:
            print("student doesn't exist")
    else:
        if(chek(en)):
            isbn=input("enter ISBN number of book to be return\n")
            if chekissued(en,isbn):
                with open("faculty.dat","rb") as f:
                    l=pickle.load(f)
                    for i in l:
                        if i.eid==en:
                            while(1):
                                n=int(input(f"this faculty having {i.book_issued[isbn][2]} copies how much have to submit\n"))
                                if(n<=i.book_issued[isbn][2]):
                                    break
                                else:
                                    print("please enter less or equal to the copies user have")
                                    
                            if(n==i.book_issued[isbn][2]):
                                i.book_issued.pop(isbn)
                            else:
                                i.book_issued[isbn][2]-=n
                            book_put(i.eno,isbn,n)
                with open("faculty.dat","wb") as f:
                    pickle.dump(l,f)
                    
                            
            else:
                print("this faculty not issued this book can't return")
        else:
            print("faculty with this id not exist")
#*************************************************************************************************************************   
def chek(en):
    if len(en)>5:
        with open("student.dat","rb") as f:
            for i in pickle.load(f):
                if i.eno==en:
                    return True
        return False
    else:
        with open("faculty.dat","rb") as f:
            for i in pickle.load(f):
                if i.eid==en:
                    return True
        return False
 #*************************************************************************************************************************      
def chekissued(en,isbn):
    if(len(en)>5):
         with open("student.dat","rb") as f:
            for i in pickle.load(f):
                if i.eno==en:
                    return isbn in i.book_issued
    else:
        with open("faculty.dat","rb") as f:
            for i in pickle.load(f):
                if i.eid==en:
                    return isbn in i.book_issued
#*************************************************************************************************************************  
def calculate_fine(en,ref,isbn):
        days=days_between(str(date.today()),str(ref.book_issued[isbn][2]))
        if days>0:
            return days*5
        return 0
#*************************************************************************************************************************  
def book_put(name,isbn,n=1):
    with open("book.dat","rb") as f:
        l1=pickle.load(f)
    for i1 in l1:
        if i1.isbn==isbn:
            if n==1:
                i1.students.pop(name)
            else:
                if(i1.faculties[name][1]==n):
                    i1.faculties.pop(name)
                else:
                    i1.faculties[name][1]-=n
    with open("book.dat","wb") as f1:
        pickle.dump(l1,f1)
    print("book return successefully")
#************************************************************************************************************************* 
def passchek_student(eno,passwrd):
    with open("student.dat","rb") as f:
        l=pickle.load(f)
    for i in l:
        if i.eno==eno:
            if i.passwrd==passwrd:
                return True
            else:
                return False
    return False
 #*************************************************************************************************************************
def passchek_faculty(id,passwrd):
    with open("faculty.dat","rb") as f:
        l=pickle.load(f)
    for i in l:
        if i.eid==id:
            if i.passwrd==passwrd:
                return True
        else:
                return False
    return False
 #*************************************************************************************************************************
def change_pass_student(eno):
     with open("student.dat","rb") as f:
        l=pickle.load(f)
     for i in l:
        if i.eno==eno:
            while(1):
                if i.passwrd==getpass.getpass("enter current password\n "):
                    i.passwrd=getpass.getpass("enter new password\n")
                    print("password changed successfully!")
                    break
                else:
                    print("wrong current password!")
                    c=input("1.Try again\n2.back\n")
                    if c=='1':
                        pass
                    elif c=='2':
                        print("password not changed")
                        return
     with open("student.dat","wb") as f:
        pickle.dump(l,f)
     return 
 #*************************************************************************************************************************
def change_pass_faculty(eid):
     with open("faculty.dat","rb") as f:
        l=pickle.load(f)
     for i in l:
        if i.eid==eid:
            while(1):
                if i.passwrd==getpass.getpass("enter current password\n "):
                    i.passwrd=getpass.getpass("enter new password\n")
                    print("password changed successfully!")
                    break
                else:
                    print("wrong current password!")
                    c=input("1.Try again\n2.back")
                    if c=='1':
                        pass
                    elif c=='2':
                        print("password not cahnged")
                        return
     with open("faculty.dat","wb") as f:
        pickle.dump(l,f)
     return T
 #*************************************************************************************************************************
def view_record_student(eno):
    with open("student.dat","rb") as f:
        l=pickle.load(f)
    for i in l:
        if i.eno==eno:
            print("\n***Student Information****\n")
            print(f"Name : {i.name}\nBranch: {i.branch}\nEnrollment Number: {i.eno}")
            print("***Book Details***")
            print("\nBook Title   \tBook ISBN    \t  Book Issue Date \t Book Return Date")
            print("************************************************************************")
            for i1 in i.book_issued:
                print(f"{i.book_issued[i1][0]}    \t{i1}      \t{i.book_issued[i1][1]}  \t{i.book_issued[i1][2]}")
            
            if input("press enter for back:")=='':
                return
 #*************************************************************************************************************************
def view_record_faculty(eid):
    with open("faculty.dat","rb") as f:
        l=pickle.load(f)
    for i in l:
        if i.eid==eid:
            print("\n***Faculty Information****\n")
            print(f"Name : {i.ename}\nID: {i.eid}\n")
            print("\n***Book Details***\n")
            print("\nBook Title \t       Book ISBN \t     Book Issue Date\t Copies")
            print("********************************************************************")
            for i1 in i.book_issued:
                print(f"{i.book_issued[i1][0]}   \t{i1}    \t{i.book_issued[i1][1]}  \t{i.book_issued[i1][2]}") 
            if input("press enter for back:")=='':
                return
 #*************************************************************************************************************************
def view_book_record(isbn):
    with open("book.dat","rb") as f:
        o=pickle.load(f)
    for i in o:
        if i.isbn==isbn:
            print("\n***Book Information****\n")
            print(" Book name\tISBN")
            print("*"*20)
            print(f"{i.title}\t {i.isbn}")
            if i.numofcopies==i.avail:
                print("\nThis Book is not issued to Anyone")
                return
            if len(i.students)!=0:
                print("\nBook issued to the Students!!\n")
                #print("********************************\n")
                print("Name\tEnrollemnt Number\tDate of Return")
                print("****************************************")
                for l in i.students:
                        print(f"{l}\t{i.students[l][0]}\t{i.students[l][1]}")
            if len(i.faculties)!=0:
                              print("\nBook issued to the Faculties!!\n")
                              print("****************************************")
                              print("Name\tEmployee Id\tNumber of copies")
                              for l in i.faculties:
                                    print(f"{l}\t{i.faculties[l][0]}\t{i.faculties[l][1]}")
                                  
            if input("press enter for back:")=='':
                return
                              
    print("This Book not exist!!")     
    if input("press enter for back:")=='':
        return
#*****************************************************************************************************************        
def reissue(en):
    if(chek(en)):
        isbn=input("enter book ISBN Number to be Re-issue\n")
        if(chekissued(en,isbn)):
            with open("student.dat","rb") as f:
                l=pickle.load(f)
            for i in l:
                if i.eno==en:
                    if(calculate_fine(en,i,isbn)):
                        print("Can't issue these book exceed return date ")
                        return
                    i.book_issued[isbn][2]+=timedelta(30)
                    i1=i
                    break
            with open("book.dat","rb") as f1:
                m=pickle.load(f1)
            for j in m:
                if j.isbn==isbn:
                    print(j.students)
                    j.students[i1.name][1]+=timedelta(30)
            with open("book.dat","wb") as f:
                    pickle.dump(m,f)
            with open("student.dat","wb") as f:
                pickle.dump(l,f)
            print("book reissued!!")
        else:
            print("This bookis not allocated to this student")
    else:
        print("student doesn't exist")
#*****************************************************************************************************************
def Clear_library_record():
    c=input("Are you Sure to Clear All Library Record ,Your All Data Will be Delete Parmanently\n1.Sure\n2.Cancle\n")
    if c=='2':
        return
    with open("student.dat","wb") as f:
        pickle.dump([],f)
    with open("faculty.dat","wb") as f:
        pickle.dump([],f)
    with open("book.dat","wb") as f:
        pickle.dump([],f)
    print("All Library Record Deleted!!")
#*****************************************************************************************************************
def change_pass_admin():
    with open("adpass.txt","r+") as f:
        chek=f.read()
    while(1):
        passwd=getpass.getpass("enter current password\n")
        if(passwd==chek):
            newpass=getpass.getpass("enter New Password \n")
            with open("adpass.txt","w") as f:
                f.write(newpass)
            print("password changed successfully!")
            if input("press enter for back")=='':
                return
            
        else:
            c=input("Wrong current password \n1.Try again\n2.Cancle\n")
            if c=='2':
                print("password  not changed")
                break
    f.close()
      