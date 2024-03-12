# Mutable data types -->    ~List    ~Dictionary    ~Byte array

# Immutable data types -->  ~int     ~Float         ~Complex       ~String      ~tuple      ~set

a = 10  # int
b = 2.0  # Float
c = 1 + 2j  # Complex in complex we use j rather than i

print(a, type(a))  # type() function returns the data type of the variable
print()
print(b, type(b))
print()
print(c, type(c))
print()
print('-------    -------- STRING ----------    --------------')
# Multiline strings can be written using triple quotes ''' or """

s = "This is a string "
print(s, type(s))
print()
s1 = ''' Hello !!!!
This is the multiline string '''
print(s1, type(s1))
print()
print('------ -----      LIST  ---------  --------')

# List is mutable data type ... always defined in square brackets

l = [10, 'ws', 5.5]
print(l, type(l))
l[2] = 10
print()
print(l, type(l))
print()

# Tuple is immutable , unordered ...........defined with () and is fast than list

print("--------------- ------- TUPLE --------- ---------------------")

t = (1, 20, 'hello ')
print(t, type(t))
# t(1) = 30  --- ERROR as tuple is immutable
print()

print("--------------- ------- Dictionary --------- ---------------------")
print()
# Dictionary --- unordered , key-value pair , keys are unique , defined with {} , pairs are as key:value
d = {
    'name': 'python ',
    'duration': '2 months'
}
print(d, type(d))
var = d['name']  # accessing values through keys
print(var)
print()

print("--------------- ------- SET --------- ---------------------")
print()

# set -- unordered , unique elements , immutable , defined with {}

st = {1, 2, 3, 4, 5}
print(st, type(st))
st1 = {1, 2, 3, 4, 5, 1}
print(st1)    # here interpreter removes double 1 from st1 because set have only unique values

