def get_employee_details(name, emp_id, department, salary):
   return(
      f"Employee Name: {name}\n"
      f"Employee ID: {emp_id}\n"
      f"Department: {department}\n"
      f"Salary: ${salary:.2f}" 
  )

#Example usage (optional)
if __name__=="__main__":
    print(get_employee_details("John Doe","E101","IT",55000))