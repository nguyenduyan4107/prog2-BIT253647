class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, s):
        name, age = s.split("-")
        return cls(name, int(age))


p = Person.from_string("An-19")
print(p.name, p.age)
