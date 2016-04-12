######################################################
#   Name: Arun Kambhammettu
#   --------------------------------------------------
#   Basic Python Conditional Statements, Loops and functions
#
######################################################

'''
  A function named add_me that accepts two numbers, adds them, then returns the result.
'''
def add_me(num_one, num_two):
    return num_one + num_two

'''
    A function function named "dedupe" that accepts two lists as parameters, for example
    dedupe(list_one, list_two).

    The function will return a new list that contains only unique values that occurred in either
    one of the lists.
'''
def dedupe(list1,list2):
	return list(set(list1+list2))

'''
    A function named "show_dinner_menu" that does the following:
    1. The function will have no parameters
    2. The function will display an input prompt to the user with a menu of 4
       food options.
    3. When the user selects a valid option the function will return a description
       of their meal
    4. We will make sure that if the user does NOT select a valid option it asks them to try again
'''
def show_dinner_menu():
    #print what menu we have
    print ' '
    print 'Welcome to Indian Food Hotel please select menu from below options'
    print ' '
    print '1) Biryani'
    print '2) Panipuri'
    print '3) Bhel Chat'
    print '4) Dosa'
    print '5) Quit menu'
    print ' '
    return input ('Choose your option: ')

loop = 1
choice = 0
while loop == 1:
    choice = show_dinner_menu()
    if choice == 1:
        print 'Boiled rice with hot and spicy chicken and roasted vegetables with Paneer and with loads of cheese'
    elif choice == 2:
        print 'Small pots filled with cilantro juice and mashed potato'
    elif choice == 3:
        print 'Spicy bhel roasted with tomato and onions'
    elif choice == 4:
        print 'Roasted maida filled with grilled cheese and onions'
    else:
        print 'Please choose a valid option from menu and try again !!'
        loop = 0
print 'Thank you for choosing our Hotel'





#################################
# These are the TESTS                        #
# No Need to MODIFY, Just these lines to see test results.#
###############################################################################################
# add me 
def test_add_me_Function():
    try:
        result = add_me(5, 8)
        if result != 13:
            raise

        result = add_me(-5, 3)
        if result != -2:
            raise

        print('Sample Question Passed! Great Job!')
    except:
        print('Ooops, please try the sample question again.')
# dedupe test
def test_dedupe():
    try:
        l_one = [1,2,3,4]
        l_two = [2,5,6,7]
        deduped = dedupe(l_one, l_two)
        if (deduped.count(2) > 1) or len(deduped) < 7:
            raise
        else:
            print('Dedupe function Passed! Great Job!')
    except:
        print('Ooops, please try question one again.')

#######################
# MAIN                #
# THIS RUNS THE TESTS #
# DO NOT MODIFY       #
#######################

if __name__ == '__main__':
    test_add_me_Function()
    test_dedupe()
