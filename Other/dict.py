from collections import defaultdict

d = defaultdict(int)
for i in range(3):
    d[i] = i * 3

for i in range(5):
    d[i] += 1

print(*d)
