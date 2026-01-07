# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import os
import codecs

# Chemin du fichier d'entrée (Android)
INPUT_PATH = "input.txt"

def main():
    if not os.path.exists(INPUT_PATH):
        print("Fichier introuvable : %s" % INPUT_PATH)
        sys.exit(1)

    # Lire le texte en UTF-8
    with codecs.open(INPUT_PATH, "r", "utf-8") as f:
        texte = f.read()

    if not texte.strip():
        print("Fichier vide.")
        sys.exit(1)

    # Transformation : mettre en minuscules
    resultat = texte.lower()

    # Afficher le résultat directement dans la console
    print(resultat)

if __name__ == "__main__":
    main()
