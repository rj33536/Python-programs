n=13
for i in range(n):
    print()
    if i<n/2-1:
        print("*",end=' ')
        for j in range(int(n/2)-1):
            print(" ",end=' ')
        print("*",end=' ')
    if i==0:
        for j in range(int(n/2)):
            print("*",end=' ')
    if i==int(n/2):
        for j in range(n):
            print("*",end=' ')
    if i>int(n/2):
        if i==n-1:
            for j in range(int(n/2)):
                print("*",end=' ')
        else:
            for j in range(int(n/2)):
                print(" ",end=' ')
        print("*",end=' ')
        for j in range(int(n/2)-1):
            print(" ",end=' ')
        print("*",end=' ')
