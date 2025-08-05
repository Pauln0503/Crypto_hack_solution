from pyasn1.codec.der.decoder import decode
from pyasn1_modules import rfc2459
from Crypto.PublicKey import RSA

with open("2048b-rsa-example-cert.der", "rb") as f:
    der_data = f.read()

cert, _ = decode(der_data, asn1Spec=rfc2459.Certificate())

subject_public_key_info = cert['tbsCertificate']['subjectPublicKeyInfo']
modulus_bitstring = subject_public_key_info['subjectPublicKey'].asOctets()

print(subject_public_key_info)


rsa_key = RSA.import_key(modulus_bitstring)
print("Modulus (decimal):", rsa_key.n)