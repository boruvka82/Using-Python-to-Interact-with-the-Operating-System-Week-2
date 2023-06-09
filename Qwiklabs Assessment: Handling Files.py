

  GNU nano 2.7.4                     File: generate_report.py                               

#!/usr/bin/env python3
import csv
def read_employees(csv_file_location):
     csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
     employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
     employee_list = []
     for data in employee_file:
        employee_list.append(data)
     return employee_list

employee_list = read_employees('/home/student-04-d1cf564b5e20/data/employees.csv')
print(employee_list)

def process_data(employee_list):
     department_list = []
     for employee_data in employee_list:
        department_list.append(employee_data['Department'])

     department_data = {}
