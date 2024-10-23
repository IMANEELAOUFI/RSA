# RSA

## Principe général de l'algorithme:

#### Génération de clés :
- Choisir deux grands nombres premiers distincts `p` et `q`.
- Calculer leur produit `n = p × q`, qui sera utilisé comme partie de la clé publique.
- Calculer `ϕ(n) = (p−1) × (q−1)`, où `ϕ(n)` est la fonction indicatrice d'Euler.
- Choisir un entier `e` tel que `1 < e < ϕ(n)`, et que `gcd(e , ϕ(n)) = 1`, c'est-à-dire, `e` et `ϕ(n)` doivent être premiers entre eux.
- Calculer l'inverse modulaire de `e`, appelé `d`, tel que `e × d ≡ 1 (mod ϕ(n))`.
- La clé publique sera `(e, n)`, et la clé privée sera `(d, n)`.

#### Chiffrement :
- Pour chiffrer un message `m` (converti en nombre), on utilise la clé publique `(e, n)`.
- Le message chiffré `c` est obtenu en calculant `c = m^e (mod n)`.

#### Déchiffrement :
- Pour déchiffrer le message chiffré `c`, on utilise la clé privée `(d, n)`.
- Le message déchiffré `m` est récupéré en calculant `m = c^d (mod n)`.

## Modification proposée
Dans cette version modifiée de RSA, nous introduisons un troisième nombre premier pour augmenter la sécurité du système, ainsi qu'un facteur aléatoire pour renforcer la protection contre certaines attaques cryptographiques.

#### 1. Génération de clés :
- Étape 1 : Choisir trois grands nombres premiers distincts `p`, `q` et `r`.
- Étape 2 : Calculer leur produit : 
  `n = p × q × r`, 
  qui sera utilisé comme partie de la clé publique.
- Étape 3 : Calculer la fonction indicatrice d'Euler :
  `φ(n) = (p−1) × (q−1) × (r−1)`, 
  cela permet de connaître le nombre de coprimes avec `n`.
- Étape 4 : Choisir un entier `e` tel que : 
  `1 < e < φ(n)` et `gcd(e, φ(n)) = 1`. 
  Autrement dit, `e` doit être premier avec `φ(n)`.
- Étape 5 : Calculer l’inverse modulaire de `e`, appelé `d`, tel que : 
  `e × d ≡ 1 (mod φ(n))`. 
  Cela garantit que `d` est l'inverse de `e` modulo `φ(n)` et que l'on pourra déchiffrer les messages.
- Résultat : La clé publique est `(e, n)` et la clé privée est `(d, n)`.

#### 2. Chiffrement :
Pour améliorer la sécurité, nous introduisons un facteur aléatoire dans le chiffrement. Voici le processus :
- Étape 1 : Convertir le message `m` en un nombre si nécessaire (dans le cas d'un texte).
- Étape 2 : Choisir un facteur aléatoire `k`, où `k` est un entier aléatoire choisi pour chaque chiffrement.
- Étape 3 : Le message chiffré `c` est alors calculé comme : 
  `c = (m^e × k) (mod n)`. 
  Cela introduit une couche de complexité qui renforce la sécurité du chiffrement en rendant plus difficile l'attaque par analyse du texte chiffré.

#### 3. Déchiffrement :
Pour déchiffrer un message chiffré avec cette version modifiée de RSA :
- Étape 1 : Le destinataire doit connaître à la fois la clé privée `(d, n)` et le facteur aléatoire `k` utilisé lors du chiffrement.
- Étape 2 : Le message original `m` est récupéré via : 
  `m = (c^d / k) (mod n)`.
  Grâce à l’inversion modulaire, on peut récupérer correctement le message initial `m`.
