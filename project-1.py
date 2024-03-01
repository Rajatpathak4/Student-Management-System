print("_____________________________________\n ")
print("WELCOME TO STUDENT MANAGEMENT SYSTEM")
name=open("database.txt","a+")
def view_stud():
    name=open("database.txt","r")
    for i in name:
        print(i)
    name.close()

def add_stud():
    name=open("database.txt","a+")
    a=input("Enter the name: ")
    a=a+"\n"
    name.write(a)
    print("Student name Added Successfully")
    name.close()

def remove_stud():
    name=open("database.txt","r")
    a=input("Enter the name: ")
    a=a+'\n'
    name.seek(0)
    rn=name.readlines()
    if a in rn:
        rn.remove(a)
        print("Removed Student name from List",a)
        s=''
        s=''.join([str(i) for i in rn])
        f1=open("database.txt","w")
        f1.write(s)
        f1.close()
    else:
        print("student not found")
    name.close()

def search_stud():
    name=open("database.txt","r")
    a=input("Enter the name to Search: ")
    result=name.read()
    if a in result:
        print("Name Found")
    else:
        print("Name not Found")

while True:
    print("_____________________________________")
    print("PLEASE CHOOSE ONE OPTION:\n")
    print("1. To View Student List")
    print("2. To Add New List")
    print("3. To Remove The Data")
    print("4. To Search Data ")
    print("5. EXIT")
    
    ch=int(input("Enter your choice:"))
    if ch==1:
        view_stud()
    elif ch==2:
        add_stud()
    elif ch==3:
        remove_stud()
    elif ch==4:
        search_stud()
    elif ch==5:
        exit()
    else:
        print("Wrong Input")


    g=input("Do you want to continut(Y/N):")
    if(g=="y"):
        continue
    elif(g=="n"):
        break


