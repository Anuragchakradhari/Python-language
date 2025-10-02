# String are immutable
# string can also be written in single,and triple quotes 
a= "Anurag"
nameshort = a[0:3] # start from index 0 all the way till 3 , excludding 3
print(nameshort)
character1  = a[1]
print(character1)# print only n
character2  = a[-1]
print(character2) #print only g

# Negative Slicing
slice = a[-4:-1]
slice1 = a[2:5] #1+1 and 4+1
# both are same , only the style of writting changes
print(slice)
print(slice1)

# SKIP VALUE
word = "amazing"
word[1:6:2] #mzn
# word= [0:]= word[0:7] in case of "amazing"
# word= [:7]= word[0:7] in case of "amazing"