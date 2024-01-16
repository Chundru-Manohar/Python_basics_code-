# zip (*iterables) = aggregate elements from two are more iterableabc@123

a = ['manu','ravi','chait']
b = ['pass@wo','abc@123','Mk@we']
f = ['1/1/2021','2/2/2022','3/3/2023']

h = list(zip(a,b,f))
z= h[0]
print(z)

for i in h:
    print(i)




c = list(zip(a,b))
d = dict(zip(a,b))

for key,value in d.items():
    print(key+" "+value)
    
print(type(d))
for i in c:
    print(i)

if __name__ == "__main__":
    print(f'both are equal ')
else:
    print('both are not equal ')