def bisiesto(a):
    if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
        return "{} es bisiesto ".format(a)
    return "{} no es bisiesto ".format(a)

for i in range(2018,2026):
    print(bisiesto(i))        
