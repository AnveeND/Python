# pickle is used to serialize and deserialize the python object structure
# i.e to store and retrive data

"""
- You can pickle objects with the following data types :-
  booleans, integers, floats, complex numbers, strings, tuples, lists, sets, dictionaries
- Pickle has two main methods :-
        - dump :- dumps object to file object (serialize an object hierarchy)
        - load :- loads an object from a file object (de-serialize a data stream)
- dump(obj, file)
- load(fileObject)
"""

import pickle
l = [10, 20, 30, 40]
f = open("datapickle.txt", "wb")               # wb indicates write binary
pickle.dump(l, f)
f.close()
f1 = open("datapickle.txt", "rb")              # rb indicates read binary
lo = pickle.load(f1)
print(lo)
