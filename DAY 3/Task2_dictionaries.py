students=[{"name":"Aafiya","marks":88},
          {"name":"Aman","marks":95},
          {"name":"Rahul","marks":91}]
                                        
top_student = students[0]

for student in students:
    if student["marks"] > top_student["marks"]:
         top_student = student


print("Highest Marks Student:",top_student)
    
            