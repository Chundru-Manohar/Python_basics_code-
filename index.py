#indexing = it gives sequence of element
name = 'manohar is a good boy!'
if (name[0].islower()):
    name = name.capitalize()

print(name)
first_name = name[7:].lower()
print(first_name)

last_Name = name[0:7].upper()
print(last_Name)

charcto = name[-1]
print(charcto)