# JSON :-

"""
JSON - Java Script Object Notation
JSON is used for data exchange mainly between browser and server
json works in key-value pairs
json supports data types like strings, number, boolean, null, object, array
Python supports JSON with built in package called json

"""
import json

d = dict(course='Python', fees=5000)
f = json.dumps(d)
print(f)  # {"course": "Python", "fees": 5000}
print(type(f))  # <class 'str'>  as it is json format not a dictionary


# Convert json to python object :-

js = '{"cname " : "python" , "fees" : 20000 , "duration" : "2 months"}'
x = json.loads(js)
print(x)  # {'cname ': 'python', 'fees': 20000, 'duration': '2 months'}
print(type(x))  # <class 'dict'>
# iterate : -
for i in x:
    print(i, x[i])
# list :-
jl = '[{"cname " : "python" , "fees" : 20000 , "duration" : "2 months"}]'
k = json.loads(jl)
print(k)
print(type(k))  # <class 'list'>


# reading and writing data in json file :-
"""
file = open("xyz.json", "r")
x = file.read()
finaldata = json.loads(x)
print(finaldata)
"""
