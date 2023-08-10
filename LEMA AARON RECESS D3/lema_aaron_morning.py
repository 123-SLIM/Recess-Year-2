# Exercise 1
class Employee:
    def __init__(self, name, salary, bonus = 0.15) :
        self.name = name
        self.salary = salary
        self.bonus = bonus
        
        def bonus(self):
          bonus = self.salary + bonus* salary
        print(f"Hello {self.name}, your bonus is:", {bonus})
          
        employee1 = Employee("Aaron", 12000000)
        employee1.bonus()
        
# Exercise 2
class Temoerature:
    def __init__(self, celcius):
        self._celcius = celcius
        
        def ferenheight(self):
            return (self._celcius * 9/5) + 32
        
        temperature = Temoerature(37)
        print(f"{temperature.ferenheight()} Ferenheight")
        
# Exercise 3...Show encapsulatio with employee information to give a pay incrememt(salary with employee information to new-salary) Eg from 850000 to 1000000
class Employee:
    def __init__(self, name, salary):
       self._name = name
       self._salary = salary
       
       def get_name(self):
           return self._name
       
       def get_salary(self):
           return self._salary
       
       def set_salary(self, new_salary):
           if new_salary > self._salary:
               self._salary = new_salary
           else:
               print("New salary should be higher than the current salary.")
               
               employee = Employee("John Aaron", 850000)
               
               print("Current salary:", employee.get-salary())
               
               employee.set_salary(1000000)
               print("Updated salary:", employee.get_salary())
           