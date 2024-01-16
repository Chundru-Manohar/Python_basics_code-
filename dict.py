phone_no ={'ram':1234,
           'ravi':25678,
           'teja': 56789,
           }
print(phone_no['ram'])
print(phone_no['teja'])
phone_no['teja'] = 199822
phone_no['manu'] = 262626
phone_no['mom']={1111,2222,3333}
phone_no['mom'] = {'mom_num':8888,'mom_work':7086}
print(phone_no['mom']['mom_work'])
print(phone_no)
print(phone_no.get('ram'))
print(phone_no.pop('teja'))
del phone_no['mom']
print(phone_no.popitem())
print(phone_no)

'''phone_No = dict({'iron':2562,'gowth':561231,})
print(phone_No)
print(phone_No['gowth'])'''

data = {
    1:'manu',
    2:'trun',
    3:'lion',
    4:'pop',
    5:'tinku',
}
print(data[1])

del data[4]
print(data)

print(data.popitem())
print(data)
#print(data.clear())
print(phone_no.keys())
print(phone_no.values())
print(data.get(2))
print(data.pop(2))
print(data.popitem())
data[6]='home'
data[8]='koko'
data[9]='univ'
del data[6]
print(data)
print(data.items())
for i in data.items():
    print(i)
    #print(data[i])
print(data)
maohar = data.copy()
print(maohar)
print(len(maohar))

#nested Dicitonary

student = {
    "ram":{'roll':25,'age':20,'colour':'white'},
    "Tarun":{'roll':20,'age':21,'colour':'white'},
    "ravi":{'roll':28,'age':22,'colour':'white'},
}
print(student)
print(student['Tarun']['age'])
student['ravi']['number']=8978315418
print(student['ravi'])

Travel_details = {
    "Kolkata":['westbengal','howra'],
    "vijayawada":['Durga temple','soli']
}
print(Travel_details)

def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (variable in letters): 
        return True 
    else:
        return False
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 
filtered = filter(fun, sequence) 
print('The filtered letters are:') 
for s in filtered: 
    print(s)