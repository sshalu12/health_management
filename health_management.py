def getdata():
    import datetime
    return datetime.datetime.now()
def lock(x):
    print("if you want to enter data for food press 1  ")
    print(" and if u want to enter data for ex press 2")
    d=int(input())
    print("for whom you want to lock the data")
    print("Press 1 for Shalu ")
    print("Press 2 for shubhi ")
    print("Press 3 for mayank ")
    k=int(input())
    
    if(k==1 and d==1):
        value=input("enter food :")
        with open("shalu_food.txt","a") as op:
            op.write(str([str(getdata())])+": "+value+"\n")
        print("successfully written")
    
    elif(k==2 and d==1):
        value=input("enter food :")
        with open("shubhi_food.txt","a") as op:
            op.write(str([str(getdata())])+": "+value+"\n")
        print("successfully written")

    elif(k==3 and d==1):
        value=input("enter food :")
        with open("mayank_food.txt","a") as op:
            op.write(str([str(getdata())])+": "+value+"\n")
        print("successfully written")
    elif(k==1 and d==2):
        value=input("enter excercise :")
        with open("shalu_ex.txt","a") as op:
            op.write(str([str(getdata())])+": "+value+"\n")
        print("successfully written")
    elif(k==2 and d==2):
        value=input("enter excercise :")
        with open("shubhi_ex.txt","a") as op:
            op.write(str([str(getdata())])+": "+value+"\n")
        print("successfully written")
    elif(k==3 and d==2):
        value=input("enter excercise :")
        with open("mayank_ex.txt","a") as op:
            op.write(str([str(getdata())])+": "+value+"\n")
        print("successfully written")


def ret(a):
    print("if you want to retrive data for food press 1  ")
    print(" and if u want to retrive data for ex press 2")
    d=int(input())
    print("which person data you want to retrive")
    print("Press 1 for Shalu ")
    print("Press 2 for shubhi ")
    print("Press 3 for mayank ")
    k=int(input())
    
    if(k==1 and d==1):
        
        with open("shalu_food.txt","rt") as op:
            print(op.read())
    
    elif(k==2 and d==1):
        
        with open("shubhi_food.txt","rt") as op:
            print(op.read())

    elif(k==3 and d==1):
        
        with open("mayank_food.txt","rt") as op:
            print(op.read())

    elif(k==1 and d==2):
        
        with open("shalu_ex.txt","rt") as op:
            print(op.read())

    elif(k==2 and d==2):
        
        with open("shubhi_ex.txt","a") as op:
            print(op.read())

    elif(k==3 and d==2):
        
        with open("mayank_ex.txt","a") as op:
            print(op.read())




print("if you want to lock the data press 1")
print("if you want to retrive the data press 0 ")
a=int(input())
if(a==1):
    lock(a)
else:
    ret(a)


