import os

path = 'C:\\Users\\HP\\OneDrive\\Desktop\\mummy.txt'

if os.path.exists(path):
    print('the file is exist')
else:
    print('the file doesnt exist ')