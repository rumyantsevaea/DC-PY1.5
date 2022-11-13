from random import sample
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnopqrstuvwxyz1234567890'
def get_random_password(n) -> str:
    return ''.join(sample(s,n))

print(get_random_password(8))
