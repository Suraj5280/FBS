#1. To pass multiple values with meaning to function
#2. Mention 2 astrisk symbols before parameter name in 
#funciton defination
#3. passed data stored in directory format
#4. use for loop on dict.stems() to get values and keys

def emp(**data):
    for key, val in data.items():
        print(key,':',val)
    

emp(id = 101,age=35,add='pune',sal=50000,dept='Admin')