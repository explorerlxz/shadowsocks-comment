#!/usr/bin/env python

"""
git checkout 341ce50

This program encrypt a string with encrypt_table and then
decrypt the string with decrypt_table


"""



import string
import struct
import hashlib

key="foobar!"
m=hashlib.md5()
m.update(key)
s=m.digest()
(a,b)=struct.unpack('<QQ',s)
table=[c for c in string.maketrans('','')]

# Get encrypt table
for i in xrange(1,1024):
    table.sort(lambda x,y: int(a % (ord(x) +i) -a % (ord(y) +i)))

output = []

#print("table:\n")
#print table

# Data to be encrypted

data="ABCDEFGHIJKLMNOPQRSTUVWXYZadbcefghijklmnopqrstuvwxyz1234567890"

print "Before encrypte :\n{}".format(data.encode('hex'))
print data+"\n"

encrypt_table=''.join(table)
decrypt_table=string.maketrans(encrypt_table, string.maketrans('',''))

# Data encrypted

encdata=data.translate(encrypt_table)


print "After encrypte: \n{}".format(encdata.encode('hex'))
print(encdata)+"\n"

# Decrypt encdata with decrypt_table

decdata=encdata.translate(decrypt_table)
print "After decrypte: \n{}\n".format(decdata)


print("Encrypt table: \n")
entable=[c for c in encrypt_table]

#print entable
    
for line in xrange(0,16):
    for column in xrange(0,16):
        output.append(entable[line*16+column])
    print output
    output = []

print("\nDecrypt table: \n")
detable=[c for c in decrypt_table]

#print detable

for line in xrange(0,16):
    for column in xrange(0,16):
        output.append(detable[line*16+column])
    print output
    output = []
