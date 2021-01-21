import hashlib

S = input()
encoded = S.encode()
hexdigest = hashlib.sha256(encoded).hexdigest()
print(hexdigest)