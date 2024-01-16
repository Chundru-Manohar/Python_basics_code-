student = ('manu','25','male')
print(student.count('manu'))
print(student.index('male'))
 # im mutable it cannot change index 
for r in student:
    print(r)
if 'manu' in student:
    print('Iam back') 

a = (10,20,30,40,50)
b = ('jenny','goldman','sliverman','jenny','goldman')
c = ('manu',20,True)
d = (10,)*10
e = (10)
f = (a,b,c)
print(type(d))
print(type(e))
print(a[4])
print(b[1:4])
print(b[::2])
print(len(f))
print(f)
print(f[1][2])
print(min(a))
print(b.count('jenny'))
print(b.index('jenny'))

l = [1,2,3,4,5]
print(tuple(l))

print(d)

h = ['manu','ravi','krishna','pk','mk']
print(h)
print(tuple(h))
