
def get_initials(fullname):
    seperated_name = fullname.split(' ') #split name by spaces
    initials = ''
    for name in seperated_name: #creates loop for each first, middle and last name
        initials = initials + name[0].upper()  #capitalize initial and add each 0 position letter to the previously 0 position letter from the previously iterated initials
    return(initials) 
        
print get_initials('ozzie smith')

