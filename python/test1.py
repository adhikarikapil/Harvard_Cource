class Employee:
    def __init__(self, fname, lname, salary) -> None:
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = fname + '.' + lname + "@company.com"
    
    
    def fullname(self) :
        return '{} {}'.format(self.fname, self.lname)
        
    def raise_pay(self) :
        self.salary = (self.salary * 1.04) 
        
        
emp1 = Employee('Kapil', 'Adhikari', 50000)
emp2 = Employee('Samip', 'Regmi', 60000)

print(emp1.salary)
emp1.raise_pay()
print(emp1.salary)