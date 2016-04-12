
##############
# String functions #
##############
'''
    Function that meets the following reqs:
1. Accepts a string > 3 characters.
2. If the string is less than 3 characters throw and Exception with an appropriate message.
3. Capitializes ONLY the first letter in the sentence.
4. Replaces all letters 'z' or 's' with '5'.
5. Returns the new string (with capitialization and replaced letters)
'''
# String Check
def checkString(string):
    if len(string) < 3 :
        raise Exception('Length of the string is less than 3')
    CapsString = string[0].upper()
    var = string[1:]
    RepString = CapsString.replace('s','5').replace('z','5')
    return CapsString+RepString


'''
    Function that meets the following reqs:
1. Accepts a string > 3 characters.
2. If the string is less than 3 characters throw and Exception with an appropriate message.
3. If the string contains any non-alpha characters, throw an appropriate message
4. Make all of the characters in the string lowercase
5. Reverse the string
6. Return the new string.
'''

#String reverse
def CheckString_two(string):
    if len(string) < 3:
        raise Exception('Length of the string is less than 3')
    isalpha = string.isalpha()
    if isalpha == False:
        raise Exception('String should contain only alphabets')
    else:
        lower_string = string.lower()
        final_string = lower_string[::-1]
        return final_string


# String manipulation
'''
    Function that meets the following reqs:
1. Accepts 3 string parameters, a full sentence, a string to be replaced, and the string to replace it with
2. This function will take a full string, and replace all instances of the "string to be replaced" with
   the "string to replace"...
3. for example: func("Hello World", "Hello", "Good Bye") would return "Good Bye World"
'''

def string_manipulation(string1,string2,string3):
    manipulated_string = string.replace(string2,string3)
    return manipulated_string

#########
# TESTS Methods#
#########

# String Check
def test_String_Check():
    try:
        try:
            checkString('ar')
            raise Exception('Question 1 Failed.... No exception was thrown with a string of len 2')
        except:
            print('Length requirement passed.')

        test_return = checkString('this string should come back correctly!')
        if test_return != 'Thi5 5tring 5hould come back correctly!':
            raise Exception('Q1 Test for capitialization FAILED!, The string returned was:' + test_return)
        else:
            print('Good Job! Q1, Test 2 PASSED!')

    except Exception as ex:
        print('Ooops, please try question one again.', ex)


# string reverse
def test_string_reverse():
    try:
        try:
            CheckString_two('ar')
            raise Exception('Question 1 Failed.... No exception was thrown with a string of len 2')
        except:
            print('Length requirement passed.')

        try:
            CheckString_two('python123')
            raise Exception('Question 1 Failed.... No exception was thrown with a string of Alpha Numeric')
        except:
            print('NonAlpha requirement passed.')

        test_return = CheckString_two('StrinG')
        if test_return != 'gnirts':
            raise Exception('Test for string reverse failed')
        else:
            print('Good Job! Q2 Test3 has been PASSED!')

    except Exception as ex:
        print('Ooops, please try question one again.', ex)


# string manipulation
def test_string_manipulation():
    try:
        test_string = string_manipulation('Arun Kambhammettu','Kambhammettu','Arun')
          if test_string != 'Arun Kambhammettu':
              raise Exception('Input is not valid')
          else:
              print('Good Job! Q3 Test has been PASSED!')

    except Exception as ex:
        print('Ooops, please try question one again.', ex)


#######################
# MAIN                #
# THIS RUNS THE TESTS #
# DO NOT MODIFY       #
#######################

if __name__ == '__main__':
    test_String_Check()
    test_string_reverse()
    test_string_manipulation()
