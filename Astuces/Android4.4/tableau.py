#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import sys
import textwrap
import codecs
import os

# Forcer stdin / stdout en UTF-8 (Python 2)
sys.stdin = codecs.getreader('utf-8')(sys.stdin)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

# Separateur CSV
sep = ";"   # ",", "\t", etc.

# LARGEUR MAXIMALE DU TABLEAU
MAX_TABLE_WIDTH = 120

def lire_lignes_csv(texte, sep=","):
    lignes_brutes = texte.splitlines()
    lignes = []

    for ligne in lignes_brutes:
        lignes.append(ligne.split(sep))

    if not lignes:
        return []

    max_cols = max(len(l) for l in lignes)
    return [l + [""] * (max_cols - len(l)) for l in lignes]


def largeurs_colonnes(lignes):
    return [
        max(len(row[c]) for row in lignes)
        for c in range(len(lignes[0]))
    ]


def ajuster_largeurs_dynamique(largeurs, max_width):
    nb = len(largeurs)
    bordures = 3 * nb + 1
    espace = max_width - bordures

    if espace <= nb:
        return [1] * nb

    total = sum(largeurs)
    if total <= espace:
        return largeurs[:]

    nouvelles = [max(1, int(w * espace / total)) for w in largeurs]

    diff = espace - sum(nouvelles)
    i = 0
    while diff != 0:
        idx = i % nb
        if diff > 0:
            nouvelles[idx] += 1
            diff -= 1
        elif nouvelles[idx] > 1:
            nouvelles[idx] -= 1
            diff += 1
        i += 1

    return nouvelles


def separateur_ligne(largeurs):
    return "+" + "+".join("-" * (w + 2) for w in largeurs) + "+"


def wrap_cell(cell, largeur):
    if not cell:
        return [u""]
    return textwrap.wrap(
        cell,
        width=largeur,
        replace_whitespace=False,
        drop_whitespace=False
    ) or [u""]


def generer_tableau(lignes, max_width):
    if not lignes:
        return u""

    largeurs = largeurs_colonnes(lignes)
    largeurs = ajuster_largeurs_dynamique(largeurs, max_width)

    sep_line = separateur_ligne(largeurs)
    resultat = [sep_line]

    for ligne in lignes:
        cellules = [wrap_cell(cell, w) for cell, w in zip(ligne, largeurs)]
        hauteur = max(len(c) for c in cellules)

        for i in range(hauteur):
            row = u"| "
            for cell_lines, w in zip(cellules, largeurs):
                texte = cell_lines[i] if i < len(cell_lines) else u""
                row += texte.ljust(w) + u" | "
            resultat.append(row.rstrip())

        resultat.append(sep_line)

    return u"\n".join(resultat)


# --- Nouveau main pour lire un fichier ---
def main():
    chemin_fichier = "input.txt"

    if not os.path.exists(chemin_fichier):
        print(u"Le fichier n'existe pas :", chemin_fichier)
        return

    with codecs.open(chemin_fichier, "r", "utf-8") as f:
        lignes_input = [ligne.rstrip("\r\n") for ligne in f]

    if not lignes_input:
        print(u"Le fichier est vide.")
        return

    texte = u"\n".join(lignes_input)
    lignes = lire_lignes_csv(texte, sep=sep)

    tableau = generer_tableau(lignes, MAX_TABLE_WIDTH)

    print(tableau)


if __name__ == "__main__":
    main()
