import psutil
from collections import defaultdict
from collections import OrderedDict

addr={}
countdict={}
process=psutil.net_connections(kind='tcp')

addr=defaultdict(list)
for i in range(len(process)):
  
   if process[i].laddr and process[i].raddr:
      laddr = "%s@%s" %(process[i].laddr)
      raddr = "%s@%s" %(process[i].raddr)
      addr[process[i].pid].append([laddr,raddr,process[i].status])
i=i+1;

for mykey in addr.keys():

    countdict[mykey]=len(addr[mykey])


desc=OrderedDict(sorted(countdict.items(),key=lambda kv: kv[1],reverse=True))

print 'PID      ,laddr          ,raddr          ,status'
for i in desc.keys():
 
 for n in addr[i]:
    print "\"%s\", \"%s\", \"%s\", \"%s\"" % (i,n[0],n[1],n[2])
