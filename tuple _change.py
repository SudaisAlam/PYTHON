"""
    first change the tuple into list and the make changes
"""
barca = ("messi","pedri","griezmann","piqué")

update = list(barca)

update.append("ter stegen")

barca = tuple(update)

print(barca)