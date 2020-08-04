
from dataclasses import dataclass, field

def get_default_salary():
    sal = [2323, 4354, 3445, 6543]
    return sum(sal) / len(sal)

@dataclass(unsafe_hash=True)
class DataClassFields:
    name: str
    age: int = 18
    city: str = field(default='Berlin')
    salary: float = field(default_factory=get_default_salary) # you can not call a mehtod which takes arguments
    risk_factor: float = field(init=False, default=3.4) # i don't want this field part of the initialization
    addr: str = field(default='123, Berlin', repr=False, hash=False, compare=False) # i don't want to see this field in the class representation and also don'' consider this field while calculating the hash of the object
    # compare=False - i don'' wnt to include this filed while comparing the objects
    year_of_birth : int = field(default=1990, metadata={'format' : 'year'})



d1 = DataClassFields('Ashok')
print(d1.__dataclass_fields__)
print(d1)
print(hash(d1))
print(d1.__dataclass_fields__['year_of_birth'].metadata['format'])
