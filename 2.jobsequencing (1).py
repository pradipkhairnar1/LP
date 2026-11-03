jobs = [(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 3, 15)]

jobs.sort(key=lambda x: x[2], reverse=True)

n = max(j[1] for j in jobs)
slots = [None] * n
profit = 0

for job in jobs:
    for i in range(job[1] - 1, -1, -1):
        if slots[i] is None:
            slots[i] = job[0]
            profit += job[2]
            break

print("Scheduled jobs:", [j for j in slots if j])
print("Maximum profit:", profit)