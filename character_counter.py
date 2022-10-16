def character_count():
    '''
    The purpose of this function is count the number of characters within a user's name
    '''

    #Prompts the user to enter their name
    user_name = input("Please enter your name: ")

    #Utilize the built-in len() function to count the characters in the name
    #and save the value to the variable
    count_of_name = len(user_name)

    print(f"Your name {user_name} has {count_of_name} characters in it.")

character_count()
