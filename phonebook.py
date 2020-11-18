import pickle

phonebook = {
    "Andrea": 12345678,
    "Robbie": 123456789
}

with open('phonebook.pickle', 'rb') as fh:
    phonebook = pickle.load(fh)

#print(phonebook1)

one_through_five = ''

def phone_function(one_through_five):
    one_through_five = input("""
        Electronic Phone Book
        =====================

         What do you want to do (1-5)?

            1. Look up an entry
            2. Set an entry
            3. Delete an entry
            4. List all entries
            5. Quit  """
            )
    name = ''
    number = ''
    if one_through_five == '1':
        name = input("Name, please: ")
        look_up_1(name)
    elif one_through_five == '2':
        name = input("New Name, please: ")
        number = input("New Number, please: ")
        set_entry(name, number)
    elif one_through_five == '3':
        name = input("What name would you like to delete?")
        delete_entry(name)
    elif one_through_five == '4':
        print(phonebook) 
        continue_on()
    elif one_through_five == '5':
        quit()

        

def look_up_1(name):
    ph_num = phonebook[name]
    print(f"{name}: {ph_num} ")
    continue_on()

def set_entry(name, number):
    phonebook[name] = number
    print(f"Entry stored for {name} at {number}")
    continue_on()


def delete_entry(name):
    del phonebook[name]
    print(f"Entry deleted for {name}.")
    continue_on()


def quit():
    with open('phonebook.pickle', 'wb') as fh:
        pickle.dump(phonebook, fh)
    print("Okay, goodbye.")

def continue_on():
    y_or_no = input("Would you like to continue? yes/no ")
    if y_or_no == 'yes':
        phone_function(one_through_five)
    else: 
        quit()


phone_function(one_through_five)
# print(phonebook)


    
        
        