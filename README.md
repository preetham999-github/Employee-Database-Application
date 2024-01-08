# Employee-Database-Application
Classes
Employee (Base Class)

Attributes:
Employee's name (string)
Employee's address (string)
Vehicle data (Vehicle object)
FullTimeEmployee (Child Class of Employee)

Additional Properties:
Salary (float)
Methods:
compute_compensation()
compute_reimbursement()
HourlyEmployee (Child Class of Employee)

Additional Properties:
Hours Worked (int)
Hourly Rate (float)
Methods:
compute_compensation()
compute_reimbursement()
Consultant (Child Class of Employee)

Additional Properties:
Hours Worked (int)
Project Type (valid values: 1, 2, and 3)
Methods:
compute_compensation()
compute_reimbursement()
Management (Child Class of FullTimeEmployee and Consultant)

Inherited Attributes:
Name, address, and vehicle object from Employee
Salary from FullTimeEmployee
Hours worked and project type from Consultant
Methods:
compute_compensation()
compute_reimbursement()
Vehicle (Class for Vehicle Information)

Attributes:
Make (string)
Model (string)
Year of Manufacture (int)
Mileage (int)
Constructor Method (init)
Program Execution
The program allows users to perform various operations on the employee database through a menu-driven interface. The main functionalities include:

Add a New Employee (Option 1):

Accepts input for new employees based on employee type.
Temporary objects are stored in an "object container" and written to a new database upon program exit.
Display Employees' Information (Option 2):

Displays employee information based on user input.
Compute and Print Compensation (Option 3):

Lists the names of all employees along with their respective compensations.
Search Employees by Name (Option 4):

Searches for employees by name and displays matching results.
Check Basic Statistics of Employees (Option 5):

Displays basic statistics of the employee database.
Calculate Reimbursement of One Employee (Option 6):

Allows users to select an employee and calculates weekly reimbursement based on employee type.
Exit the Application (Option 7):

Writes all information to a new database/file.
Asks for user confirmation before closing the program.
