def calculate_average(students):
     averages={name: round(sum(marks)/len(marks),2) for name,marks in students.items()}
     print("Average marks: ",averages)
     top_student=max(averages,key=averages.get)
     print(f"Top Performer: '{top_student}'")
students={}
while True:
    name=input("Enter the student name(type exit to quit)   : ")
    if name=="exit":
        break
    value=input("Enter the student marks separated by a marks : ")
    marks_list=[int(value.strip()) for value in value.split(",")]
    students[name]=marks_list
print(f"Students = {students}")
calculate_average(students)