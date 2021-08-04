s = int(input("how many seconds ?"))
a = s // 3600
b = s - (a*3600)
c = b // 60
d = s % 60
print(a,":",c,":",d)
