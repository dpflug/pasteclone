import random, string

# ok, let's explain this code. It's a Dango snippet I found, slightly modified.
# http://djangosnippets.org/snippets/814/
# It's used to generate random hashes for the pastes.

# This block builds a string out of a lowercase alphabet and 0-9.
# It removes 1, l, o, and 0 because they can be ambiguous in some fonts.
alphabet = filter(
    lambda x: x not in "1l0o",
    string.ascii_lowercase + string.digits)

def byte_to_base32_chr(byte):
    """Takes a byte and bitwise ANDs it with 31 to get one of the
    string characters."""
    return alphabet[byte & 31]

def random_id(length):
    """Given length, returns a string of that length by pulling random
    characters from the alphabet created above."""
    random_bytes = [random.SystemRandom().randint(0, 0xFF) for i in range(length)]
    return ''.join(map(byte_to_base32_chr, random_bytes))
