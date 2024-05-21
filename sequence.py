# List
students = ['Musa', 'Umar', 'Muhammad', 'Isah', 'Hafiz']

states = ['Abuja', 'Lagos', 'Kano', 'Jigawa', 'Zamfara']
#the following code will marge the values of "states" and "students"
states.extend(students)
states.remove('Abuja')
#the code below will remove out the value in respect to the provided index number.
states.pop(1)

print(states)
print(students)

# print(len(states))
# print(type(states))
# states[2] = 'Yobe'
# states[2:4] = ['Edo','Imo','Ekiti']

# states.append('Sokoto')
# states.insert(2, 'Jos')
# print(states)
# print(states[2:5])


# TUPLE
Customers = ('Musa', 'Umar', 'Muhammad', 'Isah', 'Hafiz')
# print(Customers)

# SET
users = {'Musa', 'Umar', 'Muhammad', 'Isah', 'Hafiz'}
users.add('katsina')
# print(users)

# DICTIONARY
members = {
    'name': 'Umar',
    'nick': 'Halifa',
    'edu': 'Bsc. Cyber Sec',
    'state': 'Kano'
}
x= members.get('nick')
y=members.keys()
z=members.values()
print(x)
print(y)
print(z)
# print(members)
# print(members['edu'])
# print(len(members))
# print(type(members))