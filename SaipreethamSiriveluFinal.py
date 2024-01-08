#!/usr/bin/env python
# coding: utf-8

# In[112]:


#define your own Vehicle class here
#the order of the four required positional arguments should be: make,model,year,mileage
#please use the conventional way to define function names and refer to the following test to adjust function names 
#no need to handle exceptions here

class Vehicle:
    def __init__(self, vmk, vmd, vy, vml):
        self.__make = vmk
        self.__model = vmd
        self.__year = vy
        self.__mileage = vml

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_mileage(self):
        return self.__mileage

    def set_make(self, vmk):
        self.__make = vmk

    def set_model(self, vmd):
        self.__model = vmd

    def set_year(self, vy):
        self.__year = vy

    def set_mileage(self, vml):
        self.__mileage = vml

    def __str__(self):
        return "Make: " + self.__make + "; Model: " + self.__model + "; Year of Manufacture: " + str(self.__year) + "; Mileage: " + str(self.__mileage)



# In[113]:


#do a quick test on the Vehicle class before moving forward (5 points)
#don't change this code
vehicle1=Vehicle("Honda","Civic",2014,50000)
print(vehicle1)
print("The mileage of this vehicle is:", vehicle1.get_mileage())
vehicle1.set_year(2012)
print("The year of manufacture of this vehicle is:", vehicle1.get_year())


# In[114]:


#define your own Employee class here
#the order of the three required positional arguments should be: name,address,vehicle object
#please use the conventional way to define function names and refer to the following test to adjust function names
#use emp for short of employee in naming attributes and functions
#no need to handle exceptions here

class Employee:

    def __init__(self, nm, addr, veh):
        self.__emp_name = nm
        self.__emp_addr = addr
        self.__vehicle = veh
    def get_emp_name(self):
        return self.__emp_name
    def get_emp_addr(self):
        return self.__emp_addr
    def get_vehicle(self):
        return self.__vehicle
    def set_emp_name(self, nm):
        self.__emp_name = nm
    def set_emp_addr(self, addr):
        self.__emp_addr = addr
    def set_vehicle(self, veh):
        self.__vehicle = veh
    def compute_compensation(self):
        pass
    def __str__(self):
        allData = "\nEmployee Name: " + self.__emp_name
        allData += "; Employee Address: " + str(self.__emp_addr)
        allData +=  "\n" + self.__vehicle.__str__()
        return allData


# In[115]:


#do a quick test on the Employee class before moving forward (5 points)
#don't change this code
emp1=Employee("Amy", "100 W Campbell Road, Richardson, Texas, 75080",vehicle1)
print(emp1)
print("{0} lives at {1}.".format(emp1.get_emp_name(),emp1.get_emp_addr()))
print("{0} owns a {1} {2} vehicle.".format(emp1.get_emp_name(),emp1.get_vehicle().get_make(),emp1.get_vehicle().get_model()))
emp1.set_emp_addr("800 E Campbell Road, Richardson, Texas, 75080")
print("{0} lives at {1}.".format(emp1.get_emp_name(),emp1.get_emp_addr()))


# In[116]:


#define your own Full Time Employee class here
#Full Time Employee class inherits from Employee class
#the order of the four required positional arguments should be: name,address,vehicle object,salary
#please use the conventional way to define function names and refer to the following test to adjust function names
#see detailed requirements on compute_compensation() function and compute_reimbursement() function in the pdf file
#no need to handle exceptions here

class FullTimeEmployee(Employee):


    def __init__(self, nm, addr, veh, sal):
        Employee.__init__(self,nm, addr, veh)
        self.__salary = sal
    def get_salary(self):
        return self.__salary
    def set_salary(self, sal):
        self.__salary = sal
    def compute_compensation(self):
        if self.__salary <= 25000:
            annual_compensation = self.__salary * (1 - 0.18)
        elif self.__salary <= 55000:
            annual_compensation = (self.__salary - 25000) * (1 - 0.28) + 20500
        else:
            annual_compensation = (self.__salary - 55000) * (1 - 0.33) + 42100
        return (annual_compensation/52)
    def compute_reimbursement(self,ae):
            if ae <= 10000:
                 self.__re = ae/52
            else:
                 self.__re = (10000+(0.5*(ae-10000)))/52
            return self.__re
    def __str__(self):
        childData = super().__str__()
        childData = "\nDetails of this Full Time Employee are:" + childData
        childData += "\nSalary: " + '{0:0.2f}'.format(self.__salary)
        return childData


