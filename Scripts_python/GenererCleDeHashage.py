import hashlib

def double_sha1(chaine: str) -> str:
    """Algorithme spécifique : SHA1(SHA1(chaine))"""
    return hashlib.sha1(hashlib.sha1(chaine.encode("utf-8")).digest()).hexdigest()

def main():
    while True:
        print("\n=== Menu des algorithmes de hachage disponibles ===")
        # Affiche tous les algorithmes disponibles
        algos = sorted(hashlib.algorithms_available)
        for i, algo in enumerate(algos, start=1):
            print(f"{i} - {algo}")
        print(f"{len(algos)+1} - double sha1 (spécial)")
        print("0 - quitter")

        try:
            choix = int(input("Choisissez un algorithme : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if choix == 0:
            print("Fin du programme.")
            break

        chaine = input("Entrez la chaîne à hacher : ")

        if 1 <= choix <= len(algos):
            algo = algos[choix-1]
            try:
                h = hashlib.new(algo)
                h.update(chaine.encode("utf-8"))
                resultat = h.hexdigest()
            except ValueError:
                print(f"Algorithme {algo} non supporté.")
                continue
        elif choix == len(algos)+1:
            resultat = double_sha1(chaine)
        else:
            print("Choix invalide, veuillez réessayer.")
            continue

        print(f"Clé de hachage ({algo if choix<=len(algos) else 'double sha1'}) : {resultat}")

if __name__ == "__main__":
    main()
