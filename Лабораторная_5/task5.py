from random import sample
import string
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s = s1 + s2 + s3
def get_random_password(n) -> str:
    return ''.join(sample(s,n))

print(get_random_password(8))
