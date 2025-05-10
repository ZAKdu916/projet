import itertools
import string

# Génération de toutes les combinaisons de 4 lettres
def brute_force_4_letters():
    alphabet = string.ascii_lowercase
    for combination in itertools.product(alphabet, repeat=4):
        password = ''.join(combination)
        print(password)

if __name__ == "__main__":
    brute_force_4_letters()

