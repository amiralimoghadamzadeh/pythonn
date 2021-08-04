import random
while True:
    a = random.randint(1,6)
    if a == 6:
        b = random.randint(1,6)
        print("you are lucky!",b)
        break
    else:
        print("not this time",a)
          
