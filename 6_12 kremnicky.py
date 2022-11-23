retazec1=''
retazec2=''
retazec3=input('zadaj slovo:')
for i in range(len(retazec3)):
    retazec1=retazec3[i]+retazec1
    retazec2=retazec2+retazec3[i]
    print(retazec1)
    print(retazec2)
