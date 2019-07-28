import funtions.functions as m
import getpass,os
def faculty_mode():
    while(1):
        userid=input("enter User Id/Employee ID:\n")
        passwrd= passwrd=getpass.getpass("enter password:\n")
        if(m.passchek_faculty(userid,passwrd)):
            while(1):
                c=input("****MENU****\n1.View Record\n2.Search Book\n3.Issue Book\n4.See all Available Books!\n5.Change password\n6.Logout\n")
                if c=='1':
                    m.view_record_faculty(userid)
                elif c=='2':
                    m.search_book()
                elif c=='3':
                    m.issue_book_faculty(userid)
                elif c=='4':
                    m.show_books()
                elif c=='5':
                    m.change_pass_faculty(userid)
                elif c=='6':
                    break
            break
        else:
            print("wrong employeeid or password")
            c=input("press 1 for try again else press 2 for main menu:\n")
            if c=='1':
                pass
            else:
                return
        
