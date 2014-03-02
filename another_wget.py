# -*- coding: utf-8 -*-
import urllib2, urllib, sys
import random, time
import re

starttime = time.time()

_error=0
times=300
g_url = 'http://filex.sdufe.edu.cn/down.php'
r_url = 'http://filex.sdufe.edu.cn/'
url = g_url

enable_proxy = False     #
proxy_handler = urllib2.ProxyHandler({"http" : 'http://127.0.0.2:88'})
null_proxy_handler = urllib2.ProxyHandler({})

if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)

urllib2.install_opener(opener)   ## set global


user_agent = 'Mozilla/5.0'
#forenter=&code=2&vcode=79&Submit=+++%CC%E1%C8%A1+++


find_re = re.compile(r'font-size:17px">(.+?)</span>' ,  re.DOTALL)

#find_re.findall(f)[0]

fin_find_re = re.compile(r'<a href="downex.php.+?">(.+?)</a>' ,  re.DOTALL)

url_find_re = re.compile(r'<a href="downex.php\?url=(.+?)&name=' ,  re.DOTALL)

#fin_find_re = re.compile(r'<a href="downex.php\?url=(.+?)&name=.+?">(.+?)</a>' ,  re.DOTALL)

for nn in xrange(times):
    first_headers = {"User-Agent": user_agent, "Referer": r_url}
    fisrt_data = {}  
    fisrt_data = urllib.urlencode(fisrt_data)
    request = urllib2.Request(g_url, data=fisrt_data, headers=first_headers)
    try:
        d1 = urllib2.urlopen(request,timeout=5)
        fin = d1.read() 
        #f = open(r'z:\33.txt', 'ab')
        #f.write(fin)
        #f.close()
    except:
        print 'fisrt error dl'
        continue

    #raw_input('>>')
    #vcode = raw_input('use code:')
    vcode = find_re.findall(fin)[0]

    headers = { 'User-Agent' : user_agent , "Cache-Control" : "no-cache" , "Connection" : "keep-alive", \
            'Referer': r_url , 'cookie':'cookie_vcode=%s ; down_fail_cnt=0; cookie_vcode_ok=1' %(vcode)}

    no = ''
    fin_data = {'forenter': no, 'code': str(nn) ,'vcode': vcode,'Submit': '+++%CC%E1%C8%A1+++'}  
    fin_data = urllib.urlencode(fin_data)
    req = urllib2.Request(g_url, data=fin_data, headers=headers)
    try:
        fd = urllib2.urlopen(req,timeout=5).read()
        #print fin_find_re.findall(fd)
        name = fin_find_re.findall(fd)[0]
        ssurl = url_find_re.findall(fd)[0]
        print 'name:', name
        print 'url:', ssurl
        #f = open(r'z:\111.txt','ab')
        #f.write(fd)
        #f.close()
        #print repr(fd)
        #time.sleep(10)
    except:
        pass
        #print 'error'
        #_error += 1
        #time.sleep(1)

print 'finish times: %d seconds' % int(round(time.time()-starttime))
print 'error times: %d ' %(_error)
#raw_input('done, enter to get out')



'''
use code:75
use code:73
use code:49
finish times: 22 seconds
error times: 0
'''
