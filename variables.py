# Arthimetic Operations
print(58+63)
print(58-63)
print(58*63)
print(58/63)
# The above mentioned is not correct way to perform arithmetic operation
#  because there may be a chance of typing wrong digits and also time consuming 
# so, to overcome this we use variables here we assign the values to a variable 
# so, that we can use the Variables instead of entering the no's.

#Using Variables
# * Used To Refer a Memory Block

a=45
b=82
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a % b)

# Strings -- Sequence Of Characters.
# Space is also Character and we will denote in 'Single_Qoute' and "Double_Qoutes".
#examples
X='str'
#print(x) # Here it will throw an Error NameError: name 'x' is not defined because it is "Case-Sensitive"
print(X) # The output will be -- str
# To know the type of the Variable we use type
print(type(X))
# To know the Length of the Variable we use len
print(len(X))

#Slicing
y="Naa Mate_Nene Vinanu"
print(y[5])  #Index it will denote in [Square Brackets]
print(y[2 : 9])  # in place of index valu 9 it will give the 8 value because it will consider upper boundary -1
print(y[-3])  # -ve indexing from last it will show the output in this case the o/p will be "a"
print(y[1 : 11 : 2]) # the last digit 2 defines that from the range 1 to 11 it has to skip 1 letter ex the o/p will be a aeN
print(y[-2 : -10 : -1]) # in -ve indexing o/p will be in reverse

# If u want to change any Character in a string we can use y[5]="g" in other lang. like c,c++ it is possible
# In Python change of character is not posible because of its "Immutable Property" 
# It is possible when u want to replace or change the Entire string because it will store in different memory addres
# To know the Memory Address of a Var 
var = "ip_address"
var = 'ip_address'
print(id(var))  # same ip address will be printed because it will refer to same memory block due same value
var_2 ="ip_1"
print(id(var_2))  #store in different memory location 

# Complex Numbers  
x = 2+5j
y = 4+2j
print(type(x))
print(x+y) #using Arithmetic Operations
print(x-y)
print(x*y)
print(x/y)
print(x**y)
#print(x // y)
#print(x % y)

# Boolean  - true or false
print(32.5 > 32)
print(76 <= 76)
print(95 < 58)
 # To know the integer value of true or false
print(int(False))


#lists - It is Muttable we can the item or elements present in the list and denoted in [Square brackets with ,]
new_list=[2,3,4,"lists",False,[9,"int",5]]
print(type(new_list))
print(len(new_list))
print(new_list[4])
print(new_list[-6])
print(new_list[2 : 5 : 1])
# To access the list of the sublist
print(new_list[5][1])
new_list[5][1] = "float"  # here we can the value of int to float so, it is Muttable
print(new_list[-1 : -5])
print(len(new_list[3]))  # It gives the length of the False

# Tuple  - It is Immutable we can't change the elements
tup1 = (9,8,7,6,[2,5,8],"Tuple")
print(type(tup1))
print(len(tup1))
#tup1[-3] = "hello" # Immutable we cant change elements one's assgined in variable
print(type[1 : 4])
print(tup1[2:6:1])
print(tup1[-1:-5:-2]) 






