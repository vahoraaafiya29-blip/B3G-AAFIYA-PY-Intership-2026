student=[("Riya",88),("Aman",95),("Sara",72)]
sorted=sorted(student,key=lambda x:x[1],reverse=True)

print("Student sorted by marks:")
for name,mark in sorted:
     print(name,"-",mark)
