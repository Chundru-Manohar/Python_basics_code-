# sort method used list

# sort function used iterables

people = ('ravi','manu','chait','krishna','tarun','Anil','pawan')

s_p = sorted(people,reverse=True)
#people.sort(reverse=True)

#for i in people:
#    print(i)
for i in s_p:
    print(i)

Student = [('ravi','A',30),
           ('manu','D',25),
           ('anil','C',30),
           ('tarun','B',50),
           ('lion','F',55),
           ('Amma','R',70)]


age = lambda ages:ages[2]
Student.sort(key=age,reverse=True)

for i  in Student:
    print(i)

people = ('ravi','manu','chait','krishna','tarun','Anil','pawan')
'''people.sort()
for i in people:
    print(i)'''

S_N = sorted(people,reverse=True)
for i in S_N:
    print(i)

