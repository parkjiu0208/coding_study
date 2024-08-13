li = map(int, input().split())
hap = 0

for i in li:
    hap = hap + i**2
    
print(hap%10)