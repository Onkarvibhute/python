'''spam="That is \alice's cat"
print(spam)
spam='say hi to bob\'s mother'
print(spam)
spam="say hi to \tbob\'s mother"
print(spam.expandtabs(1))
spam="say hi to \nbob's mother"
print(spam)'''

#print(r'The file is in c:\users\alice\desktop')
#print('hello...\n\n...world')
#print(r'hello...\n\n...world')
#
#print('''dear alice,
 #     can you feed eve\'s cat this weekend?
  #    sincerely,
   #    bob''')
#

'''greeting='Hello, world!'
print(greeting[0])
print(greeting[0:5])
print(greeting[7:-1])
print(greeting[-1:4:-1])
print(greeting[-1:-4:-1])'''

'''print('hello' in 'hello,world')
print('  ' in 'spam')'''

'''name='AI'
age=4000
print('my name is '+name+' and ')
print(f'my name is {name} and my age is {age}')
print('my name is %s. I am %s years old.' %(name,age))'''

'''spam="Hello,world!"
print(spam.lower())
print(spam.islower())
print(spam.upper())
print(spam.isupper())
print('HELLO'.lower().islower())'''

'''print('hello'.isalpha())
print('hello123'.isalpha())
print('hello123'.isalnum())
print('123'.isdecimal())
print(' '.isspace())
print('This Is Title Case'.istitle())'''

'''print('hello,world!'.startswith("hello"))
print('hello,world!'.endswith("world"))'''

'''print(['cats','rats','bats'])
print(','.join(['cats','rats','bats']))
print(''.join(['cats','rats','bats']))
print(' '.join(['cats','rats','bats']))
print('abc'.join(['cats','rats','bats']))'''


'''print('my name is simon'.split())
print('my name is simon'.split('m'))'''

#spam = '''Dear Alice,
 #There is a milk bottle in the fridge
 #that is labeled "Milk Experiment."

 #Please do not drink it.
 #Sincerely,
 #Bob'''
'''print(spam.split())
print('\n\n')
print(spam.split('\n'))'''

'''print('Hello'.rjust(10,'*'))
print('Hello'.rjust(20,'*'))
print('Hello'.ljust(10,'*'))
print('Hello'.center(20,'='))

spam='*****hello,world*****'
print(spam.strip('*'))
print(spam.lstrip('*'))
print(spam.rstrip('*'))

spam='SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('Bacon'))'''

'''print(ord('A'))
print(ord('a'))
print(chr(65))
print(chr(97))'''
'''
import pyperclip
pyperclip.copy('hello,world!')
print(pyperclip.paste())'''