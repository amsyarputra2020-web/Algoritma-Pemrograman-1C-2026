n = int(input("Masukkan angka : "))
for i in range (1, n+1) :
    for j in range(1, i+1) :
        print(j, end="")
    if n%2==0:
        for s in range((n-i)*2) :
            print(" ", end="")
    else :
        for s in range((n-i)*2-1):
            print(" ", end="")
    for k in range(i - 1 if i == n and n % 2 == 1 else i, 0, -1):
        print(k, end="")
    print()