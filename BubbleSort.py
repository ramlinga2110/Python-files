'''

Welcome to Python DSA.

'''

def sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp



num = [25,4,2,9,1,5,7,22,88,55,48,42,15,16,81]
sort(num)

print(num)