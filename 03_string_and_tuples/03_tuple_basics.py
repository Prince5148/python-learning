#tuple creation
tuple=(10,20,30,40,50)
print(tuple)                    #output (10, 20, 30, 40, 50) 

##accessing elements
tuple=(45,67,34,5,67)
print(tuple[1])                 #output 67

#Slicing
tuple=("mouse","keyboard","cpu","leptop")
print(tuple[0:2])              #output ('mouse', 'keyboard')
print(tuple[1:4])              #output ('keyboard', 'cpu', 'leptop')


#tuple method

#count method
tuple=("car","bike","truck","bus","car","car")
print(tuple.count("car"))      # 3


tuple=("python","java","c","c++")
print(tuple.index("java"))    #output 1
print(tuple.index("c++"))     #output 3

#Demonstrating immutability (TypeError)

tuple=(34,56,78,98,67)
print(tuple)
tuple[1]=34                #TypeError: 'tuple' object does not support item assignment


