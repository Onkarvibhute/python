'''import random
for i in range(5):
    nums=[1,2,4]
    #print(round(random.random()));
    #print(random.randint(1,10));
    #print(random.choice(range(5)));
    (random.shuffle(nums));
    print(nums)
'''
import sys
'''
while True:
    print('Type exit to exit');
    response=input('>');
    if response=='exit':
        sys.exit();
print('loop break');
'''
while True:
    print('Type exit to exit');
    response=input('>');
    if response=='exit':
        break;
print('loop break');
