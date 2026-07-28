student={"name":"sujal", 
        "age":"22","course":"mca"}
print(student)
print(student.get("course"))
print(student["name"])
student["college"]="ccmca"
student["age"]=21
student.pop("course")
print(student)
for k,v in student.items():
    print(k,":",v)
print(student.keys())
print(student.values())
student={
    1 : {"name":"sujal","course":"mc1a"},
    2 : {"name":"su2","course":"mc2a"},
    3 : {"name":"su3","course":"mcc3a"}
}
print(student)