# In[117]:


#do a quick test on the Full Time Employee class before moving forward (5 points)
#don't change this code
emp2=FullTimeEmployee("Amy", "100 W Campbell Road, Richardson, Texas, 75080", vehicle1, 40000)
print(emp2)
print("{0} has an annual salary of ${1}.".format(emp2.get_emp_name(),emp2.get_salary()))
print("{0} has a weekly compensation of ${1:0.2f}.".format(emp2.get_emp_name(),emp2.compute_compensation()))
print("{0} has a weekly reimbursement of ${1:0.2f}.".format(emp2.get_emp_name(),emp2.compute_reimbursement(12000)))
emp2.set_salary(50000)
print("{0} has an annual salary of ${1}.".format(emp2.get_emp_name(),emp2.get_salary()))


# In[118]:


#define your own Hourly Employee class here
#Hourly Employee class inherits from Employee class
#the order of the five required positional arguments should be: name,address,vehicle object,hours worked,hourly rate
#please use the conventional way to define function names and refer to the following test to adjust function names
#see detailed requirements on compute_compensation() function and compute_reimbursement() function in the pdf file
#no need to handle exceptions here

class HourlyEmployee(Employee):

    def __init__(self, nm, addr, veh, hw, hr):
        Employee.__init__(self,nm, addr, veh)
        self.__hours_wrkd = hw
        self.__hourly_rate = hr
    def get_hours_worked(self):
        return self.__hours_wrkd
    def get_hourly_rate(self):
        return self.__hourly_rate
    def set_hours_worked(self, hw):
        self.__hours_wrkd = hw
    def set_hourly_rate(self, hr):
        self.__hourly_rate = hr
    def compute_compensation(self):
        if self.__hours_wrkd > 40:
            return self.__hourly_rate * 40 + self.__hourly_rate * 1.8 * (self.__hours_wrkd - 40)
        else:
            return self.__hourly_rate * self.__hours_wrkd
    def compute_reimbursement(self,we):
            if we <= 100:
                 self.__we = we
            else:
                 self.__we = 100
            return self.__we
    def __str__(self):
        childData = super().__str__()
        childData = "\nDetails of this Hourly Employee are:" + childData
        childData += "\nHours Worked: " + str(self.__hours_wrkd)
        childData += "; Hourly Rate: " + str(self.__hourly_rate)
        return childData


# In[119]:


#do a quick test on the Hourly Employee class before moving forward (5 points)
#don't change this code
emp3=HourlyEmployee("Grace", "400 W Campbell Road, Richardson, Texas, 75080", vehicle1,50,20)
print(emp3)
print("{0} works {1} hours per week at an hourly rate of ${2}.".format(emp3.get_emp_name(),emp3.get_hours_worked(),emp3.get_hourly_rate()))
print("{0} has a weekly compensation of ${1:0.2f}.".format(emp3.get_emp_name(),emp3.compute_compensation()))
print("{0} has a weekly reimbursement of ${1:0.2f}.".format(emp3.get_emp_name(),emp3.compute_reimbursement(120)))
emp3.set_hourly_rate(22)
print("{0} works {1} hours per week at an hourly rate of ${2}.".format(emp3.get_emp_name(),emp3.get_hours_worked(),emp3.get_hourly_rate()))


# In[120]:


#define your own Consultant class here
#Consultant class inherits from Employee class
#the order of the five required positional arguments should be: name,address,vehicle object,hours worked,project type
#please use the conventional way to define function names and refer to the following test to adjust function names
#see detailed requirements on compute_compensation() function and compute_reimbursement() function in the pdf file
#no need to handle exceptions here

class Consultant(Employee):

    def __init__(self, nm, addr, veh, hw, pt):
        Employee.__init__(self, nm, addr, veh)
        self.__hours_wrkd = hw
        self.__project_type = pt
    def get_hours_worked(self):
        return self.__hours_wrkd
    def get_project_type(self):
        return self.__project_type
    def set_hours_worked(self, hw):
        self.__hours_wrkd = hw
    def set_project_type(self, pt):
        self.__project_type = pt
    def compute_compensation(self):
        if self.__project_type == 1:
            hrly_rate = 55
        elif self.__project_type == 2:
            hrly_rate = 70
        else:
            hrly_rate = 85
        return self.__hours_wrkd * hrly_rate
    def compute_reimbursement(self,we):
            if self.__project_type == 1:
                 self.__we = we
            elif self.__project_type == 2:
                 self.__we = 0.9*we
            elif self.__project_type == 3:
                 self.__we = 0.8*we   
            return self.__we
    def __str__(self):
        childData = super().__str__()
        childData = "\nDetails of this Consultant are:" + childData
        childData += "\nHours Worked: " + str(self.__hours_wrkd)
        childData += "; Project Type: " + str(self.__project_type)
        return childData


