fd=open('sample.txt','r')
s=fd.read()
print(s)
a=''
for i in s:
    if i.isdigit():
        a+=i
fd.close()
print(a)
