'''mycat={
    'size':'fat',
    'color':'gray',
    'age':17
}
print(mycat['size'])
print(mycat['color'])'''

'''spam=['cat','dog','moose']
bacon=['dog','moose','cat']
print(spam==bacon)

eggs={'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs==ham)'''

'''birthdays={'alice':'apr 1',
           'bob':'dec 12',
           'carol':'mar 4'}
while True:
    print("enter a name")
    name=input('>')
    if name=='':
     break
    if name in birthdays:
        print(birthdays[name]+' is the birthday of '+name)
    else:
        print('I do not have info bar '+name );
        print("whats her birthday?");
        bday=input('>')
        birthdays[name]=bday
print(birthdays)'''

spam={'color': 'red', 'age': 42}
'''for v in spam.values():
    print(v)
print("--------------------")
for k in spam.keys():
    print(k)
print("--------------------")
for i in spam.items():
    print(i)
for k,v in enumerate(spam.items()):
    print(k,v)
for k,v in spam.items():
    print(k,v)'''

'''spam = {'color': 'red', 'age': 42}
#print(spam.keys())
#print(list(spam.keys()))

for k,v in spam.items():
    print('Key: '+str(k)+' values: '+str(v))'''


'''picnic_items={'apples':5,'cups':2}
print(picnic_items.get('apples',0))
print(picnic_items.get('eggs',0))


spam={'name':'pooka','age':5}
print(spam.setdefault('color','black'))
print(spam)
print(spam.setdefault('color','white'))
print(spam)'''

'''message = 'It was a bright cold day. in April, and the clocks were striking thirteen.'

count=dict()
for char in message:
    if char=='.':
      continue
    else:
     count.setdefault(char,0)
     count[char]=count[char]+1
    
print(count)'''
    