#break
#continue
#pass

'''while True:
    name = input('Enter you are name')
    if name != '':
        break'''
phone = 'M-a-n-o-h-a-r'
for i in phone:
    if i == '-':
        continue
    print(i,end='')


for i in range(1,50):
    if i ==26:
        pass
    else:
        print(i)



n = '897-831-5418'
for r in n:
    if r == '-':
        continue
    else:
        print(r,end='')