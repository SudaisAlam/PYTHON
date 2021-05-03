name = {"sudais","nomi","obaid"}

names = {"sudais","nomi","obaid","hamza","junaid"}

name.intersection_update(names)

print(name)
#we use the .intersection_update() to keep it in the same set

#we use the .intersection() to return a new set

new = names.intersection(name)

print(new)