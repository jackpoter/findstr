f = open(r'z:\日1.txt', 'rb')
a1 = f.read()
f.close()

f = open(r'z:\中1.txt', 'rb')
#b1 = f.read().decode('utf-8').encode('gbk')
b1 = f.read()
f.close()

c1 = open(r'z:\整理好.txt', 'wb')

nn = 0
m = 0
mm = 0
list = []
c = 0
ssplit = '\n'
nsplit = '\r\n'     # 2
msplit = '\r\n\r\n'

nn = 0
am = 0
bm = 0

while True:
    try:
        if am == 0:
            an = a1.index(nsplit,0)
            bn = b1.index(nsplit,0)
        else:
            an = a1.index(nsplit,am+1)
            bn = b1.index(nsplit,bm+1)
        if an > 2:
            if an - am == 2:
                #print 'i found c'
                #print 'b::', u(b2[n: n+2])
                c += 1
                am += 2
                bm += 2
                continue
        #c1.write(a1[am:an+1].replace('\r','').replace('\n',''))
        c1.write(a1[am:an+1].replace(nsplit,''))
        #c1.write('\t'+b1[bm:bn+1])
        c1.write(b1[bm:bn+1])
        c1.write(msplit)
        c1.write(nsplit)
        if am ==0:
            am += 1
            bm += 1
        else:
            am = an
            bm = bn
        nn += 1
    except:break


print 'done'
print 'nn:', nn
#print 'list:', list
print 'c:', c

