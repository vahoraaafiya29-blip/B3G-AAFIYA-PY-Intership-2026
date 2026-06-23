Matrix=[[10,20,30],[40,50,60],[70,80,90]]
transpose=[[row[i]for row in Matrix] for i in range(len(Matrix[0]))]

print("original Matrix:")
for row in Matrix:
    print(row)
print("\nTransposed Matrix:")
for row in transpose:
    print(row)    