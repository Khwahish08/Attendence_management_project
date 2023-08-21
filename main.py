credentials={'admin':123}
n=len(credentials)
student={1:'Ariel', 2:'Belle', 3:'Chris', 4:'Dawn', 5:'Emily', 6:'Jason', 7:'Kristy', 8:'Leon', 9:'Millie', 10:'Nicolas'}
# def authentication(username, pwd):
#     for i in range(n):
#         if username==credentials[i] and pwd==credentials[i+1] and i%2!=0:
#             print("Successfully login")
#             tasks()
#         else:
#             print("Invalid username or password. Try again")
#             attempt=attempt-1


def tasks():
    ch=0
    while ch!='Q':
        print("Out of the following tasks")
        print("1. ADD STUDENT RECORD \n2. EDIT STUDENT RECORD \n3. VIEW STUDENT RECORD \n4. DELETE STUDENT RECORD")
        choice=int(input("Enter the task number which you want to perform:"))
        if choice==1:
            add()
        elif choice==2:
            edit()
        elif choice==3:
            view()
        elif choice==4:
            delete()
        else:
            print("Invalid choice")
        ch=input("press Q to logout\n")

    

def add():
    new_enroll=int(input("Enter enrollment number:"))
    new_name=(input("Enter name:"))
    if new_enroll in student:
        print("Record of ",new_enroll," already exist. Try again")
    else:
        student[new_enroll]=new_name
        print("Record added successfully")


def edit():
    enroll=int(input("Enter enrollment number:"))
    new_name=input("Enter new name:")
    if enroll in student:
       student[enroll]=new_name
       print("Record edited successfully")
    else:
        print("Record of ",enroll, "does not exist. Try again")


def view():
    enroll=int(input("Enter enrollment number:"))
    if enroll in student:
       print(student[enroll])
    else:
        print("Record of ",enroll, "does not exist. Try again")
        

def delete():
    enroll=int(input("Enter the enrollment number that you want to delete:"))
    if enroll in student:
       del student[enroll]
       print("Record deleted successfully")
    else:
        print("Record of ",enroll, "does not exist")
    


i=0
attempt=5
for i in range(5):
    print("Attempts left:", attempt)
    username=input("Enter the username:")
    pwd=int(input("Enter password:"))

    if username in credentials:
    # if username==credentials[j] and pwd==credentials[j+1] and j%2==0:
        print("Successfully login")
        tasks()
    else:
        print("Invalid username or password. Try again")
        attempt=attempt-1