slovo=input('zadaj slovo:')
a=0
for i in range(len(slovo)):
    if slovo[i]=='':
        a=a+1
print('pocet slov vo vete je:',a)
