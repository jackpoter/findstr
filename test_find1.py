f = open(r'z:\a1.txt', 'rb')
a1 = f.read()
f.close()

nn = 0
m = 0
list = []
while True:
    try:
        n = a1.index('\n',m+1)
        list.append(n)
        m = n
        nn += 1
    except:break

print 'done'
print 'nn:', nn
print 'list:', list


'''
done
nn: 19
list: [5, 7, 101, 169, 259, 337, 479, 581, 663, 717, \
807, 867, 941, 1003, 1093, 1145, 1181, 1213, 1263]
'''
