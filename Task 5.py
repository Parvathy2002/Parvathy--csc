# create a program of list of n integer values
n = 25
lst = [x for x in range(0,n)]
print("list = \n",lst)


# add an item in to the list
lst.append(86)
lst.insert(5,2)
print("list after adding an item:\n",lst)


#delete an item
lst.pop(20)    # in this 20 is the index no. not the item of list
lst.remove(15) # in this 15 is the item in the list
print("list after removing an item:\n",lst)

#largest no of the list
lar = max(lst)
print("largest no is:",lar)


# smallest no of the list
small = min(lst)
print("smallest no is:",small)


#create a tuple and print reverse of the created tuple
tup = (35,45,67,85,56,24,89)
print("tuple:\n",tup)
reverse = tup[::-1]
print("tuple after reversing :\n",reverse)


#create tuple and convert it into list
tup2 = (1,2,3,4,5,6,7,8,9)
list_2 = list(tup2)
print("tuple after coverting into list\n:",list_2)