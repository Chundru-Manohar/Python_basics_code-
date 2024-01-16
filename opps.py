class Employee:
    wheels = 4
    def __init__(self,name,age,id,bloodgroup,mobileNo,date_of_DoB):
        self.name = name
        self.age = age
        self.id = id
        self.bloodgroup = bloodgroup
        self.mobileNo = mobileNo
        self.date_of_DoB = date_of_DoB

    def login(self):
        print('The person is '+self.name+' login at 8.30AM ')

    def logout(self):
        print('The person is '+self.name+' logout at 6.30PM ')     