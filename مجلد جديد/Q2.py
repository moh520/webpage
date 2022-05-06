L = []
N = int (input(" enter your first N : "))
L.append(N)
i = 0
res = 0
while N != 0 :
    res = res + (N %2)*(10**i)
    N = N // 2
    i+=1
print ("the binary number is : ",res)
print ()

