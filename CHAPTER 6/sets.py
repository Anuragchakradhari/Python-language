# sets are unindexed
# sets does not contain duplicate values

S = {} #Empty Dictionary
e = set() # Dont use  s={} ass it will create an empty dictionary
# element doesnt repeat in set and order is not organized

s= {1,5,32,54,5,5,5,"Harry"} # in output only single 5 will be printed

s.add(566) # Adds 566 in the set
print(s,type(s))
s.remove(1)
print(s,type(s))
s.pop()
print(s,type(s))

s1= {1,54,78,99}
s2={1,3,4,98,7}
print(s1.union(s2))
print(s1.intersection(s2))

print(s1-s2) #print s1 without the values which is common in both set
