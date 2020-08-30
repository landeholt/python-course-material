class Human:
    def __init__(self, name, age):
        self.name = name,
        self.age = age
        self.operator = self.age
        
    def __lt__(self, other):
        return self.operator < other.operator