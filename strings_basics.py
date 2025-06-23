# positive indexing
str1="My Name Is Prince"
print("One character from index 3 of str1",str1[3])

#negative Indexing
str2="I Am Student"
print("Second last character from str2",str2[-2])

#string slicing
str3="Engineer"
print("One character from slicing with step",str3[0:2:5])

#negative slicing
str4="Technology"
print("Reverse of Technology",str4[::-1])

#concatenation
str5="Tech"
str6="Prince"
str7=str5+str6
print("Concatenated string=",str7)

#String Formatting Examples ---

name = "Prince"
course = "Python"
marks = 95.456

# 1. Using format() method
print("Hello {}, welcome to {} course!".format(name, course))

# 2. Using f-string (recommended)
print(f"Hey {name}, you scored {marks:.2f} marks in {course}.")

# 3. Percentage formatting (old style)
print("Student %s has %.1f marks in %s." % (name, marks, course))
