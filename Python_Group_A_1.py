"""
       In second year computer engineering class, group A student's play cricket, group B students play badminton and group C students play football.
        Write a Python program using functions to compute following: -
        a) List of students who play both cricket and badminton
        b) List of students who play either cricket or badminton but not both
        c) Number of students who play neither cricket nor badminton
        d) Number of students who play cricket and football but not badminton.
        (Note- While realizing the group, duplicate entries should be avoided, Do not use SET built-in functions)
"""



def intersection(l1, l2):
    inter = []
    for i in l1:
        for j in l2:
            if i == j:
                inter.append(i)
            else:
                pass
    return inter




def union(l1, l2):
    u = []
    for i in l1:
        u.append(i)
    for i in l2:
        if i not in l1:
            u.append(i)
    return u




def difference(l1, l2):
    diff = []
    for i in l1:
        if i not in l2:
            diff.append(i)
    return diff




def menu():
    flag = 9
    while flag == 9:
        print("\n\n----------MENU----------\n")
        print("1. List of students who play both cricket and badminton\n")
        print("2. List of students who play either cricket or badminton but not both\n")
        print("3. Number of students who play neither cricket nor badminton\n")
        print("4. Number of students who play cricket and football but not badminton\n")
        print("5. Exit\n")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            print(intersection(cri, bad))
            b = input("Do you want to continue (yes/no)? ")
            if b == "yes":
                flag = 9
            else:
                flag = 0
                print("Thanks for using this program :)")
        elif ch == 2:
            a = union(cri, bad)
            c = intersection(cri, bad)
            ans = difference(a, c)
            print(ans)
            b = input("Do you want to continue (yes/no)? ")
            if b == "yes":
                flag = 9
            else:
                flag = 0
                print("Thanks for using this program :)")
        elif ch == 3:
            a = foot
            c = union(cri, bad)
            ans = difference(a, c)
            print(len(ans))
            b = input("Do you want to continue (yes/no)? ")
            if b == "yes":
                flag = 9
            else:
                flag = 0
                print("Thanks for using this program :)")
        elif ch == 4:
            a = union(cri, foot)
            c = bad
            ans = difference(a, c)
            print(len(ans))
            b = input("Do you want to continue (yes/no)? ")
            if b == "yes":
                flag = 9
            else:
                flag = 0
                print("Thanks for using this program :)")
        elif ch == 5:
            print("Thanks For Using Program!!")
            flag = 0
        else:
            print("Enter valid choice")




cri = []
foot = []
bad = []

n = int(input("Enter the total number of students who play cricket: "))
for i in range(0, n):
    c = int(input("Enter the roll number of students who play cricket: "))
    if c in cri:
        print("Student roll number already exists, try again ")
    else:
        cri.append(c)
print(cri)


n = int(input("Enter the total number of students who play football: "))
for i in range(0, n):
    c = int(input("Enter the roll number of students who play football: "))
    if c in foot:
        print("Student roll number already exists, try again ")
        m = int(input("Enter ANOTHER roll number of students who play football: "))
        foot.append(m)
    else:
        foot.append(c)
print(foot)


n = int(input("Enter the total number of students who play badminton: "))
for i in range(0, n):
    c = int(input("Enter the roll number of students who play badminton: "))
    if c in bad:
        print("Student roll number already exists, try again ")
        m = int(input("Enter ANOTHER roll number of students who play badminton: "))
        bad.append(m)
    else:
        bad.append(c)
print(bad)
menu()
