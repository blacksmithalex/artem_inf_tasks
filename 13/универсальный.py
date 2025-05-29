from ipaddress import *
ip=ip_network('172.16.192.0/255.255.192.0',0)
c=0
for x in ip:
    if f'{x:b}'.count('1')%5!=0:
        c+=1
print(c)