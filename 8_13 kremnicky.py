veta = input('zadaj vetu:')
for i in range (len(veta)):
    if veta[i]=='!':
        print('rozkazovacia')
    if veta[i]=='?':
        print('opytovacia')
    if veta[i]=='.':
        print('oznamovacia')
