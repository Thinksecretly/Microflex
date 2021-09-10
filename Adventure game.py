# Adventure game

import random
import time

print(f'Welcome to Microlex industires.')

microlex = ['Microlex']
time.sleep(2)
print('Nora: My name is Nora, and i will be helping you get set up.')
time.sleep(3)
print(f'Nora: Lets get started with finding out a little about you, for umm, ...')
time.sleep(5)
print('Nora: insurance purposes. ')
time.sleep(3)
print(f'Nora: Please fill out the wavier below.')

player_name = input('First Name: ')
emergency_contact = input('Emergency contact: ')

print(f'Nora: Thank you {player_name}, your time is very valuable to us. ')
time.sleep(1)
print(f'Nora: Please wait here while we get everything ready...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
print(f'Nora: Ok {player_name}, we are ready for you, right this way.')

follow = input('DO YOU FOLLOW? ').lower
if 'y' in follow:
    print(f'Nora: So {player_name}, I am really glad you decided to join us in our 100% safe trials.  ')
elif 'n' in follow:
    print('YOU STAND IN THE LOBBY SECOND GUESSING YOURSELF')
    time.sleep(1)
    print('A STRANGE CRUMBLING SOUND COMES FROM ABOVE YOU ')
    time.sleep(1)
    print('BEFORE YOU HAVE TIME TO REACT, THE METAL INDUSTRIAL LIGHT FIXTURE ABOVE YOU GIVES WAY TO THE ENTICING ALLURE OF GRAVITY AND BREAKS FREE')
    time.sleep(1)
    print('YOU ONLY HAVE SECONDS TO REALIZE YOU ARE ALREADY DEAD')
    exit(0)


