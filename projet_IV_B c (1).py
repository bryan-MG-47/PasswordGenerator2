#project description:
                    #generate random passwords from random characters up to  the numbers of charcarters wanted by the user 


#import needed objects
import random
import string


def generate_passwords():
    # write "please enter the how many characters you want for your password:  " on the screen an wait for a value enter by the user an convert it into an int
    passwlenght = random.choice(range(8,12))
    # keep the list of all letters : return the object letters of type str
    letters=string.ascii_letters
    # keep the list of all digits : return the object digits of type str
    digits=string.digits
    # keep the list of all punctuation : return the object punctuation of type str
    #punctuation=string.punctuation
    punctuation=".<(>-=[{?)]}\%!"
    # keep all the characters of letters, digits, and punctuation : return the object asciiCombi of type str
    asciiCombi = letters + digits + punctuation
    # set the object password of type str
    password = ""



    # run the number of time conten by passwlenght
    for i in range(passwlenght):
        # create the password by randomly adding characters in it 
        password = password + (random.choice(asciiCombi))
    return (password)
#write the password on the screen
print (generate_passwords())




def verifyNames():
    ##user enters his/her name    
   name= input('Enter your name with at least 3 characters:')
    ##check the length   
   length=len(name)
       
   ##print(length)
    ##if the length is greater than 3  
   if length >3:
        ## print correct      
       print ('correct')
    ##if not print enter....       
   else:
       print('Enter a new name')
    ##return the name of the user     
   return (name)
    ## print the function   
print(verifyNames())






def ModifyThePassword():
    ##user enters his option to modify password  
    option = input ('chose either yes or no:' )
    ##if the user choses yes    
    if option=='yes':
        
    ##print.....        
        print('password modified')
        
    ##if the user choses no        
    elif option=='no':
    ##print....        
        print('password not modified')
    ##something other than yes or no    
    else:
    ##print......        
            print('invalid options')
    ##return the user's option           
    return(option)
##print the function
print(ModifyThePassword())