# In[121]:


#do a quick test on the Consultant class before moving forward (5 points)
#don't change this code
emp4=Consultant("Michael", "700 W Campbell Road, Richardson, Texas, 75080",vehicle1,40,2)
print(emp4)
print("{0} works {1} hours per week for type {2} project.".format(emp4.get_emp_name(),emp4.get_hours_worked(),emp4.get_project_type()))
print("{0} has a weekly compensation of ${1:0.2f}.".format(emp4.get_emp_name(),emp4.compute_compensation()))
print("{0} has a weekly reimbursement of ${1:0.2f}.".format(emp4.get_emp_name(),emp4.compute_reimbursement(300)))
emp4.set_hours_worked(35)
print("{0} works {1} hours per week for type {2} project.".format(emp4.get_emp_name(),emp4.get_hours_worked(),emp4.get_project_type()))


# In[122]:


#define your own Management class here
#Management class inherits from both Full Time Employee class and Consultant class
#the order of the six required positional arguments should be: name, address,vehicle object, salary, hours worked, project type
#please use the conventional way to define function names and refer to the following test to adjust function names
#see detailed requirements on compute_compensation() function and compute_reimbursement() function in the pdf file
#no need to handle exceptions here

class Management(FullTimeEmployee,Consultant):

    def __init__(self,nm,adr,veh,sal,hw,pt):
        Employee.__init__(self,nm,adr,veh)
        FullTimeEmployee.__init__(self,nm,adr,veh,sal)
        Consultant.__init__(self,nm,adr,veh,hw,pt)      
    def compute_compensation(self):
        self.__comp= (FullTimeEmployee.compute_compensation(self)+Consultant.compute_compensation(self))
        return self.__comp
    def compute_reimbursement(self, ae, we):
        self.__reim= (FullTimeEmployee.compute_reimbursement(self,ae)+Consultant.compute_reimbursement(self,we))
        return self.__reim
    def __str__(self):
        childData = "\nDetails of this Management are: \n" +"Employee Name: "+(self.get_emp_name())+"; Employee Address: "+(self.get_emp_addr())+"\n"+str(self.get_vehicle())+"\nSalary: {:.2f}".format(float((self.get_salary())))+ "; Hours Worked: "+str(self.get_hours_worked())+"; Project Type: "+str(self.get_project_type())
        return childData 


# In[123]:


#do a quick test on the Management class before moving forward (5 points)
#don't change this code
emp5=Management("Jane", "1000 W Campbell Road, Richardson, Texas, 75080",vehicle1,120000,10,3)
print(emp5)
print("\n")
print("{0} has an annual salary of ${1}.".format(emp5.get_emp_name(),emp5.get_salary()))
print("{0} works {1} hours per week for type {2} project.".format(emp5.get_emp_name(),emp5.get_hours_worked(),emp5.get_project_type()))
print("{0} has a weekly compensation of ${1:0.2f}.".format(emp5.get_emp_name(),emp5.compute_compensation()))
print("{0} has a weekly reimbursement of ${1:0.2f}.".format(emp5.get_emp_name(),emp5.compute_reimbursement(8000,300)))


# In[124]:


#complete this get_emp_input() function to prepare for the main menu application
#this function is used to ask for basic employee information and then return them: name and address
#this function doesn't take arguement(s)
#no need to handle exceptions here
def get_emp_input():
    name = input("Enter the employee's name: ")
    address = input("Enter the employee's address: ")
    return name, address


# In[125]:


#do a quick test on the get_emp_input() function before moving forward
#don't change this code and please use the sample input
#sample input: Bob; 350 E Campbell Road, Richardson, Texas, 75080
name, address=get_emp_input()
print("{0} lives at {1}.".format(name,address))


# In[159]:


