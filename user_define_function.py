'''
def hello():
    print("good morning");
    print("good afternoon");
    print("good evening");
hello();
print('one more time');
hello();
'''
'''
def say_hello(name):
    print('good morning '+name);
    print('good afternoon '+name);
    print('good evening '+name);
    
say_hello('alice');
say_hello('bob');
'''

'''
import random
def get_answer(answer_number):
    if answer_number==1:
        return "one";
    elif answer_number==2:
        return "two";
    elif answer_number==3:
        return "three";
    elif answer_number==4:
        return "four";
    elif answer_number==5:
        return "five";
    elif answer_number==6:
        return "six";
    elif answer_number==7:
        return "seven";
    elif answer_number==8:
        return "eight";
    elif answer_number==9:
        return "nine";
    
r=random.randint(1,9);
my_number=get_answer(r);
print(my_number);
'''

'''
import random
for i in range(10):
    if random.randint(0,1)==0:
        print('H',end= ' ');
    else:
        print('T',end=' ');

print('cat','dog','mice');
print('cat','dogs','mice',sep=',')
'''

'''
def a():
    print('a() starts');
    b();
    print('a() ends');
def b():
    print('b() starts');
    c();
    print('b() ends');
def c():
    print('c() starts');
    print('c() ends');

a();
'''
'''
def spam():
    eggs='sss';
spam()
print(eggs);
'''
'''
eggs='GLOBAL'
def spam():
    eggs='SPAM';
    beacon();
    print(eggs);
def beacon():
    ham='HAM';
    eggs='BEACON';
    print(eggs)
spam();
print(eggs)
'''
'''
def spam():
    eggs='eggs in spam';
    print(eggs);
def bacon():
    eggs='eggs in bacon';
    spam();
    print(eggs);
eggs='eggs in global';
bacon();
print(eggs);
'''
'''
def spam():
    global eggs;
    eggs='spam';
eggs='global'
spam();
print(eggs)
'''