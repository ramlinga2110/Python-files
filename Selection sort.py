'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

def sort(unsort):
    for i in range(len(unsort)):
        minpos = i
        for j in range(i,len(unsort)):
            if unsort[j] < unsort[minpos]:
                minpos = j 
        temp = unsort[i]
        unsort[i] = unsort[minpos]
        unsort[minpos] = temp
    
        print(unsort)




unsort = [55,66,77,88,99,11,22,33,44,12,13,14,15,16,]

sort(unsort)

print(unsort)