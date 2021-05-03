name = {"sudais","haidar","alam"}

name.remove("haidar")#if the item to remove doesn't exist in .remove() then it will raise an error

print(name)

name.add("haidar")

"""

another method to remove is .discard(), if the item to remove doesn't exist in .discard() then it will not raise any error

"""

name.discard("lkasdioa")#won't give any error

print(name)
"""
we can also use the .pop() method to remove but pop is used to remove the last element and sets are unordered so we dont
actually know what the last element will be.

"""