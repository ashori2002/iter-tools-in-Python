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
#___________________________________________________________________

X = itertools.repeat("ASHORI2002" , 5)
print(list(X))

#___________________________________________________________________
def test():
    from itertools import product
    print(list(product([1,2],repeat=2)))

test()