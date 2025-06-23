# Program to check grade based on marks using nested conditions

marks = float(input("Enter your marks out of 100: "))

if marks >=0 and marks <=100:
    if marks >=90:
        print("Grade A+: ")
    elif marks >=80:
        print("Grade A: ")
    elif marks >=70:
        print("Grade B: ")
    elif marks >=60:
        print("Grade C: ")
    elif marks >=50:
        print("Grade D: ")
    else:
        print("Grade (F) Fail")
else:
    print("Invalid Input")    

