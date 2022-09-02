# Password genrator

import random as rnd
import sys
           
if __name__ == '__main__':
    length = 20
    
    if len(sys.argv)>1:
    	length = int(sys.argv[1])
    	
    lower_letters = 'qwertyuiopasdfghjklzxcvbnm'
    upper_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    numbers = '1234567890'
    
    all_elements = lower_letters + upper_letters + numbers
    
    password = "".join(rnd.sample(all_elements,length))
    
    print('\n\t password generated!')
    print('\n\t',password,'\n\n')
