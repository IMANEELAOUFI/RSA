# RSA
## Principe général de l'algorithme:
#### Génération de clés :
•	Choisir deux grands nombres premiers distincts `p` et `q`.
•	Calculer leur produit `n = p × q`, qui sera utilisé comme partie de la clé publique.
•	Calculer `ϕ(n) = (p−1) × (q−1)`,  où `ϕ(n)` est la fonction indicatrice d'Euler.
•	Choisir un entier `e` tel que `1 < e < ϕ(n)`, et que `gcd(e , ϕ(n)) = 1`, c'est-à-dire, `e` et `ϕ(n)` doivent être premiers entre eux.
•	Calculer l'inverse modulaire de `e`, appelé `d`, tel que `e × d ≡ 1 (modϕ(n))`.
•	La clé publique sera `(e,n)`, et la clé privée sera `(d,n)`.
#### Chiffrement :
•	Pour chiffrer un message `m` (converti en nombre), on utilise la clé publique `(e,n)`.
•	Le message chiffré `c` est obtenu en calculant `c = m^e (mod n)`.
#### Déchiffrement :
•	Pour déchiffrer le message chiffré `c`, on utilise la clé privée `(d,n)`.
•	Le message déchiffré `m` est récupéré en calculant `m = c^d (mod n)`.

## Modification proposée
#### Génération de clés :
•	En plus des nombres `p` et `q`, on peut choisir un troisième nombre premier `r` et calculer `n = p × q × r`.
•	On ajuste la fonction indicatrice d'Euler : 
                                     `ϕ(n)=(p−1) × (q−1) × (r−1)`.
•	Le reste de la génération des clés est similaire, sauf que les calculs de chiffrement et déchiffrement se feront modulo `n = p × q × r`.
#### Chiffrement :
•	On introduit un masque supplémentaire lors du chiffrement. Par exemple, avant de calculer `c = m^e (mod n)`, on peut introduire un facteur aléatoire `k`, tel que : 
                                        `c = (m^e × k)(mod n)`.
•	 Le facteur `k` doit être un entier aléatoire choisi lors de chaque chiffrement pour ajouter une couche de sécurité.
#### Déchiffrement :
•	Le récepteur connaissant le facteur `k` peut l'utiliser pour déchiffrer correctement le message. Le déchiffrement devient : 
                               `m = ( c^d / k)(mod n)`
•	Cela ajoute une petite complexité, mais peut offrir une résistance supplémentaire contre certaines attaques.
