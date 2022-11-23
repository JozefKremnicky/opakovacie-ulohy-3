a='Python'
for i in range (len(a)):
    ra='.'*(len(a)-1)+a[i::-1]+a[:i+1]+'.'*(len(a))
    print(ra)
