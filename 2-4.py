a = int(input("number of the students in the class"))
S = 0
L = []
for i in range(a):
    score = int(input("enter the score"))
    L.append(score)
    S += score
print(max(L))
print(min(L))
print(float(S/a))