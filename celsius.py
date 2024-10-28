temp = input('Here we will be calculating temperature from Celsius to Farenheit, what unit? F/C ')
if temp == 'F':
    thing = int(input('What temperature is it?'))
    cels = (thing-32)*5/9
    print(cels)
elif temp == 'C':
    thing = int(input('What temperature is it?'))
    fare = (thing*9/5)+32
    print(fare)