#complete this get_vehicle_input() function to prepare for the main menu application
#this function is used to ask for vehicle information and then return them: make,model,year,mileage
#this function doesn't take arguement(s)
#no need to handle exceptions of make input and model input
#handle exceptions to make sure year is a 4-digit positive number between 1900 and 2023
#handle exceptions to make sure mileage is a positive number
def get_vehicle_input():
    veh_make = input('Enter the vehicle make: ')
    veh_model = input('Enter the vehicle model: ')

    while(True):
        try:
            veh_year = int(input('Enter the year of manufacture (yyyy): '))
            if veh_year < 1900 or veh_year > 2023: 
                raise ValueError
            break
        except ValueError:
                print('Please enter an integer value for year in the format of yyyy between 1900 and 2023.') 

    while(True):
        try:       
            veh_mileage = int(input('Enter the mileage: '))
            if veh_mileage < 0:
                raise ValueError
            break
        except ValueError:
                print('Please enter a positive number for mileage.') 

    return (veh_make, veh_model, veh_year, veh_mileage)


# In[160]:


#do a quick test on the get_vehicle_input() function before moving forward (5 points)
#don't change this code and please use the sample input
#sample input:Ford; Ranger; 2025 (when asked to enter again enter 2015); 80000
vehiclemake, vehiclemodel, vehicleyear, vehiclemileage = get_vehicle_input()  
print("The vehicle entered is a {0} {1} made in {2} with {3} mileage curently.".format(vehiclemake, vehiclemodel, vehicleyear, vehiclemileage))


# In[128]:


#complete this get_full_time_input() function to prepare for the main menu application
#this function is used to ask for specific information of full time employees and then return it: annual salary
#this function doesn't take arguement(s)
#no need to handle exceptions
def get_full_time_input():
    salary = float(input("Enter the annual salary: "))
    return salary


# In[129]:


#do a quick test on the get_full_time_input() function before moving forward
#don't change this code and please use the sample input
#sample input:80000
salary=get_full_time_input()
print("The annual salary entered is {0:0.2f}".format(salary))


# In[130]:


#complete this get_hourly_input() function to prepare for the main menu application
#this function is used to ask for specific information of hourly employees and then return them: hours worked, hourly rate
#this function doesn't take arguement(s)
#no need to handle exceptions
def get_hourly_input():
    hours_worked = int(input("Enter the hours worked: "))
    hourly_rate = float(input("Enter the hourly rate: "))
    return hours_worked,hourly_rate


# In[131]:


#do a quick test on the get_hourly_input() function before moving forward
#don't change this code and please use the sample input
#sample input: 30; 20
hours_worked, hourly_rate = get_hourly_input()
print("This hourly employee works {0} hours per week at an hourly rate of ${1:0.2f}".format(hours_worked,hourly_rate))


# In[132]:


#complete this get_consultant_input() function to prepare for the main menu application
#this function is used to ask for specific information of consultants and then return them: hours worked, project type
#this function doesn't take arguement(s)
#no need to handle exceptions
def get_consultant_input():
    hours_worked = int(input("Enter the hours worked: "))
    project_type = int(input("Project Type? (Enter a number between 1 and 3): "))
    return hours_worked, project_type


# In[133]:


#do a quick test on the get_consultant_input() function before moving forward
#don't change this code and please use the sample input
#sample input: 40; 2
hours_worked, project_type = get_consultant_input()
print("This consultant works {0} hours per week for type {1} project.".format(hours_worked,project_type))


# In[134]:


#complete this get_management_input() function to prepare for the main menu application
#this function is used to ask for specific information of managements and then return them: annual salary, hours worked, project type
#this function doesn't take arguement(s)
#no need to handle exceptions
def get_management_input():
    salary = float(input("Enter the annual salary: "))
    hours_worked = int(input("Enter the hours worked: "))
    project_type = int(input("Project Type? (Enter a number between 1 and 3): "))
    return salary, hours_worked, project_type


# In[135]:


#do a quick test on the get_management_input() function before moving forward
#don't change this code and please use the sample input
#sample input: 100000; 8; 3
salary, hours_worked, project_type = get_management_input()
print("This management has an annual salary of ${0:0.2f}. This management also works {1} hours per week additionally for type {2} project.".format(salary, hours_worked,project_type))


# In[136]:


