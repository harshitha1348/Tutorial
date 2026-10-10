n = int(input())
a = list(map(int, input().split()))

max1_val = a[0]

for i in range(n):
    if a[i] > max1_val:
        max1_val = a[i]

print(max1_val)

