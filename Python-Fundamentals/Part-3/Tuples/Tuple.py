# Immutable Sequence of Values
# tuple = (1,2,3,4,5,6,7,8)

tup = (1,2,3,4,5)
print(tup)
print(type(tup))
print(len(tup))
print(tup[4])

#slicing in tuple
print(tup[2:5])
print(tup[3::1])
print(tup[::2])


tup1 = (1) # integer not an tuple
tup2 = ("abc") # srting not an tuple
tup3 = (1,) # tuple
print(type(tup1))
print(type(tup2))
print(type(tup3))