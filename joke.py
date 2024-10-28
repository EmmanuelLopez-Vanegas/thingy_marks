import time

def joke1():
    print('Why did the scarecrow win an award?')
    time.sleep(1)
    print('Because he was outstanding in his field!')

def joke2():
    print('What do you call fake spaghetti?')
    time.sleep(1)
    print('An impasta!')

def joke3():
    print('Why did the bicycle fall over?')
    time.sleep(1)
    print('Because it was two-tired!')

joke = int(input('Choose a joke you would like to hear? (1/2/3)'))
if joke == 1:
    joke1()
elif joke == 2:
    joke2()
elif joke == 3:
    joke3()

