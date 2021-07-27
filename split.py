n=[50,49,23,56,100,98]
i=0
max=0
s_max=0
while i<len(n):
    if n[i]>max:
        s_max=max
        max=n[i]
    if s_max<n[i] and n[i]<max:
        s_max=n[i]
    i=i+1
print(s_max)