


def linersearch(lists,n):
    i = 0
    while i < len(lists):
        if lists[i] == n:
            return True
        i = i+1
    return False




lists = [2,6,4,9,8,22,99,1,66,58,32]
n = int(input())

if linersearch(lists,n):
    print("found in the existing data")
else:
    print("not found in the existing data")