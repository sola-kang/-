T = int(input())

sosu = [True] * (1299709 + 1)
sosu[0], sosu[1] = False, False
for i in range(1, 1299709 + 1):
    if not sosu[i]:
        continue
    for j in range(i * i, 1299709 + 1, i):
        sosu[j] = False

for _ in range(T):

    N = int(input())
    if sosu[N]:
        print(0)
    else:  
        i = N  
        j = N  
        count = 1  
        while True:  
            i -= 1
            if sosu[i]:
                break
            count += 1  
        while True:  
            j += 1
            if sosu[j]:
                break
            count += 1  
        print(count + 1)
