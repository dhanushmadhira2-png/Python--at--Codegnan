#To perform operators
print("Arithematic operator")
print("Addition")
a = 20
b = 10
print(a+b)
print("Subtraction")
print(a-b)
print("Multiplication")
print(a*b)
print("Division")
print(a/b)
print("Floor Division")
print(a//b)
print("Modulus")
print(a%b)
print("Exponential")
print(a**b)

print("Assignment opetrator")
a = 10
a+=10#a+=10 is writen as a=a+10
print(a)
a-=10
print(a)
a*=10
print(a)
a/=10
print(a)
b//=10
print(b)
b%=10
print(b)
b**=10
print(b)

print("Relational operator")#it defines the relation between to values and gives the output in boolean type
a = 10
b = 20
print(a<b)
print(b>a)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)

print("logical operator")
print(3<5 and 4<5)#in this both values are true then only output true
print(4>5 and 6<5)
print(5>4 and 4!=5)
print(-9>1 and 0<1)

print("or operator")
print(3<5 or 4<2)#in this any one value is true then 
print(4<6 or 5<7)
print(4==4 or 5<6)

print("not operator")#in this the output wil be inverese operation
a = 10
b = 20

print(not (a < b))
a = 2
b = 3
print(not (b<a))
print(not (a!=b))
print(not (a>b))

a = 10 # left shift
print( a << 2)

a = 10 # right shift
print(a >> 2)

#Membership and Identify operartor


numbers = (10 , 20, 30, 40)
print(20 in numbers)

numbers = (10 , 20, 30, 40)
print(20 not in numbers)

#identify operator
a = [10, 20, 30]
b = a
print(a is not b)







