s1= "ate"
s2 ="eat"

#method1 - using module
from collections import Counter
def anagram(s1,s2):   
    if Counter(s1)==Counter(s2):
        return(True)
    else:
        return(False)
print(anagram(s1,s2))        


#method2 -  using list n sorted function

list1=sorted(s1.lower())
list2=sorted(s2.lower())

print(list1==list2)