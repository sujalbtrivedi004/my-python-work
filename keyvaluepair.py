student={"name":"sujal", 
        "age":"22","course":"mca"}
for k,v in student.items():
    print(k,":",v)
print(student.values())
print(student.keys())

student={
    1 : {"name":"sujal","course":"mc1a"},
    2 : {"name":"su2","course":"mc2a"},
    3 : {"name":"su3","course":"mcc3a"}
}
print(student)
print(student[2]["name"])
print(student[2])
print(student[3])