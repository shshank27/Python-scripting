#!/bin/python
import pdb
my_list = [1,2,3]
#pdb.set_trace()
print my_list
print (my_list * 2)
l = [1,2,3]
l.append('append me!')
print(l)
l.pop(0)
print(l)

print ('/n' "Iterate list")
cat_list = ["not eating", "not playing", "on a bed", "is sleeping"]

for state in cat_list:
    print("This cat is " + state)


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
numbers_in_order = sorted(numbers)

print(numbers)
print(numbers_in_order)

print(numbers)
print(numbers_in_order)   

#2	list.count(obj)
aList = [123, 'xyz', 'zara', 'abc', 123]
print ("Count for 123 : ", aList.count(123))
print ("Count for zara : ", aList.count('zara'))

#3	list.extend(seq)
aList = [123, 'xyz', 'zara', 'abc', 123]
bList = [2009, 'manni']
aList.extend(bList)
print("Extended List : ", aList) 

#4	list.index(obj)
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
print("Index for xyz : ", aList.index( 'xyz' )) 
print("Index for zara : ", aList.index( 'zara' )) 

#5	list.insert(index, obj)
aList = [123, 'xyz', 'zara', 'abc']
aList.insert( 3, 2009)
print("Final List : ", aList)

#6	list.pop(obj=list[-1])
aList = [123, 'xyz', 'zara', 'abc']
print("A List : ", aList.pop(1))
print("B List : ", aList.pop(2))
print(aList)

#7	list.remove(obj)
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.remove('xyz')
print("List : ", aList)
aList.remove('abc')
print("List : ", aList)

#8	list.reverse()
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.reverse()
print ("List : ", aList)

#9	list.sort([func])
aList = ['xyz', 'zara', 'abc', 'xyz']
aList.sort()
print("List : ", aList)

#Indexing, Slicing, and Matrixes
L = ['spam', 'Spam', 'SPAM!']
print(L[2])
print(L[-2])
print(L[1:])

users = ["user1","user2","user3"]
num= 123
users = [u+str(num) for u in users]
print (users)

list_number = [2,3,4,5]
square_list = [i**2 for i in list_number]
print (square_list)

