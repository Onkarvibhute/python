'''def spam(divided_by):
    return 42/divided_by;

try:
    print(spam(2));
    print(spam(6));
    print(spam(7));
    print(spam(12));
    print(spam(0));
except ZeroDivisionError:
    print('error:invalid args');
finally:
    print('function ends');
'''


'''
def box_print(symbol,width,height):
    if len(symbol)!=1:
        raise Exception('Symbol must be a single character string');
    if width<=2:
        raise Exception('width must be grater than 2');
    if height<=2:
        raise Exception('Height must be greater than 2');
    
try:
    box_print('**',4,4);
except Exception as error:
    print(error);
 '''    
''' 
def calculator(a,b):
      division =a/b;
      if b==0:
          raise ZeroDivisionError;
      multiple=a*b;
      if b==1:
          raise Exception('mul');
try:
  calculator(1,0);
  
except ZeroDivisionError as err:
    print(err);
try:
    calculator(1,1);
except Exception as err:
    print(err);
'''


ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73];
ages.sort()
assert ages[0]>=ages[-1];