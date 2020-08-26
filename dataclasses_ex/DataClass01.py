

class DataClass01ProbSt:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # def __repr__(self):
    #     return "name: {}, age: {}, salary: {}".format(self.name, self.age, self.salary)

d11 = DataClass01ProbSt('Samrat', 30, 3243)
d12 = DataClass01ProbSt('Samrat', 30, 3243)

print(d11) # <__main__.DataClass01ProbSt object at 0x1021e6e10>
print(d11.__dict__)
print(d11.__dict__['name'])

print(d11 == d12) # False

print(d11.name)
d11.name = 'Ash'
print(d11.name)

from dataclasses import dataclass

@dataclass(order=True, frozen=True)
class DataClass01Sol:
    name: str
    age: int
    salary: float

d21 = DataClass01Sol('Samrat', 30, 3214)
d22 = DataClass01Sol('Samrat', 30, 3214)
d23 = DataClass01Sol('Samrat', 31, 3214)

print(d21)
print(d21 == d22)
print(d21 > d23, d22 < d23)

# d21.name = 'Arun' # compile time error, the attribut name is read-only