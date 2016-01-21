#!/usr/bin/python
# Kristina Beck

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!


print ('''Hello :)    
Choose a language and I'll greet you in that language!
1. Spanish
2. Dutch
3. French ''')  # greeting in multi-line print

language = input('Choose your language: ')  # request for user to choose a language

if language == 1:     # greeting options : set language variable option 1
    print 'Hola'      # printing variable assigned alias
if language == 2:     # greeting options : set language variable option 2
    print 'Hallo'     # printing variable assigned alias
if language == 3:     # greeting options : set language variable option 3
    print 'Bonjour'   # printing variable assigned alias


