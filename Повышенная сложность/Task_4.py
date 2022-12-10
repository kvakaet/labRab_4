k = int(input("k = "))
posl = 0
n = 1
num = 1
for i in range(10, 100):
    if k == n or k == n + 1:
        print("номер пары k-той цифры:", num)
        print("число, в которую входит k-тая цифра:", i)
        if k % 2 == 0:
            print(i // 10)
        else:
            print(i % 10)
    n += 2
    num += 1
    posl = posl * 100 + i
