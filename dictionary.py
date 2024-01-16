employee = {'name':'ramu',
            'age':25,
            'mobile':8978315418,
            'city':'vijayawada'
            }

employee.update({'colour':'red'})
employee.update({'name':'manu'})
employee.pop('city')

print(employee['name'])
#print(employee['koni'])
print(employee.get('am'))
print(employee.values())
print(employee.keys())
print(employee.items())

for key,value in employee.items():
    print(key,value)

j = employee.clear()
print(employee)