'''
spam=['cat','bat','rat','elephant']
print(spam)
for i in range(len(spam)):
    print(spam[i])
for i in range(len(spam)):
    print('Hello '+ spam[i]);
for animal in spam:
    print(animal);
'''

'''spam=[['cat','bat'],[10,20,30,40,50]]
print(spam[0])
print(spam[0][1])'''

'''spam=['cat','bat','rat','elephant']
print(spam[-1])'''

'''spam=['cat','bat','rat','elephant']
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])
print(spam[0:])'''

'''l1=[1,2,3]
l2=['a','b','c']
print(l1+l2);
print(l1*3)
l1=l1*2+l2
print(l1)'''

'''spam=['cat','bat','rat','elephant']
del spam[2]
print(spam)'''

'''animals=[]
while True:
    print("\nenter animals name")
    name=input()
    if name=='':
        break;
    animals=animals+[name];
for x in animals:
        print(x, end=' ')'''

'''while True:
 my_pets=['a','b','c','d']
 print('enter ur pet name')
 name=input('>')
 if name=='':
     break
 if name not in my_pets:
    print(name + " "+"not in the list")'''
 
'''my_pets=['a','b','c','d']   
while True:
 
 print('enter ur pet name')
 name=input('>')
 if name=='':
     break
 if name not in my_pets:
    print(name + " "+"not in the list")
    print("do u want to add "+name+ " in the list")
    
    if input().lower()=="yes":
      my_pets.append(name)
print(my_pets)'''     
  
'''cat=['fat','gray','loud']
size,color,sound=cat;
print(size)
print(color)
print(sound)'''

'''
supplies = ['pens', 'staplers', 'flamethrowers', 'binders'];
for index,item in enumerate(supplies):
    #print(str(index)+"->"+item)
    print(index,item)'''
   
   
import random
'''
while True:  
  pets=['dog','cat','moose']
  if input()=="x":
   print(random.choice(pets))
  else:
      break
'''

'''people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
print(people)
'''

'''spam = ['hello', 'hi', 'howdy', 'heyas']

print(spam.index('hello'))
spam.append('hola')
print(spam)'''

'''
spam = ['cat', 'dog', 'bat']
spam.insert(1,'chicken')
print(spam)
spam.remove('dog');
print(spam)
'''

'''spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spam = ['Ants', 'Cats', 'Dogs', 'Badgers', 'Elephants']
spam.sort()
print(spam)'''

'''spam = ['b','D','B','C','A','a']
spam.sort(key=str.lower)
print(spam)'''

'''spam = ['cat', 'dog', 'moose']
spam.reverse()
print(spam)'''

'''name='zophie a cat'
print(name[-4])
name[-4]="x";
print(name)'''

'''name='zophie a cat'
new_name=name[0:7]+"the"+name[8:12]
print(new_name)'''

