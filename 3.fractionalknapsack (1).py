n = int(input("Enter number of items: "))
w = list(map(int, input("Enter weights: ").split()))
p = list(map(int, input("Enter profits: ").split()))
c = int(input("Enter capacity: "))

items = sorted(zip(w, p), key=lambda x: x[1]/x[0], reverse=True)

total = 0

for wt, pr in items:
    if c >= wt:
        total += pr
        c -= wt
    else:
        total += pr * c / wt
        break

print("Maximum profit:", total)