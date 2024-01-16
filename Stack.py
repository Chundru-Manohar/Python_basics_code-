#List  push append pop  pop
#modules

'''a = []
a.append(10)
a.append(20)
a.extend([30,40,50])
print(a)
a.pop()
print(a)
a.pop()
a.pop()
a.pop()
print(a)
a.pop()
print(a)'''
'''print(len(a) == 0) this method will check stack 
print(not a)'''

stack = []
def push():
 if len(stack) ==n:
        print("Stack is full")
 else:
      element = input("Enter a element:")
      stack.append(element)
      print(stack)

def pop_E():
 if not stack:
        print("stack is empty ")
 else:
        e = stack.pop()
        print("removed e",e)
        print(stack)

n=int(input("enter limit of the stack"))
while True:
    print("Select the operation 1.push 2.pop 3.quit ")
    a = int(input())
    if a ==1:
        push()
    elif a ==2:
        pop_E()
    elif a ==3:
        break
    else:
        print("Enter the correct operation")