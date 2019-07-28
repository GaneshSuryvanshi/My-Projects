import funtions.functions as m
import getpass,os
def student_mode():
    while(1):
        userid=input("enter User Id/Enrollment Number\n")
        passwrd=getpass.getpass("enter password\n")
        if(m.passchek_student(userid,passwrd)):
            while(1):
                c=input("****MENU****\n1.View Record\n2.Search Book\n3.Issue Book\n4.Re-issue Book\n5.See all Available Books!\n6.Change password\n7.Logout\n")
                if c=='1':
                    m.view_record_student(userid)
                elif c=='2':
                    m.search_book()
                elif c=='3':
                    m.issue_book_student(userid)
                elif c=='4':
                    m.reissue(userid)
                elif c=='5':
                    m.show_books()
                elif c=='6':
                    m.change_pass_student(userid)
                elif c=='7':
                    break
            break
        else:
            print("wrong userid or password")
            c=input("press 1 for try again else press 2 for Cancle\n")
            if c=='1':
                pass
            else:
                return
        
