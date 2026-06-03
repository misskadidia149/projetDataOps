import random

def generer_mdp(n):
    caractere=("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    mot_de_passe= ""
    for i in range(n):
        mot_de_passe +=random.choice(caractere)
    return mot_de_passe
print(generer_mdp(12))
print(generer_mdp(5))