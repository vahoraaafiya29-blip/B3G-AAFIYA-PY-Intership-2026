task=[]

task.append("Complete phython Assignment")
task.append("Study for Exam")
task.append("Wake up Early")
task.append("Practice Phython Coding")
task.append("Exercise for 30 Minutes")

print("Task After Adding:")
for item in task:
    print("-",item)

task.remove("Study for Exam")
task.remove("Wake up Early")

print("\nTask After Removing:")
for item in task:
    print("-",item)
task.remove
