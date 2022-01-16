#Contact Keeper Program
contact_list = {};

def addPerson(name, firstcontact):
    
    contact_list[name] = [firstcontact]
    
def addContact(name, add):

    contact_list[name].append(add)

def viewAll():
    for key in sorted(contact_list.keys()):
        print(key)
        print(contact_list[key])
        print()

def getContact(name):
    print(contact_list[name])

def findKey(str):
    
    for x in sorted(contact_list.keys()):

        if x in str:
            print(x,end=' ')
            print(contact_list[x])
        
while True:
    print("Welcome to Contact Manager")
    print('1. Add a new Person to the Contact List')
    print('2. Add a new Contact of the existing Person')
    print('3. View all given contact')
    print('4. Retrive contact number for particular person')
    print('5. Retrive contact of matched string.')
    choice = input('Enter Your Choice : ')


    if choice == '1':
        name = input('Name: ')
        firstcontact = input('Contact number: ')
        addPerson(name,firstcontact)

    elif choice == '2':
        name = input('Name: ')
        add = input('Contact number: ')
        addContact(name,add)

    elif choice == '3':
        viewAll()

    elif choice == '4':
        name = input('Name: ')
        getContact(name)

    elif choice == '5':
        string = input('enter string: ')
        findKey(string)
    else:
        break
