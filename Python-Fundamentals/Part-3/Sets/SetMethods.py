# .add(val) - adds a value
# .remove(val) - removes a values
# .clear() - empties a set
# .pop() - removes arandom values
# .union(set2) - returns new union
# .intersection(set2) - returns new intersection

s={1,2,3,4,2,2,6,8,2,78,2}
s2={3,6,2,9,54,76,25,876,78,2}

s.add(34)
print(s)

s.remove(34)
print(s)

print(s.pop())

print("Union of s and s2 = " , s.union(s2))
print("Intersection of s and s2 = " , s.intersection(s2))


s.clear()
print(s)