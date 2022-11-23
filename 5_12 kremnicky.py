veta1=input('zadaj vetu1=') #zadanie 1 vety
veta2=input('zadaj vetu2=') #zadanie 2vety
retazec='' #vytvorenie prazdnej vety
pocet=len (veta1)+len(veta2)
for i in range(pocet):
    if i %2==0:
        retazec += veta1[i//2]
    else:
        retazec += veta2[i//2]


print (retazec)
