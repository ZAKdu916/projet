import itertools

# Génération de toutes les combinaisons de 4 chiffres
def brute_force_4_digits():
    for combination in itertools.product("0123456789", repeat=4):
        password = ''.join(combination)
        print(password)

if __name__ == "__main__":
    brute_force_4_digits()

