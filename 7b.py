class Employee:
    def __init(self):
        self.name = ""
        self.empId = ""
        self.dept = ""
        self.salary = 0
    def getEmpDetails(self):
        self.name = input("enter a Employee Name:")
        self.empId = input("enter employee id:")
        self.dept = input("enter the department:")
        self.salary = int(input("enter the salary:"))
    def showEmpDetails(self):
        print("Employee Details:")
        print("Name:",self.name)
        print("empId:",self.empId)
        print("dept:",self.dept)
        print("salary:",self.salary)
    def updtSalary(self):
        self.salary = int(input("enter new salary:"))
        print("Updated salary:",self.salary)
e1 = Employee()
e1.getEmpDetails()
e1.showEmpDetails()
e1.updtSalary()
