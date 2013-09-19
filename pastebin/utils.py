import random, string

alphabet = filter(
    lambda x: x not in "1l0o",
    string.ascii_lowercase + string.digits)

def byte_to_base32_chr(byte):
    return alphabet[byte & 31]

def random_id(length):
    random_bytes = [random.SystemRandom().randint(0, 0xFF) for i in range(length)]
    return ''.join(map(byte_to_base32_chr, random_bytes))
