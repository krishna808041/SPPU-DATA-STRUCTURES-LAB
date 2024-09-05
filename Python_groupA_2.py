"""
Experiment Number 2 : Write a python program to store marks stored in subject "Fundamentals of Data Structure" by
                         N students in the class. Write functions to compute following:
                         1. The average score of the class.
                         2. Highest score and lowest score of the class.
                         3. Count of students who were absent for the test.
                         4. Display mark with highest frequency.
"""




#--------------------------------------------------------Functions To be created-------------------------------------------------------
def ab(n, marks):
    c = 0
    for i in range(0, n):
        if marks[i] == -999:
            c += 1
    return c

def handl(m, n):
    h = m[0]
    for i in range(1, n):
        if h < m[i]:
            h = m[i]
    l = m[0]
    for i in range(1, n):
        if l > m[i]:
            l = m[i]
    return h, l

def avg(a, ma):
    t = 0
    for i in range(0, a):
        t += ma[i]
    return t / a  # corrected the division to use 'a' instead of 2

def frequency(marks):
    same = []
    index = 0
    count_ini = 1
    for i in range(0, len(marks)):
        count_dyn = 1
        for j in range(i + 1, len(marks)):
            if marks[i] == -999:
                break
            if marks[i] == marks[j]:
                count_dyn += 1
        if count_dyn == count_ini:
            same.append(marks[index])
            same.append(marks[i])
            continue
        if count_dyn > count_ini:
            count_ini = count_dyn
            index = i
    if len(same) == len(marks):
        return same
    else:
        return marks[index]

def menu():
    flag = 9
    while flag == 9:
        print("\n\n----------MENU----------\n")
        print("1. The average score of class")
        print("2. Highest score and lowest score of class")
        print("3. Count of students who were absent for the test")
        print("4. Display mark with highest frequency")
        print("5. Exit")

        ch = int(input("Enter your choice :"))
        if ch == 1:
            b = avg(n, marks)
            print(b)
            b = input("Do you want to continue(yes/no)?")
            if b == "yes":
                flag = 9
            else:
                flag = 0
            print("Thanks for using this program :)")
        elif ch == 2:
            h, l = handl(marks, n)
            print("Highest Score is : ", h)
            print("Lowest Score is : ", l)
            b = input("Do you want to continue(yes/no)?")
            if b == "yes":
                flag = 9
            else:
                flag = 0
            print("Thanks for using this program :)")
        elif ch == 3:
            ans = ab(n, marks)
            print(ans)
            b = input("Do you want to continue(yes/no)?")
            if b == "yes":
                flag = 9
            else:
                flag = 0
            print("Thanks for using this program :)")
        elif ch == 4:
            ans = frequency(marks)
            print(ans)
            b = input("Do you want to continue(yes/no)?")
            if b == "yes":
                flag = 9
            else:
                flag = 0
            print("Thanks for using this program :)")
        elif ch == 5:
            flag = 0
        else:
            print("Enter valid choice")

#-----------------------------------------------------Main Code------------------------------------------------------------------

n = int(input("Enter the no of students : "))
marks = []
for i in range(0, n):
    m = int(input("Enter the marks of student : "))
    marks.append(m)
menu()
