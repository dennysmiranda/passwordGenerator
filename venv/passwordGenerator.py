import string
from random import *

characters = string.ascii_letters + string.digits + string.punctuation + string.hexdigits
password = ''.join(choice(characters) for x in range(randint(8, 15)))

print(password)