a2 = int(input("a2 = "))
a1 = int(input("a1 = "))
b2 = int(input("b2 = "))
b1 = int(input("b1 = "))

r2 = a2 + b2 + ((a1 + b1) // 10)
r1 = (a1 + b1) % 10

print(r2, r1)
