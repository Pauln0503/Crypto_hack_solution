#!/usr/bin/env python3

import sys
import base64
from Crypto.Util.number import *
from pwn import xor
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

#what an ex
key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
res1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
key2 = bytes([x^y for x,y in zip(key1,res1)])

res2 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
key3 = bytes([x^y for x,y in zip(key2,res2)])

res3 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf") 
a =  bytes([x^y for x,y in zip(key3,res3)])
b =  bytes([x^y for x,y in zip(key2,a)])
flag =  bytes([x^y for x,y in zip(key1,b)])


#xor sing bytes
okay = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
damn = ""
for i in range(256):
    #print("At iterator: " , i)
    key = bytes([i] * len(okay))
    result = bytes([x^y for x,y in zip(okay,key)])
    res = result.decode()
    try:
        if "crypto" in res:
            damn = res
            break
    except UnicodeDecodeError:
        continue
#print(damn)

#the last one
keyy = b'myXORkey'
last2 = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
last_convert2 = bytes.fromhex(last2)
full_key = (keyy * (len(last_convert2) // len(keyy) + 1))[:len(last_convert2)]
halfkey = b"crypto{"
result = bytes([x^y for x,y in zip(last_convert2,full_key)])
print(result)



#print("".join(str(bytes.fromhex(ok))))
