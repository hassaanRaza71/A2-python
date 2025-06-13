class Employee:
    def __init__(self,hourlypay,employeenumber,jobtitle):
        self.__HourlyPlay=hourlypay
        self.__EmployeeNumber=employeenumber
        self.__Jobtitle=jobtitle
        self.__PayYear2022=[0.0 for _ in range(52)]

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self,week_number,numberofhours_worked):
        self.__PayYear2022[week_number]=numberofhours_worked*self.__HourlyPlay


    def GetTotalPay(self):
        Total=0
        for pay in self.__PayYear2022:
            Total+=pay
        return Total


class Manager(Employee):
    def __init__(self,hourlypay,employeenumber,bonusvalue,jobtitle):
        super().__init__(hourlypay,employeenumber,jobtitle)
        self.__BonusValue=bonusvalue

    def SetPay(self,week_number,numberofhours_worked):
        hoursworked= numberofhours_worked*(1+self.__BonusValue)
        super().SetPay(week_number, hoursworked)

with open("Employees.txt") as data:
    count=0

    job_titles=["Junior Developer","Web Developer","Assistant Tester","Team Leader","Intern","Junior Testing Manager", "System analyst"]
    employees_data=[]
    for line in data:
        employees_data.append(line.strip())
EmployeeArray=[Employee(employees_data[0],employees_data[1],employees_data[3])
    ,Employee(employees_data[4],employees_data[5],employees_data[6])
    ,Employee(employees_data[7],employees_data[8],employees_data[9],employees_data[10])
    ,Employee(employees_data[11],employees_data[12],employees_data[13],em)



