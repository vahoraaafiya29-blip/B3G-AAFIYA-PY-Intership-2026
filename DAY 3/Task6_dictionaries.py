employees={
"Aafiya":50000,
"Aksha":70000,
"suzan":60000,
"faizan":80000,
"farhan":75000
}
sorted_employees = dict(
  sorted(employees.items(),key=lambda
 x: x[1],reverse=True))           

print("Employees sorted by salary:")
for name, salary in sorted_employees.items():
    print(name, ":", salary)

print("\nTop 3 highest paid employees:")
count=0

for name,salary in sorted_employees.items():
    if count<3:
     print(name,":",salary)
    count +=1