#complete this read_file_data() function to prepare for the main menu application
#this function is used to read information from an existing databse/binary file, which is empdata.dat in the final exam
#this function doesn't take argument(s)
#this function returns a list containing all employee objects stored in the database; each employ object is an element in the list; the list will also be used and updated later
#need to handle exceptions if file doesn't exist
import pickle
import sys
def read_file_data():
    with open('empdata.dat', 'rb') as f:
        emp_list =[]
        while(1):
            try:
                emp_list.append(pickle.load(f))
            except EOFError:
                break
            except:
                pass
    return emp_list


# In[137]:


#do a quick test on the read_file_data() function before moving forward (5 points)
#don't change this code
emp_list=read_file_data()
print("There are {} employees stored in the database.".format(len(emp_list)))
print("\nBelow is the information of the first employee in the database: {}".format(emp_list[0]))
print("\n{} is the first employee.".format(emp_list[0].get_emp_name()))


# In[138]:


#complete option 1 related code here
#the idea is to walk through users to input required information
#the first and foremost step is to ask for emloyee type
#this function doesn't take arguement(s)
#this function prints the entered object and also returns the entered object
#some parts are provided so you don't need to change them (but you still can if you want to)

def run_option1():
    #ask for employee type
    #exceptions need to be handled here to accept valid input 

    while(1):
        try:
            emp_type = int(input("Enter the employee type(1-Full Time;2-Hourly;3-Consultant;4-Management)"))
            if emp_type<1 or emp_type>4:
                raise ValueError
            else:
                break
        except ValueError:
            print("Please select an option from 1, 2, 3, and 4")
 
    #call the previous get_emp_input() to ask for employee information and store the values      
    name, address = get_emp_input()
    
    #call the previous get_vehicle_input() to ask for vehicle information and store the values
    vehiclemake, vehiclemodel, vehicleyear, vehiclemileage = get_vehicle_input()    
    
    #create an object of Vehicle class using the prervious information
    a_vehicle = Vehicle(vehiclemake, vehiclemodel, vehicleyear, vehiclemileage)
    
    #depending on previous input, call the prervious functions to ask for corresponding information
    #then use all the required information to create an object of a certain class 
    #type 1:annual salary
    #type 2:hours worked,hourly rate
    #type 3:hours worked, project type
    #type 4:annual salary, hours worked, project type
    if emp_type == 1:
        sal = get_full_time_input()
        an_emp = FullTimeEmployee(name, address, a_vehicle,sal)
    elif emp_type == 2:
        hw, hr = get_hourly_input()
        an_emp = HourlyEmployee(name, address, a_vehicle, hw, hr)
    elif emp_type == 3:
        hw, pt = get_consultant_input()
        an_emp = Consultant(name, address, a_vehicle, hw, pt)
    elif emp_type ==4:
        sal, hw, pt = get_management_input()
        an_emp = Management(name, address, a_vehicle, sal, hw, pt)
    
    print(an_emp)
    
    print("\n============================================================")        
    print("New employee entered successfully! Now going to the main menu.")
    print("==============================================================")       
    return an_emp    


# In[139]:


#do a quick test on the run_option1() function before moving forward (5 points)
#don't change this code and please use the example input
#example input: 5 (then zzz then 4); David; 103 E Campbell Road, Richardson, Texas, 75080; BMW; X3;2018;5000;110000;5;2
run_option1()


# In[140]:


#complete option 2 related code here
#the function is to print centain number of employees as required by users
#first choice:print all employees; second choice: print first 5 employees when there are at least 5 employees (print all if fewer than 5)
#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)
#this function doesn't return anything
#needs to handle exceptions when taking user seletions
def run_option2(my_lst):
    while(1):
        try:
            emp_count = int(input("Do you want to see information of all employees (input 1) or the first 5 employees (input 2)? "))
            if emp_count == 1 or emp_count==2:
                break
            else:
                raise ValueError
        except ValueError:
            print("Please select 1 or 2")
    if emp_count == 1:
        print("\n============================================================")        
        print("Below is the information of all the employees stored in the database.")
        print("==============================================================")
        for i in range(0,len(my_lst)):
            print(my_lst[i])
    else:
        if len(my_lst) >= 5:
            print("==========================================================================")
            print("Below is the information of the first 5 employees stored in the database.")
            print("==========================================================================")
            for i in range(0,5):
                print(my_lst[i])
        else:
            print("\n============================================================")        
            print("Below is the information of all the employees stored in the database.")
            print("==============================================================")
            for i in range(0,len(my_lst)):
                print(my_lst[i])


