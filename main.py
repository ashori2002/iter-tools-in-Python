import itertools

for i in itertools.count(1 , 2):
    if(i < 21):
        print(i)
    else:
        break
#___________________________________________________________________
numbers = len("ASHORI2002")
for i in itertools.cycle("ASHORI2002"):

    if (numbers <= 0):
        break
    else:
        print(i)
    numbers -= 1

