word=["Apple","Ant","Banana","Cat","Carrot"]
group={}
for A in word:
    letter=A[0]
    group.setdefault(letter,[]).append(A)

print(group)