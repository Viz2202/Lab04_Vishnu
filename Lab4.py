list1=[["161E90","Raman",41,56000],["161F91","Himadri",38,67500],["161F99","Jaya",51,82100],
       ["171G30","Ajay",45,44000],["171E20","Tejas",30,55000]]
print("Menu")
print("1.Name")
print("2.Age")
print("3.Salary")
ch=int(input("Enter your choice"))
if(ch==1):
    name=input("Enter name")
    for i in range(len(list1)):
        if(list1[i][1].lower()==name.lower()):
            print("Employee id: ",list1[i][0])
            print("Name: ",list1[i][1])
            print("Age: ",list1[i][2])
            print("Salary: ",list1[i][3])
            break
        else:
            print("Not Found")
elif(ch==2):
    name=int(input("Enter Age"))
    for i in range(len(list1)):
        if(list1[i][2]==name):
            print("Employee id: ",list1[i][0])
            print("Name: ",list1[i][1])
            print("Age: ",list1[i][2])
            print("Salary: ",list1[i][3])
            break
        else:
            print("Not Found")
elif(ch==3):
    name=int(input("Enter Salary"))
    op=input("Choose the operator out of (<,>,>=,<=)")
    if op==">":
        for i in range(len(list1)):
            if(list1[i][3]>name):
                print("Employee id: ",list1[i][0])
                print("Name: ",list1[i][1])
                print("Age: ",list1[i][2])
                print("Salary: ",list1[i][3])
            else:
                continue
    elif op=="<":
        for i in range(len(list1)):
            if(list1[i][3]<name):
                print("Employee id: ",list1[i][0])
                print("Name: ",list1[i][1])
                print("Age: ",list1[i][2])
                print("Salary: ",list1[i][3])
            else:
                continue
    elif op=="<=":
        for i in range(len(list1)):
            if(list1[i][3]<=name):
                print("Employee id: ",list1[i][0])
                print("Name: ",list1[i][1])
                print("Age: ",list1[i][2])
                print("Salary: ",list1[i][3])
            else:
                continue
    elif op==">=":
        for i in range(len(list1)):
            if(list1[i][3]>=name):
                print("Employee id: ",list1[i][0])
                print("Name: ",list1[i][1])
                print("Age: ",list1[i][2])
                print("Salary: ",list1[i][3])
            else:
                continue
    else:
        print("Invalid operator used")
else:
    print("Invalid Choice")