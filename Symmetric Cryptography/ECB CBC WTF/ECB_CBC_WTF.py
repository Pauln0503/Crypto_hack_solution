import os
iv = os.urandom(16)
print(iv.hex())

ok = "db67a2ff2c5c9433b4029b74f0f79c1a  2732e98f18ae233695005ba1ce5041749d792ed205c1efb7c316971e2a7a8024"

ciphertext = iv.hex() + ok
print(ok)

db67a2ff2c5c9433b4029b74f0f79c1a
b815db8f5833ef00d760c4418594f72f78069fbf29ca7c07a25f7a80ef716009


'2732e98f18ae233695005ba1ce504174    9d792ed205c1efb7c316971e2a7a8024'

flag = 'crypto{3cb_5uck5_4v01d_17_!!!!!}'