# In[141]:


#do a quick test on run_option2() function before moving forward (5 points)
#don't change this code and please use the sample input
#sample input: 3 (then zzz then 2)
run_option2(emp_list)


# In[142]:


#complete option 3 related code here
#the function is used to print compensations of all Employees
#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)
#this function doesn't return anything
#no need to handle exceptions
def run_option3(my_lst):
    print("\nEmployee name and Compensation of all Employees")
    print("=================================================")
    for i in range(0,len(my_lst)):
        print("{0}'s weekly compensation is ${1:0.2f}".format(my_lst[i].get_emp_name(),my_lst[i].compute_compensation()))


# In[143]:


#do a quick test on run_option3() function before moving forward (5 points)
#don't change this code and please use the sample input
run_option3(emp_list)


# In[144]:


#complete option 4 related code here
#the function is used to search for an employee by name and the searching is NOT case sensitive
#if there are some matching cases, print the information of all matched employees
#if no matchng cases, print "There is no employee matching the name you entered."
#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)
#this function also returns a list of objects of the matched employees
#no need to handle exceptions
def run_option4(my_lst):
    ename_list = []
    e_name = input("\nPlease enter the name of the emplyee you want to search:")
    e_name=e_name.upper()
    for i in range(0,len(my_lst)):
        if my_lst[i].get_emp_name().upper() == e_name:
            ename_list.append(my_lst[i])
            
    if len(ename_list) == 0:
        print('There is no employee matching the name you entered.')
        return ename_list
    
    print('==========================================================================')
    print('Below is the information of all employees that match the name you entered.')
    print('==========================================================================')
    
    for i in range(0, len(ename_list)):
        print(ename_list[i])
    return ename_list


# In[145]:


#do a quick test on run_option4() function before moving forward (5 points)
#don't change this code and please use the example input (all upper cases)
#example input: TOM
#part 1
matched_emp_list=run_option4(emp_list)
print("\nThere are {} employees matching your search.".format(len(matched_emp_list)))


# In[146]:


#do a quick test on run_option4() function before moving forward 
#don't change this code and please use the example input
#example input: Hongchang
#part 2
run_option4(emp_list)


# In[147]:


#complete option 5 related code here
#the function is used to show some basic statistics. They are: 
#(1) the number of employees stored in the database
#(2) the highest weekly compensation
#(3) the mean weekly compensation
#(4) the number of employees who have a vehicle with over 100,000 mileage
#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)
#this function doesn't return anything
#no need to handle exceptions

def run_option5(my_lst):
    emp_count = len(my_lst)
    mean_comp = 0
    max_comp = 0
    count = 0
    for i in range(0,len(my_lst)):
        if my_lst[i].compute_compensation() > max_comp:
            max_comp = my_lst[i].compute_compensation()
        mean_comp += my_lst[i].compute_compensation()
        if my_lst[i].get_vehicle().get_mileage() > 100000:
            count += 1
    print('\n========================================================')
    print('Below is the statistics of all employees in this database.')
    print('========================================================')
    print("There are {0} emplyees stored in this employee database.".format(emp_count))
    print("The highist weekly compensation is ${0:0.2f}.".format(max_comp))
    print("The mean weekly compensation is: ${0:0.2f}.".format(mean_comp/emp_count))
    print("The number of employees who have a vehicle with over 100,000 mileage is {0}.".format(count))


# In[148]:


#do a quick test on run_option5() function before moving forward (5 points)
#don't change this code 
run_option5(emp_list)


# In[161]:


#complete option 6 related code here
#the function is used to compute weekly reimbursement (assuming the user has the requirerd information)
#the first step is to ask for the name of the employee (you can call run_option4() here)
#the second step is to select one employee from the matched employees
#the third step is to ask for required information 
#this function doesn't return anything
#no need to handle exceptions
def run_option6(emp_list):
    matched_list=run_option4(emp_list)
    choice=int(input("Which employee do you want to check (enter a number)?"))
    emp=matched_list[choice-1]
    
    weekly_expense = int(input("What is the annual expense?"))
    print("\n############################################################")
    print("This employee should have a weekly reimbursement of ${:.2f}.".format(
        round(matched_list[choice - 1].compute_reimbursement(weekly_expense), 2)))


# In[162]:


#do a quick test on run_option6() function before moving forward (5 points)
#don't change this code and please use the example input (all lower cases)
#example input: bob;1;8000
#part 1

