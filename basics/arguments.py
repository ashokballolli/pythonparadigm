

def student(name, age=20): # default parameters should be at the end
    print(name, age)
    
student('ashok', 30)

def student(name, pyhsicsMarks, mathMarks, chemMarks, age=20):
    print(name, age, pyhsicsMarks, mathMarks, chemMarks)

student('ashok', 60, 50, 70, 20)

def student(name='no name', age=20, *marks):
    print(name)
    print(age)
    print(marks)
    for m in marks:
        print(m)

student('shilpa', 20, 90, 80, 70)


def student(name='no name', age=20, **marks): # dictionary
    print(name)
    print(age)
    print(marks)
    for key, value in marks.items():
        print(key, ' = ', value)


student('shilpa', 23, phy=90, chem=80, math=70)
student(name='Newton', phy=90, chem=80, math=70)
