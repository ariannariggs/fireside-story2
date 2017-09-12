def get_initials(fullname):
    seperated_name = fullname.split(' ') #split name by spaces
    initials = ''
    for name in seperated_name: #creates loop for each first, middle and last name
        initials = initials + name[0].upper()  #capitalize initial and add each 0 position letter to the previously 0 position letter from the previously iterated initials
    return(initials) #returns the initials joined by the + sign

def main():
    user_input = input("What is your full name?") #asks the user for their name
    initl= user_input #defines the user input under a new variable
    print(get_initials(initl)) #runs the new variable (user input) through the get_initials function and prints initials

if __name__ == '__main__':
    main()