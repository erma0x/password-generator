# Password genrator


if __name__ == '__main__':
           import random as rnd
           import sys

           length = int(sys.argv[1])

           lower_letters = 'qwertyuiopasdfghjklzxcvbnm'
           upper_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
           numbers = '1234567890'
           symbols = "[]{}();,./@#$%^&*"


           all_elements = lower_letters + upper_letters + numbers + symbols


           password = "".join(rnd.sample(all_elements,length))
           print(password)
