'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
pos = -1

def binarysearch(lists,n):
    l = 0
    u = len(lists)-1
    while l <= u:
        mid = (l+u) // 2
        if lists[mid] == n:
            globals()['pos']=mid
            return True
        else:
            if lists[mid]<n:
                l = mid+1
            else:
                u = mid-1
            
    return False

lists = [66,85,90,100]
n = int(input())

if binarysearch(lists,n):
    print("Data found at ",pos+1)
else:
    print("Data not found in the database")
