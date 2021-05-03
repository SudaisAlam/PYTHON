"""
~tuples are used to store multiple items in a single variable.
~tuples are ordered and have index numbers.
~tuples are unchangable, means you cannot add or remove an item to a tuple
~Always add a comma in a tuple containing single item, otherwise puthon will not recognize it.
~A tuple can be of diffrent data types
~tuple constructor tuple().
"""

first_tuple = ("Sudais","nomi","Obaid")
singleitem = ("sudais",)#tuple
singleitem1 = ("sudais")#not tuple

cons = tuple(("sudais",12,True,"okay"))

print(first_tuple)
print(len(first_tuple))
print(cons)