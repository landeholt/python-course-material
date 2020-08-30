class Student:
    def __init__(self, payload):
        self.name = f'{payload[1]} {payload[0]}'.strip().replace('"','')
        self.ssn = payload[2].strip().replace('"','')
        self.final = payload[6].strip().replace('"','')
        self.grade = payload[7].strip().replace('"','')
    
    def __repr__(self):
        return f'<Student name: {self.name} grade: {self.grade}>'