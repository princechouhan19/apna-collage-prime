# collection of unique elements
# cant accept mutable datatypes(dictionaryt,lists)

s={1,2,3,4,2,2,6,8,2,78,2}
print(s) #{1, 2, 3, 4, 6, 8, 78}
print(type(s)) #<class 'set'>
print(len(s)) #7
s.add(99)
print(s)

empty_set = {} #❌ type = dict
empty_set = set() #✅ type = set