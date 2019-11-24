import random
import string
salt = ''
for i in range(16):
    salt += random.choice(string.ascii_letters.lower()+'1234567890')
print (salt)