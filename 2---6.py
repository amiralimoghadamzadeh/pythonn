def f(n):
    if n <= 0 :
        print("wrong input")
    elif n == 1 or n == 2:
        return("1")
    else:
        return(f(n-1) + f(n-2)) 

L = []
a = int(input("terms"))
for i in (1,a):
    L.append(f(i))

print(L)