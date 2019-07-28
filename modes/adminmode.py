import funtions.functions as m
import getpass,os
def admin_mode():
    userid=input("enter username: ")
    passwrd=getpass.getpass("enter password:")
    f=open("adpass.txt","r")
    if userid=="admin" and passwrd==f.read():
        while(1):
            c=input("1.Add Student\n2.Show Students\n3.Delete Student\n4.Add Faculty\n5.Show All Faculty\n6.Delete Faculty\n7.Add Book\n8.Delete Book\n9.Show Books\n10.Issue Book to Student\n11.Issue Book Faculty\n12.Re-issue Book to Student\n13.Show Student Record\n14.Show Faculty Record\n15.View Book Record\n16.Return Book\n17.Update Book\n18.Update Student Details\n19.Update Faculty Details\n20.Delete All Library Records\n21.Change Password\n22.Logout\n")
            
            if c=='1':
                c1=m.add_student()
                if(c1):
                    print("data entered Succesfully!!")
                    print("enrollment no is :",c1)
                else:
                    print("Can't add, student alredy exist!")
            elif c=='2':
                m.show_students()
            elif c=='3':
                en=input("enter the student enrollment number to delete\n")
                if(m.remove_student(en)):
                    print("student deleted!")
                else:
                    print("student not exist!")
            elif c=='4':
                if(m.add_faculty()):
                    print("added successfully!")
                else:
                    print("faculty of this employee id already exist!!")
            elif c=='5':
                m.show_faculties()
            elif c=='6':
                en=input("enter the fuculty employee id to be delete\n")
                if(m.remove_Faculty(en)):
                    print("faculty deleted!")
                else:
                    print("fuculty not exist!!")
            elif c=='7':
                if(m.add_book()):
                    print("book added")
                else:
                    print("not added")
            elif c=='8':
                isbn=input("enter the book isbn to be delete\n")
                if(m.del_book(isbn)):
                    print("book deleted!")
                else:
                    print("book not exist!!")
            elif c=='9':
                m.show_books()
            elif c=='10':
                eno=input("enter the enrollment of the student have to issue book\n")
                m.issue_book_student(eno,'a')
            elif c=='11':
                eid=input("enter employee id have to issue book\n")
                m.issue_book_faculty(eid)
            elif c=='12':
                m.reissue(input("enter student Enrollment Number have to Re-Issue Book\n "))
            elif c=='13':
                m.view_record_student(input("enter student Enrollment Number\n "))
            elif c=='14':
                m.view_record_faculty(input("enter Employee id Number\n "))
            elif c=='15':
                m.view_book_record(input("enter book's Isbn Number\n"))
            elif c=='16':
                en=input("enter student enrollment number or faculty's employee id which have to return book\n")
                m.return_book(en)
            elif c=='17':
                m.update_book(input("enter ISBN number of the book have to update :")) 
            elif c=='18':
                m.update_student(input("enter Enrollment number of  the Student have to update :")) 
            elif c=='19':
                m.update_faculty(input("enter Employee Number of the Faculty have to update :")) 
            elif c=='20':
                m.Clear_library_record()
            elif c=='21':
                m.change_pass_admin()
            elif c=='22':
                break
    
    else:
        print("Wrong username or password !!")
    
   
        