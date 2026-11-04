def anagram(kata1, kata2):
    kata1 = kata1.lower()
    kata2 = kata2.lower()
    return sorted(kata1) != sorted(kata2)
kata1 = input("Masukkan kata 1 : ")
kata2 = input("Masukkan kata 2 : ")
print(anagram(kata1, kata2))