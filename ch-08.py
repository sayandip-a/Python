my_list=[1,2,3,4,5]
print(my_list)


#append method
my_list.append(6)#append method adds a single element to the end of the list
print(my_list)

#extend method
my_list.extend([7,8,9])#extend method adds multiple elements to the end of the list
print(my_list)

#insert method
my_list.insert(2,16)#insert method adds an element at a specific index.
print(my_list)

#remove method
my_list.remove(16)#remove method removes the first occurrence of a specific element from the list.
print(my_list)

#pop method
my_list.pop(3)#pop method removes and returns the element at a specific index.
print(my_list)

#clear method
my_list.clear()#clear method removes all elements from the list, leaving it empty.  
print(my_list)

#count method
my_list=[10,15,9,45,23]
count = my_list.count(2)#count method returns the number of occurrences of a specific element in the list.
print(count)

#sort method
my_list.sort()#sort method sorts the elements of the list in ascending order.
print(my_list)

#reverse method
my_list.reverse()#reverse method reverses the order of the elements in the list.
print(my_list)