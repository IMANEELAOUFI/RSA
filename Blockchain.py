import random
from math import gcd


# Fonction pour calculer l'inverse modulaire
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


# Génération des clés RSA avec 3 nombres premiers
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
    k = random.randint(1, n - 1)
    while gcd(k, n) != 1:  # k doit être co-prime avec n
        k = random.randint(1, n - 1)

    # Chiffrement
    c = (pow(message, e, n) * k) % n
    return c, k

# Déchiffrement :
def decrypt(ciphertext, priv_key, k):
    d, n = priv_key
    c_prime = (ciphertext * modinv(k, n)) % n
    message = pow(c_prime, d, n)
    return message


# Exemple d'utilisation
def rsa_example():
    # Générer les clés publique et privée
    pub_key, priv_key = generate_keys()

    # Le message à chiffrer (doit être < n)
    message = 30
    print(f"Message original: {message}")

    # Chiffrement

    ciphertext, k = encrypt(message, pub_key)
    print(f"Message chiffré: {ciphertext}, avec le facteur k: {k}")

    # Déchiffrement
    decrypted_message = decrypt(ciphertext, priv_key, k)
    print(f"Message déchiffré: {decrypted_message}")


rsa_example()
