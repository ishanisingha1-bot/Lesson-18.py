#Creating a tuple with different data types
tuplex=("tuple",True,3.2,1)
print(tuplex)
tuplex=(4,6,2,8,3,1)
print(tuplex)
#You cannot add new elements to tuples
#using + operator you can merge tuples
tuplex=tuplex+(9,)
print(tuplex)
#Count number of occurences of an elemnt in a tuple
tuple1=(50,60,10,70,50)
print(tuple1.count(50))
#creating a tuple
tuple=(2,4,3,5,4,6,7,8,4,9,10)
#slicing a tuple
_slice=tuplex[3:5]
print(_slice)
_slice=tuplex[:6]
print(_slice)