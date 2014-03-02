f = open(r'z:\a1.txt', 'rb')
a1 = f.read()
f.close()

nn = 0
m = 0
list = []
while(1):
    try:
        n = a1.index('\n',m+1)
        list.append(n)
        m = n
        nn += 1
    except:break

print 'done'
print 'nn:', nn
print 'list:', list
