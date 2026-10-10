n = int(input())
a = list(map(int, input().split()))

max1_val = a[0]
max2_val = a[0]

for i in range(n):
    if a[i] > max1_val:
        max2_val = max1_val
        max1_val = a[i]
    if a[i] < max1_val and a[i] > max2_val:
        max2_val = a[i]

print("Max:", max1_val)
print("Second Max:", max2_val)
