import sys
import modes.adminmode as A,modes.studentmode as S,modes.facultymode as F
def main():
    try:
        while(1):
            i=input("1.admin\n2.student\n3.Faculty\n4.exit\n")
            if i=='1':
                A.admin_mode()
            elif i=='2':
                S.student_mode()
            elif i=='3':
                F.faculty_mode()
            elif i=='4':
                sys.exit(1)
    except SystemExit:
        print("Thank you for use our Library,hope you enjoyed so much!")