run_option6(emp_list)


# In[151]:


#do a quick test on run_option6() function before moving forward 
#don't change this code and please use the sample input (all lower cases)
#sample input: james;1;130
#part 2

run_option6(emp_list)


# In[152]:


#complete option 7 related code here
#the function is used to store changes into a new file/database (i.e. empdata_updated.dat) and exit the program
#the first step is to double check with the user if he/she does want to exit (not case sensitive)
#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)
#this function doesn't return anything
#no need to handle exceptions

import sys
def run_option7(my_lst):
    f = open('empdata.updated.dat', 'w')
    f.close()
    exit = input('You chose to exit the program \nAre you sure(Y/N)?')
    if exit.lower() == 'n':
        print("\n\n=================================")
        print("Going back to the selection menu.")
        print("=================================")
    elif exit.lower() == 'y':
        print("=================================")
        print("Program successfully being closed")
        print("=================================")
        sys.exit()
    elif exit.lower() != 'n' or exit.lower() != 'y':
        print(
            "\n\nYour input doesn't match any valid option and has been considered as 'N'.\nGoing back to the selection menu.")


# In[153]:


#do a quick test on run_option7() function before moving forward (5 points)
#don't change this code and please use the example input
#example input: b
#part 1
run_option7(emp_list)


# In[154]:


#do a quick test on run_option7() function before moving forward 
#don't change this code and please use the example input
#example input: n
#part 2
run_option7(emp_list)


# In[155]:


#do a quick test on run_option7() function before moving forward 
#don't change this code and please use the example input
#example input: y
#part 3
run_option7(emp_list)


# In[156]:


#complete the main application
#the application menu provides 7 options
#when user selects a valid option (except for 7), execute that option and come back to the menu again
#need to handle exceptions when taking user's choices
#this function doesn't take any arguments
#it will work on the employ object list which is read from file empdata.dat

def run_menu_options():
    #read employee objects in to a list
    emp_list = read_file_data()
    
    # display 7 options and ask users to select from them and execute the selection
    sel = 1
    while sel <=  7 and sel >= 1:
        #display options
        while True:
            print("\n==== Menu ====")
            print("1. To add an employee")
            print("2. To print the name and address of employees")
            print("3. To print the employee name and compensation of all employees")
            print("4. To search for employees by name")
            print("5. To check the basic statistics of employees")
            print("6. To calculate the reimbursement of one employee")
            print("7. To exit program")
        
            #take selection 
        
            try:
                sel=int(input('Your selection is: '))
                if(sel<1 or sel>7):
                    raise ValueError
                break
            except ValueError:
                print("\n=========================================")
                print('You must enter an integer between 1 and 7!')
                print("=========================================")
        
        #execute selection
        if sel == 1:
            emp_list.append(run_option1())
        elif sel == 2:
            run_option2(emp_list)
        elif sel == 3:
            run_option3(emp_list)
        elif sel == 4:
            run_option4(emp_list)
        elif sel == 5:
            run_option5(emp_list)
        elif sel == 6:
            run_option6(emp_list)
        elif sel == 7:  
            run_option7(emp_list)
        else:
            print("Invalid choice!")


# In[157]:


#do a quick test run_menu_options() function before moving forward (5 points)
#don't change this code and please use the example input
#example inputs in this order: 0;8;zzz;7;n;7;y
run_menu_options()


# In[158]:


#here comes the main test, which is splitted into several steps (20 points in total)

#step 1: choose option 1 three times and enter the following three employees (5 points)
#type 4 employee: David; 103 E Campbell Road, Richardson, Texas, 75080; BMW; X3; 2018;5000;110000;5;2
#type 4 employee: Grace; 105 E Campbell Road, Richardson, Texas, 75080; Porsche; Cayenne; 2019;3000;180000;8;1
#type 4 employee: Zoey; 107 E Campbell Road, Richardson, Texas, 75080; Audi; A3; 2022;3000;90000;10;3

#step 2: choose option 2
#then choose 1

#step 3:choose option 3 (5 points)

#step 4:choose option 4 
#then type in: grace (all lower cases)

#step 5:choose option 5 (5 points)

#step 6:choose option 6 (5 points)
#then type in: ZOEY (all upper cases); then 1; then 120

#step 7:choose option 7
#then type in: y
run_menu_options()


# In[ ]:




