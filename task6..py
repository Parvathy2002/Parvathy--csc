#1) Write a Python script to merge two Python dictionaries
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
print("merged dic is:")
dict1.update(dict2)
print(dict1)
print()
#2) Write a Python program to remove a key from a dictionary
dic = {"Arun" : 50, "Anu" : 21, "Maan" : 16, "Harry" : 22}
print ("The dictionary before performing remove is : " + str(dic))
print()
del dic['Maan']
print ("The dictionary after remove is : " + str(dic))

print()
#3) Write a Python program to map two lists into a dictionary
d1=['a','b','c','d','e']
d2=[4,5,6,7,8]
res = {}
for i in d1:
    for j in d2:
        res[i] = j
        d2.remove(j)
        break  
print("Dictionary is: ")
print(str(res))


print()
#4) Write a Python program to find the length of a set
names={'abc','ab','qwerty','qaz','zxc','xyz','pqr','bcm'}
print("Number of names in Set is :",len(names))

print()
#5) Write a Python program to remove the intersection of a 2nd set from the 1st set

a={1,5,9,7,6,8,2,4,3,10}
b={2,4,5,9}
print(a.intersection(b))