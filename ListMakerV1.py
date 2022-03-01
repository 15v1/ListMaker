import random, string
from colorama import *
init(autoreset=True)
print(Fore.RED+ 'Make Sure To Make List.txt File First!!!')
a=input("[1] only letters \n [2] letters & numbers  \n choose: ")
if a=='1':
    te=string.ascii_letters
    length = int(input('Enter Word Length : '))
    count = int(input('How Many Words : '))
    with open("list.txt", 'a') as file: #make sure to make list.txt file first
        for x1 in range(count): 
            ww1=''.join(random.choice(te) for x1 in range(length))
            if x1 == range(count)[-1]:
                file.write(ww1+'\n')
            else:
                file.write(ww1+'\n')
if a=='2':
    text3=  string.digits+string.ascii_letters
    length = int(input('Enter Word Length : '))
    count = int(input('How Many Words : '))
    with open("list.txt", 'a') as file: #make sure to make list.txt file first
        for x in range(count): 
            ww=''.join(random.choice(text3) for x in range(length))
            if x == range(count)[-1]: 
                file.write(ww+'\n')
            else:
                file.write(ww+'\n')


    
