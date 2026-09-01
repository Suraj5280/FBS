emp_details = {}

def addEmp():
    id = int(input('Enter ID:'))
    nm = input('Enter NAME:')
    dept = input('Enter DEPARTMENT:')
    sal = float(input('Enter SALARY:'))
    passwd = input('Enter PASSWORD:')
    if(id not in emp_details):
        emp_details[id] = [id, nm, dept, sal, passwd]
        print('Employee added successfully.')
    else:
        print('Employee ID already available.')

def updEmp():
    id = int(input('Enter ID:'))
    er = emp_details.get(id)
    if(er):
        nm = input(f'Enter new NAME({er[1]}):')
        dept = input(f'Enter new DEPARTMENT({er[2]}):')
        sal = float(input(f'Enter new SALARY({er[3]}):'))
        passwd = input(f'Enter new PASSWORD({er[4]}):')
        emp_details[id] = [id, nm, dept, sal, passwd]
        print('Employee updated successfully.')
    else:
        print('ID not found.')

def delEmp():
    id = int(input('Enter ID:'))
    if(id in emp_details):
        del emp_details[id]
        print('Employee deleted successfully.')
    else:
        print('ID not found.')

def searchEmp():
    id = int(input('Enter ID:'))
    if(id in emp_details):
        emp = emp_details[id]
        print('\n')
        print('+-------+------------------+------------------+------------------+------------------+')
        print('|  ID   |       NAME       |    DEPARTMENT    |      SALARY      |      PASSWORD    |')
        print('+-------+------------------+------------------+------------------+------------------+')
        print(f'| {emp[0]:5d} | {emp[1]:16s} | {emp[2]:16s} | {emp[3]:16.2f} | {emp[4]:16s} |')
        print('+-------+------------------+------------------+------------------+------------------+')
        print()
    else:
        print('ID not found.')

def showAllEmp():
    if(emp_details):
        print('\n')
        print('+-------+------------------+------------------+------------------+------------------+')
        print('|  ID   |       NAME       |    DEPARTMENT    |      SALARY      |      PASSWORD    |')
        print('+-------+------------------+------------------+------------------+------------------+')
        for id, emp in emp_details.items():
            print(f'| {emp[0]:5d} | {emp[1]:16s} | {emp[2]:16s} | {emp[3]:16.2f} | {emp[4]:16s} |')
        print('+-------+------------------+------------------+------------------+------------------+')
        print()
    else:
        print('No employees found.')

def login():
    print('####LOGIN PAGE####')
    uid = 'admin'
    passw = '1234'
    username = input('Enter USERNAME:')
    password = input('Enter PASSWORD:')
    if(uid == username and passw == password):
        empManage()
    else:
        print('Invalid credentials...')

def empManage():
    while True:
        print('\n================== EMPLOYEE MANAGEMENT ==================')
        print('1. Add New Employee')
        print('2. Update Employee')
        print('3. Delete Employee')
        print('4. Search Employee')
        print('5. Show All Employees')
        print('6. Logout')
        print('=========================================================')
        ch = input('Enter choice: ')
        if(ch == '1'):
            addEmp()
        elif(ch == '2'):
            updEmp()
        elif(ch == '3'):
            delEmp()
        elif(ch == '4'):
            searchEmp()
        elif(ch == '5'):
            showAllEmp()
        elif(ch == '6'):
            print('Logged out...')
            break
        else:
            print('Invalid choice...')

ch = ''
while(ch != '2'):
    print('''Please select option from below:
    1. Login
    2. Exit''')
    ch = input("Enter choice: ")
    if(ch == '1'):
        login()
    elif(ch == '2'):
        print('Thank you for choosing us!')
    else:
        print('Invalid choice...')
