t = input("enter time (hh:mm:ss)")
a = int(t[0])
b = int(t[1])
c = int(t[3])
d = int(t[4])
e = int(t[6])
f = int(t[7])
A = (a + b) * 3600
B = (c + d) * 60
C = e + f
print(A + B + C)
