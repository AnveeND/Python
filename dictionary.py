# Dictionary syntax :-
#                      d = {'name':'Python' , 'fees':8000 , 'time':'2 months'}

# instead of index , in dictionary we use keys to access data from dictionary


d = {'name': 'Python', 'fees': 8000, 'time': '2 months'}
print(d)
d1 = d['fees']
print("\nFees is : ", d1)  # Accessing one element using key
print()
print(len(d), type(d))
print()

# To get all data from dictionary we can use for loop

for n in d:
    # print(n)     -->  only print keys
    # print(d[n])  -->   print values

    print(n, " ", d[n])  # prints both keys and values

# Functions of dictionary :-
print("\nFunctions of dictionary :- \n")

# get() -->  pass key and it returns its value
n1 = d.get('name')
print("Name through get function is : ", n1)
print()
# keys() --> returns the keys of the dictionary
for a in d.keys():
    print(a)

# values() --> returns values
print()
for a in d.values():
    print(a)

# items --> Returns the keys as well as values
print()
for a, b in d.items():
    print(a, " --> ", b)

# Delete item from dictionary :-
print()
# del keyword --> using keys
del d['fees']
print(d)

# pop function --> deletes and returns the deleted element
print()
p = d.pop('time')
print(p)
print(d)

# To create dictionary --
print()

# dict() is used to create the dictionary , we have to pass variable name along with its values
dd = dict(name='cpp', fees=5000, time='2 months ')
print(dd)

# update in dictionary :-
print()

# update Function :-
dd.update({'time': '3 months'})
print(dd)

# or
print()
dd['fees'] = 5500
print(dd)

# To clear all values from the dictionary :-
print()
d.clear()
print(d)  # prints {} since dictionary is empty

# Adding an item in dictionary
print()
d['name'] = 'Python'  # if the key is already present in the dictionary its value gets updated
print(d)

# Nested dictionary

'''course1 = {
    'python': {'duration': '2 Months', 'fees': 5000},
    'java': {'duration': '5 Months', 'fees': 7000},
    'cpp': {'duration': '3 Months', 'fees': 4000},
}'''
# OR

course = dict(python={'duration': '2 Months', 'fees': 5000}, java={'duration': '5 Months', 'fees': 7000},
              cpp={'duration': '3 Months', 'fees': 4000})

print()
print(course)
print()

# print all details of python
print(course['python'])

print()

# To print only fees of python
print(course['python']['fees'])

print()

# To print all values :-

for i, j in course.items():
    print(i, "--> Duration is ", j['duration'], ", Fees is  ", j['fees'])

print()
for i, j in course.items():
    print(i, "--> Fees : ", j['fees'], ", Duration is  ", j['duration'])

# updating value in a nested dictionary -->
course['java']['fees'] = 8000
print()
print(course['java']['fees'])

# delete from nested dictionary
del course['java']['fees']
print()
print(course)
