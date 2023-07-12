import os

num = 0
cnt  = 0

for rt, _, files in os.walk("."):
    for file in files:
        if file.split('.')[-1] == "md":
            with open(rt + '\\'+file, 'r') as f:
                num += 1
                cnt += len(''.join(f.readlines()))
                
print(cnt, num)