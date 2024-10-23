import random
from math import gcd

# Function to compute the modular inverse
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


def generate_keys():
    p = 7
    q = 11
    r = 13
    n = p * q * r
    phi_n = (p - 1) * (q - 1) * (r - 1)

    e = 7
    while gcd(e, phi_n) != 1:
        e += 1

    d = modinv(e, phi_n)
    return (e, n), (d, n)


def encrypt(message, pub_key):
    e, n = pub_key
    k = random.randint(2, n - 1)
    while gcd(k, n) != 1:
        k = random.randint(2, n - 1)


    text_as_numbers = [ord(char) for char in str(message)]
    encrypted_message = [(pow(num, e, n) * k) % n for num in text_as_numbers]

    return encrypted_message, k


def decrypt(encrypted_message, priv_key, k):
    d, n = priv_key

    k_inv = modinv(k, n)

    decrypted_numbers = [(pow(num * k_inv % n, d, n)) for num in encrypted_message]

    return ''.join([chr(num) for num in decrypted_numbers])

def rsa_example():
    pub_key, priv_key = generate_keys()

    message = input("Entrez un message (nombre ou texte) : ")
    encrypted_message, k = encrypt(message, pub_key)
    print(f"Message chiffré : {encrypted_message}")

    decrypted_message = decrypt(encrypted_message, priv_key, k)
    print(f"Message déchiffré : {decrypted_message}")


rsa_example()
