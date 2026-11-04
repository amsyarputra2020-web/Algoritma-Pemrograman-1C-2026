def fibonacci(hari) :
    if hari == 1:
        return 1
    elif hari == 2:
        return 1
    else :
        return fibonacci(hari - 1) + fibonacci (hari - 2)
hari = int(input("Masukkan hari : "))
print(fibonacci(hari))