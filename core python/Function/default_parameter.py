#1. To mack the parameter optinal
#2. parameter - default (assigning value to parameter in function definition)
#3. If we pass value to default para,it takes passed value
#   If we don't pass value to default para,it takes default value
#4. Flow from right to left


def emp(id, name, sal, dept = 'Backoffice'):
    print('Id:',id)
    print('Name:',name)
    print('Sal:',sal)
    print('Department:',dept)

emp(101,'ABC',50000,'IT')
print('#################')
emp (102,'xyz',10000)